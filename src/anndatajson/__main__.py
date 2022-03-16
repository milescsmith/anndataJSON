from pathlib import Path

import anndata as ad
import typer

from . import app
from . import console
from . import version_callback
from .exporting import to_json


@app.command(name="to_json")
def main(
    adata: Path = typer.Argument(
        ..., help="AnnData object (stored as an .h5ad) to convert to JSON"
    ),
    output: Path = typer.Argument(..., help="Location to save JSON file"),
    overwrite: bool = typer.Option(
        True, "-o", "--overwrite", help="Overwrite an existing file"
    ),
    compress: bool = typer.Option(True, "-c", "--compress", help="Compress JSON file"),
    version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the plinkliftover package.",
    ),
) -> None:

    if not adata.exists():
        raise FileExistsError(f"Cannot find the file {adata.name} in {adata.parent}")
    else:
        adata = ad.read(adata)

    adata.to_json(
        outfile=output,
        overwrite=overwrite,
        compress=compress,
    )


if __name__ == "__main__":
    typer.run(app)
