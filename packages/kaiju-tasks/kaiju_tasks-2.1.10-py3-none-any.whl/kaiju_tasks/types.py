"""Data types."""
import abc
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import ClassVar, TypedDict
from uuid import UUID

from kaiju_tools.encoding import Serializable
from kaiju_tools.registry import ClassRegistry
from kaiju_tools.rpc import RPCRequest
from kaiju_tools.templates import Condition as Condition


__all__ = [
    'TaskStatus',
    'RestartPolicy',
    'Limit',
    'TaskCommand',
    'Task',
    'Notification',
    'ExecutorTask',
    'ExitCode',
    'Message',
    'Timer',
    'SPECIAL_COMMANDS',
]


class TaskCommand(TypedDict, total=False):
    """Task command.

    It's just a typed dict providing an interfaces for task command format.

    .. code-block:: python

        Task(commands=[
            TaskCommand(method='do.something', params={'value': True})
        ])

    """

    method: str  #: method name as in RPC request
    params: dict | None  #: params as in RPC request
    max_timeout: int | None  #: optional command execution timeout in seconds
    condition: Condition | dict  #: optional command exec condition (must be True to execute)


class _SpecialCommand(Serializable, abc.ABC):
    """Special instructions for a task executor (base class)."""

    method: ClassVar[str]  #: command name is required

    @abc.abstractmethod
    def repr(self) -> TaskCommand:
        """Get a task command dict."""


@dataclass(slots=True)
class Message(_SpecialCommand):
    """Message hook.

    A task must wait until a message is received for this task to continue.

    .. code-block:: python

        Task(commands=[
            TaskCommand(method='do.first'),
            Message(),
            TaskCommand(method='do.second')
        ])

    Upon this stage the task will be put in :py:attr:`TaskStatus.WAITING` and the executor will drop the task.
    The manager will wait until the task service has received a message for this particular task. The message will
    be saved in the stage results (stage "1" in the example) and the task will continue.

    This command allows you to arbitrarily send data to a running task, for example to create tasks which depend on
    user input / external systems.
    """

    method = '_MESSAGE_'

    max_timeout: int | None = None
    """Currently not used."""

    def repr(self) -> TaskCommand:
        return TaskCommand(method=self.method, params=None, max_timeout=self.max_timeout)


@dataclass(slots=True)
class Timer(_SpecialCommand):
    """Timer hook.

    The task must wait for a timer to continue.

    Use in your task chain of commands:

    .. code-block:: python

        Task(commands=[
            TaskCommand(method='do.first'),
            Timer(60),
            TaskCommand(method='do.second')
        ])

    Upon this stage the task will be put in :py:attr:`TaskStatus.WAITING` and the executor will drop the task. Once
    the timer is reached the manager will continue the task execution.

    Basically the process is similar to suspended tasks but with a wait timeout between stages.

    Timer always writes None into its stage results.
    """

    method = '_TIMER_'

    timer: int
    """Wait time in seconds."""

    def repr(self) -> TaskCommand:
        return TaskCommand(method=self.method, params={'timer': self.timer})


class _SpecialCommandsRegistry(ClassRegistry[str, _SpecialCommand]):
    """Registry for special task commands."""

    @classmethod
    def get_base_classes(cls) -> tuple[type, ...]:
        return (_SpecialCommand,)

    def get_key(self, obj: _SpecialCommand) -> str:
        return obj.method


SPECIAL_COMMANDS = _SpecialCommandsRegistry()
SPECIAL_COMMANDS.register_from_namespace(locals())


class Limit(Enum):
    """Global task limits and parameters."""

    MAX_STAGES = 100
    """Max allowed number of commands inside of a `Task.commands` block."""

    MAX_RETRIES = 10
    """Max allowed number of task restarts set by `Task.max_retries`."""

    MIN_T = 10
    """Minimum allowed task timeout value in seconds set by `Task.max_exec_timeout`."""

    DEFAULT_T = 300
    """Default task timeout value in seconds set by `Task.max_exec_timeout`."""

    MAX_T = 3600 * 4
    """Maximum allowed task timeout value in seconds set by `Task.max_exec_timeout`."""

    PING_INTERVAL = 30
    """Executor ping interval in seconds. Each executor sends signals to the manager according to this interval.
    If an executor misses several consequent pings, the manager will suspend its tasks and remove the executor from
    the list of registered executors."""

    SUSPEND_AFTER_PINGS = 3
    """Number of pings for an executor to miss to be suspended by the manager."""


