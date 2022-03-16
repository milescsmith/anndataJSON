# src/anndataJSON/__init__.py
"""anndataJSON."""

from importlib.metadata import metadata
from importlib.metadata import version

import typer
from rich.console import Console
from rich.traceback import install

from .exporting import to_json


install(show_locals=True)

try:
    __author__ = metadata(__name__)["Author"]
except KeyError:
    __author__ = "unknown"

try:
    __email__ = metadata(__name__)["Author-email"]
except KeyError:  # pragma: no cover
    __email__ = "unknown"

try:
    __version__ = version(__name__)
except KeyError:  # pragma: no cover
    __version__ = "unknown"


__all__ = ["to_json"]


console = Console()


def version_callback(value: bool):
    """Prints the version of the package."""
    if value:
        console.print(f"[yellow]plinkliftover[/] version: [bold blue]{__version__}[/]")
        raise typer.Exit()


app = typer.Typer(
    name="anndataJSON",
    help="Serializes an anndata object to JSON representation",
    add_completion=False,
)
