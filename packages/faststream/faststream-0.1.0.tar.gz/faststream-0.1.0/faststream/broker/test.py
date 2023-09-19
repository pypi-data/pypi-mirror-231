from types import TracebackType
from typing import Any, Callable, ContextManager, Dict, Optional, Type

import anyio
from anyio import CancelScope
from anyio.abc._tasks import TaskGroup

from faststream.app import FastStream
from faststream.broker.core.abc import BrokerUsecase
from faststream.broker.handler import AsyncHandler
from faststream.types import SendableMessage, SettingField


class TestApp:
    # make sure pytest doesn't try to collect this class as a test class
    """A class to represent a test application.

    Attributes:
        app : an instance of FastStream
        _extra_options : optional dictionary of additional options
        _event : an instance of anyio.Event
        _task : an instance of TaskGroup

    Methods:
        __init__ : initializes the TestApp object
        __aenter__ : enters the asynchronous context and starts the FastStream application
        __aexit__ : exits the asynchronous context and stops the FastStream application
    !!! note

        The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
    """
    __test__ = False
    app: FastStream
    _extra_options: Optional[Dict[str, SettingField]]
    _event: anyio.Event
    _task: TaskGroup

    def __init__(
        self,
        app: FastStream,
        run_extra_options: Optional[Dict[str, SettingField]] = None,
    ) -> None:
        """Initialize a class instance.

        Args:
            app: An instance of the FastStream class.
            run_extra_options: Optional dictionary of extra options for running the application.

        Returns:
            None
        !!! note

            The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
        """
        self.app = app
        self._extra_options = run_extra_options

    async def __aenter__(self) -> FastStream:
        self.app._stop_event = self._event = anyio.Event()
        await self.app._start(run_extra_options=self._extra_options)
        self._task = tg = anyio.create_task_group()
        await tg.__aenter__()
        tg.start_soon(self.app._stop)
        return self.app

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_val: Optional[BaseException] = None,
        exec_tb: Optional[TracebackType] = None,
    ) -> None:
        """Exit the asynchronous context manager.

        Args:
            exc_type: The type of the exception raised, if any.
            exc_val: The exception instance raised, if any.
            exec_tb: The traceback for the exception raised, if any.

        Returns:
            None
        !!! note

            The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
        """
        self._event.set()
        await self._task.__aexit__(exc_type, exc_val, exec_tb)


def patch_broker_calls(broker: BrokerUsecase[Any, Any]) -> None:
    """Patch broker calls.

    Args:
        broker: The broker to patch.

    Returns:
        None.
    !!! note

        The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
    """
    for handler in broker.handlers.values():
        for f, _, _, _, _, _ in handler.calls:
            f.event = anyio.Event()
        handler.set_test()


async def call_handler(
    handler: AsyncHandler[Any],
    message: Any,
    rpc: bool = False,
    rpc_timeout: Optional[float] = 30.0,
    raise_timeout: bool = False,
) -> Optional[SendableMessage]:
    """Asynchronously call a handler function.

    Args:
        handler: The handler function to be called.
        message: The message to be passed to the handler function.
        rpc: Whether the call is a remote procedure call (RPC).
        rpc_timeout: The timeout for the RPC, in seconds.
        raise_timeout: Whether to raise a timeout error if the RPC times out.

    Returns:
        The result of the handler function if `rpc` is True, otherwise None.

    Raises:
        TimeoutError: If the RPC times out and `raise_timeout` is True.
    !!! note

        The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
    """
    scope: Callable[[Optional[float]], ContextManager[CancelScope]]
    if raise_timeout:
        scope = anyio.fail_after
    else:
        scope = anyio.move_on_after

    with scope(rpc_timeout):
        result = await handler.consume(message)

        if rpc is True:
            return result

    return None
