"""Services and classes."""

from datetime import datetime, timedelta, timezone
from time import time
from typing import Any
from uuid import UUID, uuid4

import kaiju_tools.jsonschema as j
import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as sa_pg
from croniter import croniter
from kaiju_db import DatabaseService, PermHook, SQLService
from kaiju_redis import RedisTransportService
from kaiju_tools.app import SERVICE_CLASS_REGISTRY, ContextableService, Scheduler
from kaiju_tools.exceptions import InternalError, ValidationError
from kaiju_tools.functions import get_short_uid, retry
from kaiju_tools.interfaces import PublicInterface
from kaiju_tools.rpc import JSONRPCHeaders, JSONRPCServer, RPCError
from kaiju_tools.streams import StreamRPCClient, Topic
from kaiju_tools.templates import Condition, Template
from kaiju_tools.types import Scope

from kaiju_tasks.types import (
    ExecutorTask,
    ExitCode,
    Limit,
    Message,
    Notification,
    RestartPolicy,
    Task,
    TaskCommand,
    TaskStatus,
    Timer,
)


__all__ = ['TaskService', 'NotificationService', 'TaskManager', 'TaskExecutor']


class TaskService(SQLService[str, Task], PermHook, PublicInterface):
    """Tasks public interface.

    This service should be used to create, view or modify tasks. The interface is the same as in `SQLService`.

    Task service is not required by executors so you can have a single task service for different executor applications.
    """

    service_name = 'tasks'
    table = sa.Table(
        'tasks',
        sa.MetaData(),
        sa.Column('id', sa_pg.TEXT, primary_key=True),
        # executor instructions
        sa.Column('app_name', sa_pg.TEXT, nullable=False),
        sa.Column('commands', sa_pg.JSONB, nullable=False),
        sa.Column('kws', sa_pg.JSONB, nullable=False),
        # manager instructions
        sa.Column('enabled', sa_pg.BOOLEAN, nullable=False),
        sa.Column('cron', sa_pg.TEXT, nullable=True),
        sa.Column('max_exec_timeout', sa_pg.INTEGER, nullable=False),
        sa.Column('max_retries', sa_pg.INTEGER, nullable=False),
        sa.Column('restart_policy', sa_pg.TEXT, nullable=False),
        sa.Column('notify', sa_pg.BOOLEAN, nullable=False),
        sa.Column('next_task', sa.ForeignKey('tasks.id', ondelete='SET NULL'), nullable=True),
        sa.Column('system', sa_pg.BOOLEAN, nullable=False),
        # meta
        sa.Column('description', sa_pg.TEXT, nullable=True),
        sa.Column('meta', sa_pg.JSONB, nullable=False, default={}),
        # managed
        sa.Column('status', sa_pg.TEXT, nullable=False),
        sa.Column('result', sa_pg.JSONB, nullable=False),
        sa.Column('stage', sa_pg.INTEGER, nullable=False),
        sa.Column('stages', sa_pg.INTEGER, nullable=False),
        sa.Column('created', sa_pg.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('queued_at', sa_pg.INTEGER, nullable=True),
        sa.Column('exec_deadline', sa_pg.INTEGER, nullable=True),
        sa.Column('wait_deadline', sa_pg.INTEGER, nullable=True),
        sa.Column('next_run', sa_pg.INTEGER, nullable=True),
        sa.Column('status_change', sa_pg.INTEGER, nullable=True),
        sa.Column('user_id', sa_pg.UUID(as_uuid=True), nullable=True),
        sa.Column('executor_id', sa_pg.UUID(as_uuid=True), nullable=True),
        sa.Column('job_id', sa_pg.TEXT, nullable=True),
        sa.Column('retries', sa_pg.INTEGER, nullable=False),
        sa.Column('exit_code', sa_pg.INTEGER, nullable=True),
        sa.Column('error', sa_pg.JSONB, nullable=True),
    )
    sa.Index(
        f'idx__{table.name}__queued_at',
        sa.nulls_last(sa.desc(table.c.queued_at)),
        postgresql_where=table.c.enabled.is_(True),
    )
    sa.Index(
        f'idx__{table.name}__wait_deadline',
        sa.nulls_last(sa.desc(table.c.wait_deadline)),
        postgresql_where=table.c.enabled.is_(True),
    )
    sa.Index(
        f'idx__{table.name}__next_run',
        sa.nulls_last(sa.desc(table.c.next_run)),
        postgresql_where=table.c.enabled.is_(True),
    )
    sa.Index(
        f'idx__{table.name}__cron',
        table.c.cron,
        postgresql_where=sa.and_(sa.not_(table.c.cron.is_(None)), table.c.enabled.is_(True)),
    )
    sa.Index(
        f'idx__{table.name}__status__idle',
        sa.nulls_last(sa.desc(table.c.next_run)),
        postgresql_where=table.c.enabled.is_(True),
    )

    _task_command = j.Object(
        {'id': j.Integer(), 'method': j.String(), 'params': j.Object()}, additionalProperties=False, required=['method']
    )

    _task_validator = j.Object(
        {
            'id': j.String(minLength=1),
            'app_name': j.String(),
            'commands': j.Array(_task_command, minItems=1, maxItems=Limit.MAX_STAGES.value),
            'kws': j.Object(),
            'cron': j.String(),
            'system': j.Boolean(),
            'max_exec_timeout': j.Integer(minimum=Limit.MIN_T.value, maximum=Limit.MAX_T.value),
            'max_retries': j.Integer(minimum=0, maximum=Limit.MAX_RETRIES.value),
            'restart_policy': j.Enumerated(enum=[RestartPolicy.CURRENT.value, RestartPolicy.FIRST.value]),
            'next_task': j.String(minLength=1),
            'notify': j.Boolean(),
            'description': j.String(),
            'meta': j.Object(),
            'enabled': j.Boolean(default=True),
        },
        additionalProperties=False,
        required=['commands'],
    )

    @property
    def routes(self) -> dict:
        return {
            **super().routes,
            'reset': self.reset_task,
            'delete_old_tasks': self.delete_old_tasks,
            'write_message': self.write_message,
        }

    @property
    def permissions(self) -> dict:
        return {
            '*': self.PermissionKeys.GLOBAL_USER_PERMISSION,
            'delete_old_tasks': self.PermissionKeys.GLOBAL_SYSTEM_PERMISSION,
        }

    @property
    def validators(self) -> dict:
        return {'create': j.Object({'data': self._task_validator}, additionalProperties=True, required=['data'])}

    async def delete_old_tasks(self, interval_days: int = 7) -> None:
        """Delete old tasks and notifications (excluding periodic and system tasks).

        `RPC method: tasks.delete_old_tasks`

        This method can be used to remove finished not needed tasks from the database. It will not delete cron tasks
        or tasks marked as `system`. The proper way to use it is to make a cron task with this method.

        :param interval_days: delete tasks and notifications older than `interval_days` days
        """
        await self.m_delete(
            conditions={
                'cron': None,
                'created': {'lt': datetime.now() - timedelta(days=interval_days)},
                'system': False,
            },
            columns=[],
        )

    async def reset_task(self, id: str) -> bool:
        """Reset task to :py:attr:`~kaiju_tasks.types.TaskStatus.IDLE`.

        `RPC method: tasks.reset`

        All results and execution data will be removed and a new `job_id` will be assigned to the task.

        :param id: task id
        :returns: True if task has been restarted, False if it can't be restarted
        """
        restarted = await self.m_update(
            id=[id],
            data={
                'status': TaskStatus.IDLE.value,
                'executor_id': None,
                'job_id': get_short_uid(),
                'exit_code': None,
                'error': None,
                'retries': 0,
                'exec_deadline': None,
                'wait_deadline': None,
                'status_change': int(time()),
                'stage': 0,
                'result': [],
            },
            columns=['id'],
        )
        return bool(restarted)

    async def write_message(self, id: str, data: dict) -> bool:
        """Send a message to a running task.

        `RPC method: tasks.write_message`

         The task must be :py:attr:`~kaiju_tasks.types.TaskStatus.WAITING`.
         The task will continue to the next stage only after it receives a message.

        :param id: task id
        :param data: message data will be available in the task results for the next stage
        :returns: True if a task has received the message
        """
        updated = await self.m_update(
            id=[id],
            data={
                'status': TaskStatus.SUSPENDED.value,
                'result': self.table.c.result + [data],
                'stage': self.table.c.stage + 1,
                'status_change': int(time()),
                'executor_id': None,
            },
            conditions={'status': TaskStatus.WAITING.value},
            columns=['id'],
        )
        return bool(updated)

    def prepare_insert_data(self, data: dict):
        """Prepare task object."""
        data = self._validate_data(data)
        task = Task(
            id=data.get('id', str(uuid4()).replace('-', '')),
            app_name=data.get('app_name', self.app.name),
            commands=[TaskCommand(method=cmd['method'], params=cmd.get('params')) for cmd in data['commands']],
            kws=data.get('kws', {}),
            cron=data.get('cron'),
            max_exec_timeout=data.get('max_exec_timeout', Limit.DEFAULT_T.value),
            max_retries=data.get('max_retries', 0),
            description=data.get('description'),
            meta=data.get('meta', {}),
            notify=data.get('notify', False),
            restart_policy=data.get('restart_policy', RestartPolicy.CURRENT.value),
            enabled=data.get('enabled', True),
            system=data.get('system', False),
            status=TaskStatus.IDLE.value,
            stage=0,
            stages=len(data['commands']),
            result=[],
            created=sa.func.now(),
            queued_at=None,
            exec_deadline=None,
            wait_deadline=None,
            next_run=int(time()),
            user_id=self.get_user_id(),
            executor_id=None,
            job_id=get_short_uid(),
            retries=0,
            exit_code=None,
            error=None,
            next_task=data.get('next_task'),
        )
        return task

    def prepare_update_data(self, data: dict):
        """Prepare task object."""
        return self._validate_data(data)

    @staticmethod
    def _validate_data(data: dict) -> dict:
        cron = data.get('cron')
        if cron:
            croniter(data.get('cron'), start_time=datetime.now()).next()  # testing for validity
        commands = data.get('commands')
        if commands and len(commands) == 0:
            raise ValidationError('Commands must not be empty.')
        return data


class NotificationService(SQLService[UUID, Notification], PermHook, PublicInterface):
    """Task notifications interface.

    Notification service stores task job history for `notify` tasks. Its interface is similar to `SQLService`.

    Executors do not require notification service.
    """

    service_name = 'notifications'

    table = sa.Table(
        'notifications',
        sa.MetaData(),
        sa.Column('id', sa_pg.UUID(as_uuid=True), primary_key=True, server_default=sa.text('uuid_generate_v4()')),
        sa.Column('task_id', sa.ForeignKey(TaskService.table.c.id, ondelete='CASCADE'), nullable=True),
        sa.Column('message', sa_pg.TEXT, nullable=True),
        sa.Column('kws', sa_pg.JSONB, nullable=True, server_default=sa.text("'{}'::jsonb")),
        sa.Column('created', sa_pg.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.Column('enabled', sa_pg.BOOLEAN, nullable=False, default=True),
        sa.Column('meta', sa_pg.JSONB, nullable=False, default={}),
        sa.Column('user_id', sa_pg.UUID(as_uuid=True), nullable=True),
        sa.Column('job_id', sa_pg.TEXT, nullable=True),
        sa.Column('status', sa_pg.TEXT, nullable=True),
        sa.Column('result', sa_pg.JSONB, nullable=True),
        sa.Column('exit_code', sa_pg.INTEGER, nullable=True),
        sa.Column('error', sa_pg.JSONB, nullable=True),
    )
    sa.Index('idx_notification_timestamp', table.c.user_id, sa.desc(table.c.created))

    update_columns = {'enabled'}


class TaskManager(ContextableService, PublicInterface):
    """Task manager schedules tasks execution."""

    service_name = 'taskman'
    table = TaskService.table

    def __init__(
        self,
        app,
        stream_client: StreamRPCClient = None,
        database_service: DatabaseService = None,
        redis_transport: RedisTransportService = None,
        notification_service: NotificationService = None,
        scheduler_service: Scheduler = None,
        executor_topic: str = Topic.EXECUTOR,
        refresh_rate: int = 1,
        suspended_task_lifetime_hours: int = 24,
        logger=None,
    ):
        """Initialize.

        :param app: web app
        :param database_service: database connector instance or service name
        :param stream_client: stream client to the executor
        :param redis_transport: a cache for executor states\
        :param notification_service: notification service instance or service name
        :param scheduler_service: internal loop scheduler
        :param refresh_rate: watcher loop refresh rate in seconds
        :param executor_topic: optional topic name for executor
        :param suspended_task_lifetime_hours: if task was last queued before this interval, it won't be executed again
        :param logger: optional logger
        """
        super().__init__(app=app, logger=logger)
        self._db = self.discover_service(database_service, cls=DatabaseService)
        self._scheduler = scheduler_service
        self._stream = stream_client
        self._notifications = notification_service
        self._redis = redis_transport
        self._refresh_interval = max(1, int(refresh_rate))
        self._suspended_lifetime = max(1, int(suspended_task_lifetime_hours))
        self._executor_topic = executor_topic
        self.executor_map_key = f'{self.service_name}.executors'
        self._task = None
        self._closing = None

    @property
    def routes(self) -> dict:
        return {
            'list_active_executors': self.list_active_executors,
            'ping': self.ping,
            'suspend_executor': self.suspend_executor,
            'execute_stage': self.execute_stage,
            'write_stage': self.write_stage,
            'wait_for_message': self.wait_for_message,
            'wait_for_timer': self.wait_for_timer,
        }

    @property
    def permissions(self) -> dict:
        return {'*': self.PermissionKeys.GLOBAL_SYSTEM_PERMISSION}

    async def init(self):
        self._closing = False
        self._scheduler: Scheduler = self.discover_service(self._scheduler, cls=Scheduler)
        self._notifications = self.discover_service(self._notifications, cls=NotificationService)
        self._redis = self.discover_service(self._redis, cls=RedisTransportService)
        self._stream = self.discover_service(self._stream, cls=StreamRPCClient)
        self._task = self._scheduler.schedule_task(
            self._queue_tasks, interval=self._refresh_interval, policy=Scheduler.ExecPolicy.WAIT, name='taskman.loop'
        )

    async def close(self):
        self._task.enabled = False

    @property
    def closed(self) -> bool:
        return self._closing is None

    async def list_active_executors(self) -> dict:
        """Return executor ids and their last ping time.

        `RPC method: manager.list_active_executors`
        """
        return await self._redis.hgetall(self.executor_map_key)

    async def ping(self, executor_id: UUID) -> None:
        """Receive ping from an executor.

        `RPC method: manager.ping`

        This method is used by executors to tell the manager that they are alive.

        :param executor_id: executor instance app id
        """
        await self._redis.hset(self.executor_map_key, {str(executor_id): int(time())})

    async def suspend_executor(self, executor_id: UUID) -> None:
        """Suspend an executor and its tasks.

        `RPC method: manager.suspend_executor`

        This method is used by an executor when it's about to exit.

        :param executor_id: executor instance app id
        """
        self.logger.info('Suspending executor', executor_id=executor_id)
        t = int(time())
        sql = (
            self.table.update()
            .where(sa.and_(self.table.c.status == TaskStatus.EXECUTED.value, self.table.c.executor_id == executor_id))
            .values({'status': TaskStatus.SUSPENDED.value, 'executor_id': None, 'status_change': t})
        )
        await self._db.execute(sql)
        await self._redis.hdel(self.executor_map_key, [str(executor_id)])

    async def execute_stage(self, task_id: str, executor_id: UUID, stage: int, timestamp: int) -> None:
        """Accept an executor report on stage execution.

        `RPC method: manager.execute_stage`

        This method is used by an executor before each stage to notify the manager which stage is being executed.

        :param task_id: task id
        :param executor_id: executor instance app id
        :param stage: current stage
        :param timestamp: executor UNIX time
        """
        self.logger.info('Stage executed', task_id=task_id, stage=stage, executor_id=executor_id)
        sql = (
            self.table.update()
            .where(
                sa.and_(
                    self.table.c.id == task_id,
                    self.table.c.status == TaskStatus.QUEUED.value,
                    self.table.c.status_change <= timestamp,
                )
            )
            .values(
                {
                    'status': TaskStatus.EXECUTED.value,
                    'stage': stage,
                    'executor_id': executor_id,
                    'status_change': timestamp,
                }
            )
        )
        await self._db.execute(sql)
        await self.ping(executor_id)

    async def wait_for_timer(self, task_id: str, executor_id: UUID, stage: int, timer: int, timestamp: int) -> None:
        """Require a task to wait for a message to continue.

        `RPC method: manager.wait_for_timer`

        The task will continue after certain timeout. This method is used by an executor
        when it encounters a :py:class:`~kaiju_tasks.types.Timer` special command.

        :param task_id: task id
        :param executor_id: executor instance app id
        :param stage: current stage
        :param timer: timer value in seconds
        :param timestamp: executor UNIX time
        """
        sql = (
            self.table.update()
            .where(
                sa.or_(
                    sa.and_(self.table.c.id == task_id, self.table.c.executor_id == executor_id),
                    sa.and_(
                        self.table.c.id == task_id,
                        self.table.c.executor_id.is_(None),
                        self.table.c.status == TaskStatus.QUEUED.value,
                    ),
                )
            )
            .values(
                {
                    'status': TaskStatus.WAITING.value,
                    'stage': stage,
                    'executor_id': None,
                    'wait_deadline': int(time()) + timer,
                    'status_change': timestamp,
                }
            )
        )
        await self._db.execute(sql)

    async def wait_for_message(self, task_id: str, executor_id: UUID, stage: int, timestamp: int) -> None:
        """Require a task to wait for a message to continue.

        `RPC method: manager.wait_for_message`

        The task will continue when a message to this task is received by the `TaskService`. This method is used
        by an executor when it encounters a :py:class:`~kaiju_tasks.types.Message` special command.

        :param task_id: task id
        :param executor_id: executor instance app id
        :param stage: current stage
        :param timestamp: executor UNIX time
        """
        sql = (
            self.table.update()
            .where(
                sa.or_(
                    sa.and_(self.table.c.id == task_id, self.table.c.executor_id == executor_id),
                    sa.and_(
                        self.table.c.id == task_id,
                        self.table.c.executor_id.is_(None),
                        self.table.c.status == TaskStatus.QUEUED.value,
                    ),
                )
            )
            .values(
                {'status': TaskStatus.WAITING.value, 'stage': stage, 'executor_id': None, 'status_change': timestamp}
            )
        )
        await self._db.execute(sql)

    async def write_stage(
        self, task_id: str, executor_id: UUID, stage: int, stages: int, result: Any, error: bool, timestamp: int
    ) -> None:
        """Write stage result to the task table.

        `RPC method: manager.write_stage`

        This method is used by executors to return each stage results to the manager. If it's the last stage
        or there was an error, the task will be finished and notification may be created.

        :param task_id: task id
        :param executor_id: executor instance app id
        :param stage: current stage
        :param stages: total number of stages
        :param result: result value
        :param error: result is an error
        :param timestamp: executor UNIX time
        """
        sql = self.table.update().where(
            sa.or_(
                sa.and_(self.table.c.id == task_id, self.table.c.executor_id == executor_id),
                sa.and_(
                    self.table.c.id == task_id,
                    self.table.c.executor_id.is_(None),
                    self.table.c.status == TaskStatus.QUEUED.value,
                ),
            )
        )
        columns = [self.table.c.job_id, self.table.c.result, self.table.c.notify, self.table.c.user_id]
        if error:
            sql = sql.values(
                {
                    'status': TaskStatus.FAILED.value,
                    'error': result,
                    'exit_code': ExitCode.EXECUTION_ERROR.value,
                    'executor_id': None,
                    'next_run': None,
                    'status_change': timestamp,
                }
            ).returning(*columns)
            task = await self._db.execute(sql)
            task = task.first()
            if task:
                self.logger.error('Stage failed', stage=stage, task_id=task_id, executor_id=executor_id, error=result)
                if task.notify:
                    task = task._asdict()  # noqa
                    notification = Notification(
                        message='task.result',
                        user_id=task['user_id'],
                        task_id=task_id,
                        job_id=task['job_id'],
                        status=TaskStatus.FAILED.value,
                        result=task['result'],
                        exit_code=ExitCode.EXECUTION_ERROR.value,
                        error=result,
                    )
                    await self._notifications.create(notification, columns=[])
        elif stage == stages - 1:
            columns.append(self.table.c.next_task)
            sql = sql.values(
                {
                    'status': TaskStatus.FINISHED.value,
                    'result': self.table.c.result + [result],
                    'exit_code': ExitCode.SUCCESS.value,
                    'executor_id': None,
                    'next_run': None,
                    'status_change': timestamp,
                }
            ).returning(*columns)
            task = await self._db.execute(sql)
            task = task.first()
            if task:
                self.logger.info('Task finished', stage=stage, task_id=task_id, executor_id=executor_id)
                if task.next_task:
                    self.logger.info('Starting next task', task_id=task_id, next_task=task.next_task)
                    sql = (
                        self.table.update()
                        .where(
                            sa.and_(
                                self.table.c.id == task.next_task,
                                self.table.c.status.in_(
                                    [TaskStatus.IDLE.value, TaskStatus.FAILED.value, TaskStatus.FINISHED.value]
                                ),
                                self.table.c.enabled.is_(True),
                            )
                        )
                        .values({'status': TaskStatus.IDLE.value, 'next_run': int(time())})
                    )
                    await self._db.execute(sql)
                if task.notify:
                    task = task._asdict()  # noqa
                    notification = Notification(
                        message='task.result',
                        user_id=task['user_id'],
                        task_id=task_id,
                        job_id=task['job_id'],
                        status=TaskStatus.FINISHED.value,
                        result=task['result'],
                        exit_code=ExitCode.SUCCESS.value,
                    )
                    await self._notifications.create(notification, columns=[])
        else:
            sql = sql.values({'result': self.table.c.result + [result], 'stage': stage + 1}).returning(self.table.c.id)
            task = await self._db.execute(sql)
            task = task.first()
            if task:
                self.logger.info('Stage finished', stage=stage, task_id=task_id, executor_id=executor_id)

    async def _queue_tasks(self):
        """Iterate over the tasks table."""
        await self._expell_dead_executors()
        await self._abort_timed_out_tasks()
        await self._restart_cron_tasks()
        await self._queue_timers()
        await self._queue_suspended_and_idle()
        await self._queue_failed()

    async def _expell_dead_executors(self):
        """Check if some executors are not responding and abort their tasks."""
        dead_executors = await self._list_dead_executors()
        t = int(time())
        if dead_executors:
            sql = (
                self.table.update()
                .where(
                    sa.and_(
                        self.table.c.executor_id.in_(dead_executors), self.table.c.status == TaskStatus.EXECUTED.value
                    )
                )
                .values({'status': TaskStatus.SUSPENDED.value, 'executor_id': None, 'status_change': t})
            )
            self.logger.info('Suspending dead executors', executor_id=dead_executors)
            await self._db.execute(sql)
            await self._redis.hdel(self.executor_map_key, dead_executors)

    async def _list_dead_executors(self) -> list[str]:
        """List executors with expired lifetime."""
        executors = await self._redis.hgetall(self.executor_map_key)
        t = time()
        dt = Limit.PING_INTERVAL.value * Limit.SUSPEND_AFTER_PINGS.value
        dead_executors = [key.decode('utf-8') for key, t0 in executors.items() if t - int(t0.decode('utf-8')) > dt]
        return dead_executors

    async def _queue_timers(self):
        """Queue tasks waiting for timers."""
        t = int(time())
        sql = (
            self.table.update()
            .where(
                sa.and_(
                    self.table.c.wait_deadline < int(time()),
                    self.table.c.status == TaskStatus.WAITING.value,
                    self.table.c.enabled.is_(True),
                )
            )
            .values(
                {
                    'status': TaskStatus.SUSPENDED.value,
                    'result': self.table.c.result + [None],
                    'stage': self.table.c.stage + 1,
                    'wait_deadline': None,
                    'executor_id': None,
                    'status_change': t,
                }
            )
        )
        await self._db.execute(sql)

    async def _queue_suspended_and_idle(self):
        """Queue all suspended tasks."""
        t = int(time())
        sql = (
            self.table.update()
            .where(
                sa.or_(
                    sa.and_(
                        self.table.c.next_run < int(time()),
                        self.table.c.status == TaskStatus.IDLE.value,
                        self.table.c.enabled.is_(True),
                    ),
                    sa.and_(
                        self.table.c.status == TaskStatus.SUSPENDED.value,
                        self.table.c.queued_at > int(time()) - self._suspended_lifetime * 3600,
                        self.table.c.enabled.is_(True),
                    ),
                )
            )
            .values(
                {
                    'status': TaskStatus.QUEUED.value,
                    'queued_at': int(time()),
                    'exec_deadline': int(time()) + self.table.c.max_exec_timeout,
                    'wait_deadline': None,
                    'exit_code': None,
                    'error': None,
                    'status_change': t,
                    'result': sa.text(
                        f"CASE WHEN {self.table.c.status.name} = '{TaskStatus.SUSPENDED.value}'"
                        f' THEN {self.table.c.result.name}'
                        " ELSE '[]' END"
                    ),  # CURRENT or FIRST
                }
            )
            .returning(
                self.table.c.id,
                self.table.c.commands,
                self.table.c.kws,
                self.table.c.stage,
                self.table.c.exec_deadline,
                self.table.c.app_name,
                self.table.c.result,
                self.table.c.job_id,
            )
        )
        async with self._db.begin() as conn:
            queued_tasks = await conn.execute(sql)
            queued_tasks = [r._asdict() for r in queued_tasks.all()]  # noqa
            await self._send_tasks(queued_tasks)
            await conn.commit()

    async def _abort_timed_out_tasks(self):
        """Abort all queued tasks reached their timeout."""
        t = int(time())
        sql = (
            self.table.update()
            .where(
                sa.and_(
                    self.table.c.queued_at < int(time()) - Limit.MIN_T.value - self.table.c.max_exec_timeout,
                    self.table.c.status.in_(
                        [TaskStatus.QUEUED.value, TaskStatus.EXECUTED.value, TaskStatus.WAITING.value]
                    ),
                    self.table.c.enabled.is_(True),
                )
            )
            .values(
                {
                    'status': TaskStatus.FAILED.value,
                    'error': None,
                    'exit_code': ExitCode.ABORTED.value,
                    'next_run': None,
                    'executor_id': None,
                    'status_change': t,
                }
            )
            .returning(self.table.c.id)
        )
        await self._db.execute(sql)

    async def _queue_failed(self):
        """Queue all failed tasks with available retries."""
        t = int(time())
        sql = (
            self.table.update()
            .where(
                sa.and_(
                    self.table.c.queued_at > int(time()) - self._suspended_lifetime * 3600,
                    self.table.c.status == TaskStatus.FAILED.value,
                    self.table.c.max_retries > self.table.c.retries,
                    self.table.c.enabled.is_(True),
                )
            )
            .values(
                {
                    'status': TaskStatus.QUEUED.value,
                    'queued_at': int(time()),
                    'exec_deadline': int(time()) + self.table.c.max_exec_timeout,
                    'wait_deadline': None,
                    'stage': sa.text(
                        f"CASE WHEN {self.table.c.restart_policy.name} = '{RestartPolicy.CURRENT.value}'"
                        f' THEN {self.table.c.stage.name}'
                        ' ELSE 0 END'
                    ),  # CURRENT or FIRST
                    'executor_id': None,
                    'retries': self.table.c.retries + 1,
                    'exit_code': None,
                    'status_change': t,
                }
            )
            .returning(
                self.table.c.id,
                self.table.c.commands,
                self.table.c.kws,
                self.table.c.stage,
                self.table.c.exec_deadline,
                self.table.c.app_name,
                self.table.c.result,
                self.table.c.job_id,
            )
        )
        async with self._db.begin() as conn:
            queued_tasks = await conn.execute(sql)
            queued_tasks = [r._asdict() for r in queued_tasks.all()]  # noqa
            await self._send_tasks(queued_tasks)
            await conn.commit()

    async def _restart_cron_tasks(self):
        """Reset all finished cron tasks to IDLE."""
        t = datetime.now(timezone.utc)
        _t = int(time())
        sql = (
            self.table.update()
            .where(
                sa.and_(
                    self.table.c.cron.isnot(None),
                    self.table.c.enabled.is_(True),
                    sa.or_(
                        self.table.c.status == TaskStatus.FINISHED.value,
                        sa.and_(
                            self.table.c.status == TaskStatus.FAILED.value,
                            self.table.c.max_retries <= self.table.c.retries,
                        ),
                    ),
                )
            )
            .values(
                {
                    'status': TaskStatus.IDLE.value,
                    'stage': 0,
                    'executor_id': None,
                    'retries': 0,
                    'wait_deadline': None,
                    'status_change': _t,
                    # 'result': [],
                    # 'exit_code': None,
                    # 'error': None,
                }
            )
            .returning(self.table.c.id, self.table.c.cron)
        )
        async with self._db.begin() as conn:
            cron_tasks = await conn.execute(sql)
            cron_tasks = [r._asdict() for r in cron_tasks.all()]  # noqa
            if cron_tasks:
                sql = (
                    self.table.update()
                    .where(self.table.c.id == sa.bindparam('_id'))
                    .values({'next_run': sa.bindparam('next_run'), 'job_id': sa.bindparam('job_id')})
                )
                cron_tasks = [
                    {
                        '_id': task['id'],
                        'next_run': int(croniter(task['cron'], t).next(datetime).timestamp()),
                        'job_id': get_short_uid(),
                    }
                    for task in cron_tasks
                ]
                sql.__len__ = lambda: 1  # TODO: alchemy compatibility ?
                await conn.execute(sql, cron_tasks)
            await conn.commit()

    async def _send_tasks(self, queued_tasks: list[Task]) -> None:
        """Send tasks to executor streams."""
        for task in queued_tasks:
            stage = task['stage']
            await self._stream.call(
                method='executor.run_task',
                headers={JSONRPCHeaders.CORRELATION_ID_HEADER: task['job_id']},
                params={
                    'data': ExecutorTask(
                        id=task['id'],
                        commands=task['commands'][stage:],
                        kws=task['kws'],
                        result=task['result'][:stage],
                        exec_deadline=task['exec_deadline'],
                        stage=stage,
                        stages=len(task['commands']),
                        job_id=task['job_id'],
                    )
                },
                app=task['app_name'],
                topic=self._executor_topic,
            )


class TaskExecutor(ContextableService, PublicInterface):
    """Task executor receives and processes tasks from a manager.

    Executor can be of different app than the manager. Executors do not require access to the tasks table or
    task / notification services but do require configured RPC stream to the manager. They also require an executor
    stream listener with exposed `TaskExecutor.run_task` method.
    """

    service_name = 'executor'
    manager_service_name = TaskManager.service_name

    def __init__(
        self,
        app,
        stream_client: StreamRPCClient = None,
        manager_app: str = None,
        manager_topic: str = Topic.MANAGER,
        rpc_service: JSONRPCServer = None,
        scheduler: Scheduler = None,
        data: dict = None,
        logger=None,
    ):
        """Initialize.

        :param app: web app
        :param manager_app: manager app name (by default: same as executor)
        :param manager_topic: manager topic name
        :param rpc_service: local rpc server name or instance
        :param scheduler: local scheduler
        :param stream_client: stream client to the manager
        :param data: additional data for command templates
        :param logger: optional logger instance
        """
        ContextableService.__init__(self, app=app, logger=logger)
        self.data = data if data else {}
        self._rpc = rpc_service
        self._scheduler = scheduler
        self._manager_app = manager_app if manager_topic else self.app.name
        self._manager_topic = manager_topic
        self._stream = stream_client
        self._task_ping = None
        self._closing = True

    @property
    def routes(self):
        return {'run_task': self.run_task}

    @property
    def permissions(self) -> dict:
        return {'*': self.PermissionKeys.GLOBAL_SYSTEM_PERMISSION}

    async def init(self):
        self._closing = False
        self._rpc = self.discover_service(self._rpc, cls=JSONRPCServer)
        self._stream = self.discover_service(self._stream, cls=StreamRPCClient)
        self._scheduler = self.discover_service(self._scheduler, cls=Scheduler)
        await self._send_ping()
        self._task_ping = self._scheduler.schedule_task(
            self._send_ping, interval=Limit.PING_INTERVAL.value, name=f'{self.service_name}._send_ping'
        )

    async def close(self):
        self._closing = True
        self._task_ping.enabled = False
        await self._suspend_self()

    @property
    def closed(self) -> bool:
        return self._closing

    async def run_task(self, data: ExecutorTask) -> None:
        """Run a task locally.

        `RPC method: executor.run_task`

        This method is used by the task manager to send tasks to executors and should be exposed
        as public in the executor RPC stream.

        An executor runs a task stage by stage in a local RPC server with `correlation_id` equals to the task `job_id`.
        An executor sends `execute_stage` message to the manager before each stage and `write_stage` with stage results
        after it's completed.

        The method returns nothing because all task data is sent in separate stream requests.

        :param data: task partial data
        """
        stage, deadline = data['stage'], data['exec_deadline']
        self.logger.info('Acquired task', task_id=data['id'], stage=stage, deadline=deadline)
        template_data = self._create_template_dict(data)
        for n, cmd in enumerate(data['commands']):
            if self._closing:
                break

            stage = data['stage'] + n
            self.logger.info(
                'Stage executed', task_id=data['id'], stage=stage, method=cmd['method'], deadline=data['exec_deadline']
            )
            if cmd['method'] == Message.method:
                return await self._wait_for_message(data, stage)
            elif cmd['method'] == Timer.method:
                return await self._wait_for_timer(data, stage, cmd['params']['timer'])

            await self._alert_on_stage_execution(data, stage)
            stage_timeout = cmd.get('max_timeout')
            headers = {
                JSONRPCHeaders.CORRELATION_ID_HEADER: data['job_id'],
            }
            if stage_timeout:
                stage_deadline = int(time() + stage_timeout)
                headers[JSONRPCHeaders.REQUEST_DEADLINE_HEADER] = min(stage_deadline, deadline)
            else:
                headers[JSONRPCHeaders.REQUEST_DEADLINE_HEADER] = deadline
            try:
                cmd = Template(cmd).fill(template_data)
                cond, execute = cmd.get('condition'), True
                if cond:
                    cond = Condition(Template(cond['schema']))
                    execute = cond(template_data)
                if execute:
                    _, result = await self._rpc.call(body=cmd, headers=headers, scope=Scope.SYSTEM)
                else:
                    self.logger.info('Stage condition failed', task_id=data['id'], stage=stage, method=cmd['method'])
                    _, result = None, None
            except Exception as exc:
                error = result = RPCError(
                    id=None, error=InternalError(base_exc=exc, message='Template evaluation error')
                )
            else:
                error, result = self._parse_result(result)

            if error:
                self.logger.error(
                    'Stage failed', task_id=data['id'], stage=stage, method=cmd['method'], error=error['error']
                )
                await self._write_stage_result(data, stage, error=True, result=result)
                return

            self.logger.info('Stage finished', task_id=data['id'], stage=stage, method=cmd['method'])
            template_data[str(stage)] = result
            await self._write_stage_result(data, stage, error=False, result=result)

    def _create_template_dict(self, data: ExecutorTask) -> dict:
        env = {str(stage): data['result'][stage] for stage in range(data['stage'])}
        env.update({'id': data['id'], 'kws': data['kws'], 'executor': self.data})
        return env

    @staticmethod
    def _parse_result(result) -> tuple:
        """Get error flag and result from rpc server response."""
        if result is None:
            return False, None
        elif isinstance(result, list):
            _result = []
            for r in result:
                if 'error' in r:
                    result.append(r)
                else:
                    result.append(r['result'])
            return False, _result
        elif 'error' in result:
            return result, result
        else:
            return False, result['result']

    async def _call_manager(self, method: str, params: dict, job_id: str | None) -> None:
        """Call the manager stream."""
        headers = {}
        if job_id:
            headers[JSONRPCHeaders.CORRELATION_ID_HEADER] = job_id
        await retry(
            self._stream.call,
            kws=dict(
                headers=headers,
                method=f'{self.manager_service_name}.{method}',
                params=params,
                app=self._manager_app,
                topic=self._manager_topic,
            ),
            retries=5,
            retry_timeout=1,
            logger=self.logger,
        )

    async def _wait_for_timer(self, data: ExecutorTask, stage: int, timer: int) -> None:
        """Wait for a timer."""
        t = int(time())
        params = {
            'task_id': data['id'],
            'executor_id': self.app.id,
            'stage': stage,
            'timer': timer,
            'timestamp': t,
        }
        await self._call_manager('wait_for_timer', params, data['job_id'])

    async def _wait_for_message(self, data: ExecutorTask, stage: int) -> None:
        """Wait until the task receives a callback message."""
        t = int(time())
        params = {'task_id': data['id'], 'executor_id': self.app.id, 'stage': stage, 'timestamp': t}
        await self._call_manager('wait_for_message', params, data['job_id'])

    async def _alert_on_stage_execution(self, data: ExecutorTask, stage: int) -> None:
        """Alert the manager on task execution."""
        t = int(time())
        params = {'task_id': data['id'], 'executor_id': self.app.id, 'stage': stage, 'timestamp': t}
        await self._call_manager('execute_stage', params, data['job_id'])

    async def _write_stage_result(self, data: ExecutorTask, stage: int, error: bool, result) -> None:
        """Send task stage results to the manager."""
        t = int(time())
        params = {
            'task_id': data['id'],
            'executor_id': self.app.id,
            'stage': stage,
            'stages': data['stages'],
            'result': result,
            'error': error,
            'timestamp': t,
        }
        await self._call_manager('write_stage', params, data['job_id'])

    async def _send_ping(self) -> None:
        """Send a health report message to the manager."""
        if not self._closing:
            await self._call_manager('ping', {'executor_id': self.app.id}, None)

    async def _suspend_self(self) -> None:
        """Send an executor suspend message to the manager."""
        await self._call_manager('suspend_executor', {'executor_id': self.app.id}, None)


SERVICE_CLASS_REGISTRY.register(TaskService)
SERVICE_CLASS_REGISTRY.register(NotificationService)
SERVICE_CLASS_REGISTRY.register(TaskManager)
SERVICE_CLASS_REGISTRY.register(TaskExecutor)