class TaskStatus(Enum):
    """Task status types."""

    IDLE = 'IDLE'
    """Initial state. All newly created, reset tasks and restarted cron tasks become `IDLE` until they are queued
    by the manager."""

    QUEUED = 'QUEUED'
    """Task is queued for execution by the manager. This status means that the task has been put to the queue
    (executor stream) but not yet has been acquired."""

    EXECUTED = 'EXECUTED'
    """Task has been acquired by an executor and is being executed."""

    SUSPENDED = 'SUSPENDED'
    """Executor running this task has been suspended due to an exit signal or because it missed several ping requests.
    Suspended tasks are `QUEUED` by the manager in the next cycle.
    """

    WAITING = 'WAITING'
    """Task has encountered a :py:class:`~kaiju_tasks.types.Timer` or :py:class:`~kaiju_tasks.types.Message`
    special command and has been put on hold by the manager. Executor has dropped the task and it will not continue
    until the wait condition (either a timer or an external message)
    has been satisfied. Manager will put waiting tasks back to `QUEUED` once the condition is met.
    """

    FINISHED = 'FINISHED'
    """Task has finished successfully and the result is available in `Task.result`."""

    FAILED = 'FAILED'
    """Task has finished with an error, the error is available in `Task.error`."""


class ExitCode(Enum):
    """Task execution unix style exit codes."""

    SUCCESS = 0
    """Task is completed."""

    EXECUTION_ERROR = 1
    """One of the task commands has failed."""

    ABORTED = 130
    """Task has been aborted by the manager due to timeout or other reason."""


class RestartPolicy(Enum):
    """Task restart policy types.

    This setting can be set in `Task.restart_policy` to tell the manager which stage you want task to be restarted from
    in case of an error. Note that this setting is useless when `Task.max_retries` is not set.
    """

    CURRENT = 'CURRENT'
    """Restart from the current (i.e. first failed) stage. Results from the previous stages will be preserved."""

    FIRST = 'FIRST'
    """Clear all results and restart fresh from the first stage."""


class Task(TypedDict, total=False):
    """Task object.

    This is a typed dict which provides hints for task data.
    """

    id: str  #: generated / user-defined unique identifier

    # executor instructions

    app_name: str  #: executor type (app.name)
    commands: list[TaskCommand | RPCRequest]  #: sequential list of commands
    kws: dict  #: additional kws template arguments

    # manager instructions

    enabled: bool  #: inactive tasks are not processed
    cron: str  #: cron instructions for periodic tasks
    max_exec_timeout: int  #: (s) max allowed execution time in total
    max_retries: int  #: max retries for a failed task (0 for no retries)
    restart_policy: str  #: how the task will be restarted on failure, see :py:class:`~kaiju_tasks.types.RestartPolicy`
    notify: bool  #: notify user about status changes
    next_task: str | None  #: next task to run after finishing of this one
    system: bool  #: system task (should never be removed by cleaning jobs)

    # meta

    description: str | None  #: task long description, completely optional
    meta: dict  #: task metadata, unused by the services

    # managed params

    status: str  #: current task status, see :py:class:`~kaiju_tasks.types.TaskStatus`
    result: list  #: task execution result, a list of stage returns
    stage: int  #: current stage (command) being executed
    stages: int  #: number of commands in this task
    queued_at: int | None  #: UNIX time last queued
    exec_deadline: int | None  #: UNIX time deadline
    wait_deadline: int | None  #: UNIX time deadline for a timer command (see :py:class:`~kaiju_tasks.types.Timer`)
    next_run: int | None  #: UNIX time for next run
    status_change: int | None  #: last change of status
    user_id: UUID | None  #: user created the task
    executor_id: UUID | None  #: which executor has this task
    job_id: str | None  #: updated for each new run
    retries: int  #: current number of retries
    created: datetime  #: when task record was added to the table
    exit_code: int | None  #: exit (error) code similar to UNIX codes (see :py:class:`~kaiju_tasks.types.ExitCode`)
    error: dict | None  #: error.repr() if there's an error


class ExecutorTask(TypedDict):
    """Task data provided to an executor by the manager."""

    id: str  #: task id
    commands: list[TaskCommand | RPCRequest]  #: sequential list of commands
    kws: dict  #: additional template arguments
    result: list  #: task execution result, a list of stage returns
    stage: int  #: current stage being executed (or about to execute)
    stages: int  #: total number of stages
    exec_deadline: int  #: UNIX time deadline
    job_id: str  #: current job id for this task


class Notification(TypedDict, total=False):
    """Notification object.

    This is a typed dict which provides hints for task notifications data.
    """

    id: UUID  #: generated
    message: str | None  #: human-readable message or tag
    kws: dict | None  #: format keywords
    created: datetime  #: timestamp
    enabled: bool  #: mark as read
    user_id: UUID | None  #: receiver
    task_id: str | None  #: task id
    job_id: str | None  #: job id
    status: str | None  #: task job status
    result: list | None  #: job results
    exit_code: int | None  #: unix style exit code (see :py:class:`~kaiju_tasks.types.ExitCode`)
    error: dict | None  #: error.repr() if the task has failed
