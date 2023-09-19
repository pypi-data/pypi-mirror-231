import logging
import sys
from pathlib import Path
from typing import Dict, Optional

import anyio
import typer

from faststream.__about__ import __version__
from faststream.cli.docs.app import docs_app
from faststream.cli.utils.imports import get_app_path, try_import_app
from faststream.cli.utils.logs import LogLevels, get_log_level, set_log_level
from faststream.cli.utils.parser import parse_cli_args
from faststream.log import logger
from faststream.types import SettingField

cli = typer.Typer(pretty_exceptions_short=True)
cli.add_typer(docs_app, name="docs", help="AsyncAPI schema commands")


def version_callback(version: bool) -> None:
    """Callback function for displaying version information.

    Args:
        version: If True, display version information

    Returns:
        None
    !!! note

        The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
    """
    if version is True:
        import platform

        typer.echo(
            "Running FastStream %s with %s %s on %s"
            % (
                __version__,
                platform.python_implementation(),
                platform.python_version(),
                platform.system(),
            )
        )

        raise typer.Exit()


@cli.callback()
def main(
    version: Optional[bool] = typer.Option(
        False,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Show current platform, python and FastStream version",
    )
) -> None:
    """
    Generate, run and manage FastStream apps to greater development experience
    """


@cli.command(
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
def run(
    ctx: typer.Context,
    app: str = typer.Argument(
        ...,
        help="[python_module:FastStream] - path to your application",
    ),
    workers: int = typer.Option(
        1,
        show_default=False,
        help="Run [workers] applications with process spawning",
    ),
    log_level: LogLevels = typer.Option(
        LogLevels.info,
        case_sensitive=False,
        show_default=False,
        help="[INFO] default",
    ),
    reload: bool = typer.Option(
        False,
        "--reload",
        is_flag=True,
        help="Restart app at directory files changes",
    ),
    app_dir: str = typer.Option(
        ".",
        "--app-dir",
        help=(
            "Look for APP in the specified directory, by adding this to the PYTHONPATH."
            " Defaults to the current working directory."
        ),
    ),
) -> None:
    """Run [MODULE:APP] FastStream application"""
    app, extra = parse_cli_args(app, *ctx.args)
    casted_log_level = get_log_level(log_level)

    module, app = get_app_path(app)

    if app_dir:
        sys.path.insert(0, app_dir)

    args = (module, app, extra, casted_log_level)

    if reload and workers > 1:
        raise ValueError("You can't use reload option with multiprocessing")

    if reload is True:
        from faststream.cli.supervisors.watchfiles import WatchReloader

        WatchReloader(target=_run, args=args, reload_dirs=(str(module.parent),)).run()

    elif workers > 1:
        from faststream.cli.supervisors.multiprocess import Multiprocess

        Multiprocess(target=_run, args=(*args, logging.DEBUG), workers=workers).run()

    else:
        _run(module=module, app=app, extra_options=extra, log_level=casted_log_level)


def _run(
    module: Path,
    app: str,
    extra_options: Dict[str, SettingField],
    log_level: int = logging.INFO,
    app_level: int = logging.INFO,
) -> None:
    """Runs the specified application.

    Args:
        module: Path to the module containing the application.
        app: Name of the application to run.
        extra_options: Additional options for the application.
        log_level: Log level for the application (default: logging.INFO).
        app_level: Log level for the application (default: logging.INFO).

    Returns:
        None

    Raises:
        ImportError: If `uvloop` is not installed.

    Note:
        This function uses the `anyio.run()` function to run the application.
    !!! note

        The above docstring is autogenerated by docstring-gen library (https://docstring-gen.airt.ai)
    """
    app_obj = try_import_app(module, app)
    set_log_level(log_level, app_obj)

    if sys.platform not in ("win32", "cygwin", "cli"):  # pragma: no cover
        try:
            import uvloop
        except ImportError:
            logger.warning("You have no installed `uvloop`")
        else:
            uvloop.install()

    anyio.run(
        app_obj.run,
        app_level,
        extra_options,
    )
