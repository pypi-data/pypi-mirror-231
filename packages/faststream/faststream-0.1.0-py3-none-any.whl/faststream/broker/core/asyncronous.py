import logging
from abc import abstractmethod
from functools import wraps
from types import TracebackType
from typing import (
    Any,
    Awaitable,
    Callable,
    Dict,
    Mapping,
    Optional,
    Sequence,
    Sized,
    Tuple,
    Type,
    Union,
    cast,
)

import anyio
from fast_depends.core import CallModel
from fast_depends.dependencies import Depends

from faststream._compat import Self, override
from faststream.broker.core.abc import BrokerUsecase
from faststream.broker.handler import AsyncHandler
from faststream.broker.message import StreamMessage
from faststream.broker.middlewares import BaseMiddleware
from faststream.broker.push_back_watcher import BaseWatcher
from faststream.broker.types import (
    AsyncCustomDecoder,
    AsyncCustomParser,
    ConnectionType,
    CustomDecoder,
    CustomParser,
    Filter,
    MsgType,
    P_HandlerParams,
    T_HandlerReturn,
    WrappedReturn,
)
from faststream.broker.wrapper import HandlerCallWrapper
from faststream.exceptions import AckMessage, NackMessage, RejectMessage, SkipMessage
from faststream.log import access_logger
from faststream.types import SendableMessage
from faststream.utils import context
from faststream.utils.functions import to_async


async def default_filter(msg: StreamMessage[Any]) -> bool:
    """A function to filter stream messages.

    Args:
        msg : A stream message object

    Returns:
        True if the message has not been processed, False otherwise
    !!! note

        The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
    """
    return not msg.processed


class BrokerAsyncUsecase(BrokerUsecase[MsgType, ConnectionType]):
    """A class representing a broker async usecase.

    Attributes:
        handlers : A dictionary of handlers for different message types.
        middlewares : A sequence of middleware functions.
        _global_parser : An optional global parser for messages.
        _global_decoder : An optional global decoder for messages.

    Methods:
        start() : Abstract method to start the broker async usecase.
        _connect(**kwargs: Any) : Abstract method to connect to the broker.
        _close(exc_type: Optional[Type[BaseException]] = None, exc_val: Optional[BaseException] = None, exec_tb: Optional[TracebackType] = None) : Abstract method to close the connection to the broker.
        close(exc_type: Optional[Type[BaseException]] = None, exc_val: Optional[BaseException] = None, exec_tb: Optional[TracebackType] = None) : Close the connection to the broker.
        _process_message(func: Callable[[StreamMessage[MsgType]], Awaitable[T_HandlerReturn]], watcher: BaseWatcher) : Abstract method to process a message.
        publish(message: SendableMessage, *args: Any, reply_to: str = "", rpc: bool = False, rpc_timeout: Optional[float]
    !!! note

        The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
    """

    handlers: Dict[Any, AsyncHandler[MsgType]]  # type: ignore[assignment]
    middlewares: Sequence[Callable[[MsgType], BaseMiddleware]]
    _global_parser: Optional[AsyncCustomParser[MsgType]]
    _global_decoder: Optional[AsyncCustomDecoder[MsgType]]

    @abstractmethod
    async def start(self) -> None:
        super()._abc_start()
        for h in self.handlers.values():
            for c, _, _, _, _, _ in h.calls:
                c.event = anyio.Event()
        await self.connect()

    @abstractmethod
    async def _connect(self, **kwargs: Any) -> ConnectionType:
        """Connect to a resource.

        Args:
            **kwargs: Additional keyword arguments for the connection.

        Returns:
            The connection object.

        Raises:
            NotImplementedError: If the method is not implemented.
        !!! note

            The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
        """
        raise NotImplementedError()

    @abstractmethod
    async def _close(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_val: Optional[BaseException] = None,
        exec_tb: Optional[TracebackType] = None,
    ) -> None:
        """Close the object.

        Args:
            exc_type: Optional. The type of the exception.
            exc_val: Optional. The exception value.
            exec_tb: Optional. The traceback of the exception.

        Returns:
            None
        !!! note

            The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
        """
        super()._abc__close(exc_type, exc_val, exec_tb)

    async def close(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_val: Optional[BaseException] = None,
        exec_tb: Optional[TracebackType] = None,
    ) -> None:
        """Closes the object.

        Args:
            exc_type: The type of the exception being handled, if any.
            exc_val: The exception instance being handled, if any.
            exec_tb: The traceback of the exception being handled, if any.

        Returns:
            None

        Raises:
            NotImplementedError: If the method is not implemented.
        !!! note

            The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
        """
        super()._abc_close(exc_type, exc_val, exec_tb)

        for h in self.handlers.values():
            await h.close()

        if self._connection is not None:
            await self._close(exc_type, exc_val, exec_tb)

    @override
    @abstractmethod
    def _process_message(
        self,
        func: Callable[[StreamMessage[MsgType]], Awaitable[T_HandlerReturn]],
        watcher: BaseWatcher,
    ) -> Callable[[StreamMessage[MsgType]], Awaitable[WrappedReturn[T_HandlerReturn]],]:
        """Process a message.

        Args:
            func: A callable function that takes a StreamMessage and returns an Awaitable
            watcher: An instance of BaseWatcher

        Returns:
            A callable function that takes a StreamMessage and returns an Awaitable

        Raises:
            NotImplementedError: If the method is not implemented
        !!! note

            The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
        """
        raise NotImplementedError()

    @abstractmethod
    async def publish(
        self,
        message: SendableMessage,
        *args: Any,
        reply_to: str = "",
        rpc: bool = False,
        rpc_timeout: Optional[float] = None,
        raise_timeout: bool = False,
        **kwargs: Any,
    ) -> Optional[SendableMessage]:
        """Publish a message.

        Args:
            message: The message to be published.
            *args: Additional arguments.
            reply_to: The reply-to address for the message.
            rpc: Whether the message is for RPC.
            rpc_timeout: The timeout for RPC.
            raise_timeout: Whether to raise an exception on timeout.
            **kwargs: Additional keyword arguments.

        Returns:
            The published message.

        Raises:
            NotImplementedError: If the method is not implemented.
        !!! note

            The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
        """
        raise NotImplementedError()

    @override
    @abstractmethod
    def subscriber(  # type: ignore[override,return]
        self,
        *broker_args: Any,
        retry: Union[bool, int] = False,
        dependencies: Sequence[Depends] = (),
        decoder: Optional[CustomDecoder[MsgType]] = None,
        parser: Optional[CustomParser[MsgType]] = None,
        middlewares: Optional[Sequence[Callable[[MsgType], BaseMiddleware]]] = None,
        filter: Filter[StreamMessage[MsgType]] = default_filter,
        _raw: bool = False,
        _get_dependant: Optional[Any] = None,
        **broker_kwargs: Any,
    ) -> Callable[
        [
            Union[
                Callable[P_HandlerParams, T_HandlerReturn],
                HandlerCallWrapper[MsgType, P_HandlerParams, T_HandlerReturn],
            ]
        ],
        HandlerCallWrapper[MsgType, P_HandlerParams, T_HandlerReturn],
    ]:
        """A function decorator for subscribing to a message broker.

        Args:
            *broker_args: Positional arguments to be passed to the message broker.
            retry: Whether to retry the subscription if it fails. Can be a boolean or an integer specifying the number of retries.
            dependencies: Sequence of dependencies to be injected into the decorated function.
            decoder: Custom decoder function for decoding the message.
            parser: Custom parser function for parsing the decoded message.
            middlewares: Sequence of middleware functions to be applied to the message.
            filter: Filter function for filtering the messages to be processed.
            _raw: Whether to return the raw message instead of the processed result.
            _get_dependant: Optional argument to get the dependant object.

        Returns:
            A callable decorator that wraps the decorated function and handles the subscription.

        Raises:
            NotImplementedError: If silent animals are not supported.
        !!! note

            The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
        """
        super().subscriber()

    def __init__(
        self,
        *args: Any,
        apply_types: bool = True,
        logger: Optional[logging.Logger] = access_logger,
        log_level: int = logging.INFO,
        log_fmt: Optional[str] = "%(asctime)s %(levelname)s - %(message)s",
        dependencies: Sequence[Depends] = (),
        decoder: Optional[CustomDecoder[MsgType]] = None,
        parser: Optional[CustomParser[MsgType]] = None,
        middlewares: Optional[Sequence[Callable[[MsgType], BaseMiddleware]]] = None,
        **kwargs: Any,
    ) -> None:
        """Initialize the class.

        Args:
            *args: Variable length arguments
            apply_types: Whether to apply types or not
            logger: Logger object for logging
            log_level: Log level for logging
            log_fmt: Log format for logging
            dependencies: Sequence of dependencies
            decoder: Custom decoder object
            parser: Custom parser object
            middlewares: Sequence of middlewares
            **kwargs: Keyword arguments
        !!! note

            The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
        """
        super().__init__(
            *args,
            apply_types=apply_types,
            logger=logger,
            log_level=log_level,
            log_fmt=log_fmt,
            dependencies=dependencies,
            decoder=cast(
                Optional[AsyncCustomDecoder[MsgType]],
                to_async(decoder) if decoder else None,
            ),
            parser=cast(
                Optional[AsyncCustomParser[MsgType]],
                to_async(parser) if parser else None,
            ),
            middlewares=middlewares,
            **kwargs,
        )

    async def connect(self, *args: Any, **kwargs: Any) -> ConnectionType:
        """Connect to a remote server.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            The connection object.
        !!! note

            The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
        """
        if self._connection is None:
            _kwargs = self._resolve_connection_kwargs(*args, **kwargs)
            self._connection = await self._connect(**_kwargs)
        return self._connection

    async def __aenter__(self) -> Self:
        await self.connect()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exec_tb: Optional[TracebackType],
    ) -> None:
        """Exit the context manager.

        Args:
            exc_type: The type of the exception raised, if any.
            exc_val: The exception raised, if any.
            exec_tb: The traceback of the exception raised, if any.

        Returns:
            None

        Overrides:
            This method overrides the __aexit__ method of the base class.
        !!! note

            The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
        """
        await self.close(exc_type, exc_val, exec_tb)

    @override
    def _wrap_decode_message(
        self,
        func: Callable[..., Awaitable[T_HandlerReturn]],
        params: Sized = (),
        _raw: bool = False,
    ) -> Callable[[StreamMessage[MsgType]], Awaitable[T_HandlerReturn]]:
        """Wraps a function to decode a message and pass it as an argument to the wrapped function.

        Args:
            func: The function to be wrapped.
            params: The parameters to be passed to the wrapped function.
            _raw: Whether to return the raw message or not.

        Returns:
            The wrapped function.

        Raises:
            AssertionError: If the code reaches an unreachable state.
        !!! note

            The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
        """
        params_ln = len(params)

        @wraps(func)
        async def decode_wrapper(message: StreamMessage[MsgType]) -> T_HandlerReturn:
            """A wrapper function to decode and handle a message.

            Args:
                message : The message to be decoded and handled

            Returns:
                The return value of the handler function

            Raises:
                AssertionError: If the code reaches an unreachable state
            !!! note

                The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
            """
            if _raw is True:
                return await func(message)

            msg = message.decoded_body
            if params_ln > 1:
                if isinstance(msg, Mapping):
                    return await func(**msg)
                elif isinstance(msg, Sequence):
                    return await func(*msg)
            else:
                return await func(msg)

            raise AssertionError("unreachable")

        return decode_wrapper

    @override
    def _wrap_handler(
        self,
        func: Callable[P_HandlerParams, T_HandlerReturn],
        *,
        retry: Union[bool, int] = False,
        extra_dependencies: Sequence[Depends] = (),
        _raw: bool = False,
        _get_dependant: Optional[Any] = None,
        **broker_log_context_kwargs: Any,
    ) -> Tuple[
        HandlerCallWrapper[MsgType, P_HandlerParams, T_HandlerReturn],
        CallModel[P_HandlerParams, T_HandlerReturn],
    ]:
        """Wrap a handler function.

        Args:
            func: The handler function to wrap.
            retry: Whether to retry the handler function if it fails. Can be a boolean or an integer specifying the number of retries.
            extra_dependencies: Additional dependencies to inject into the handler function.
            _raw: Whether to return the raw response from the handler function.
            _get_dependant: An optional object to use as the dependant for the handler function.
            **broker_log_context_kwargs: Additional keyword arguments to pass to the broker log context.

        Returns:
            A tuple containing the wrapped handler function and the call model.
        !!! note

            The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
        """
        return super()._wrap_handler(  # type: ignore[return-value]
            func,
            retry=retry,
            extra_dependencies=extra_dependencies,
            _raw=_raw,
            _get_dependant=_get_dependant,
            **broker_log_context_kwargs,
        )

    async def _execute_handler(
        self,
        func: Callable[[StreamMessage[MsgType]], Awaitable[T_HandlerReturn]],
        message: StreamMessage[MsgType],
    ) -> T_HandlerReturn:
        """Executes a handler function asynchronously.

        Args:
            func: The handler function to be executed.
            message: The message to be passed to the handler function.

        Returns:
            The return value of the handler function.

        Raises:
            AckMessage: If the handler function raises an AckMessage exception.
            NackMessage: If the handler function raises a NackMessage exception.
            RejectMessage: If the handler function raises a RejectMessage exception.
        !!! note

            The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
        """
        try:
            return await func(message)
        except AckMessage as e:
            await message.ack()
            raise e
        except NackMessage as e:
            await message.nack()
            raise e
        except RejectMessage as e:
            await message.reject()
            raise e

    @override
    def _log_execution(
        self,
        func: Callable[
            [StreamMessage[MsgType]],
            Awaitable[WrappedReturn[T_HandlerReturn]],
        ],
        **broker_args: Any,
    ) -> Callable[[StreamMessage[MsgType]], Awaitable[WrappedReturn[T_HandlerReturn]]]:
        """Decorator to log the execution of a function.

        Args:
            func: The function to be decorated.

        Returns:
            The decorated function.

        Raises:
            SkipMessage: If the message should be skipped.

        Note:
            This decorator logs the execution of the function, including the received message and any exceptions that occur during execution.
        !!! note

            The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
        """

        @wraps(func)
        async def log_wrapper(
            message: StreamMessage[MsgType],
        ) -> WrappedReturn[T_HandlerReturn]:
            """A wrapper function for logging.

            Args:
                message : The message to be logged.

            Returns:
                The wrapped return value.

            Raises:
                SkipMessage: If the message is to be skipped.
                Exception: If an exception occurs during processing.
            !!! note

                The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
            """
            log_context = self._get_log_context(message=message, **broker_args)

            with context.scope("log_context", log_context):
                self._log("Received", extra=log_context)

                try:
                    r = await func(message)
                except SkipMessage as e:
                    self._log("Skipped", extra=log_context)
                    raise e
                except Exception as e:
                    self._log(f"{type(e).__name__}: {e}", logging.ERROR, exc_info=e)
                    raise e
                else:
                    self._log("Processed", extra=log_context)
                    return r

        return log_wrapper
