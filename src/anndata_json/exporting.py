from gzip import open as gzopen
from pathlib import Path
from typing import Union, Optional

import pandas as pd
from anndata import AnnData
from orjson import dumps
from typeguard import typechecked

from .utils import add_method


# TODO: add gzipping on save, provided it isn't difficult to read
# a gzipped JSON file in R
@add_method(AnnData)
@typechecked
def to_json(
    self,
    outfile: Optional[Union[Path, str]] = None,
    overwrite=True,
    compress: bool = True,
) -> None:
    """Save an Anndata object to disk in JSON format

    Parameters
    ----------
    outfile : Path
        Where to save the file
    """

    if outfile is None:
        outfile = Path().cwd() / "output.json"

    if isinstance(outfile, str):
        outfile = Path(outfile)

    if outfile.exists() and overwrite is False:
        raise FileExistsError(
            f"{outfile.name} already exists at that location. "
            f"If you really wish to save the file to {outfile.parent}, "
            f"please retry with overwrite set to True"
        )

    obs_dict = self.obs.to_dict()
    var_dict = self.var.to_dict()
    scale_data = self.X.T.tolist()
    counts = self.raw.X.toarray().tolist()

    paga_dict = {
        "connectivities": self.uns["paga"]["connectivities"].todense().tolist(),
        "connectivities_tree": self.uns["paga"]["connectivities_tree"]
        .todense()
        .tolist(),
        "groups": self.uns["paga"]["groups"],
        "pos": self.uns["paga"]["pos"].tolist(),
    }

    reductions = {
        x[2:]: pd.DataFrame(
            self.obsm[x],
            index=self.obs.index,
            columns=[f"{x[2:]}_{y+1}" for y in range(self.obsm[x].shape[1])],
        ).to_dict()
        for x in self.obsm
    }

    uns_dict = {
        i: j
        for i, j
        in zip(
            self.uns,
             [
                 self.uns[x].tolist()
                if isinstance(self.uns[x], np.ndarray)
                else self.uns[x]
                for x
                in self.uns
              ]
            )
        }

    adata_dict = {
        "flavor": "anndata",
        "obs": obs_dict,
        "var": var_dict,
        "scale_data": scale_data,
        "counts": counts,
        "uns": uns_dict,
        "obsm": reductions,
        "paga": paga_dict,
        "varm": {x: self.varm[x].tolist() for x in self.varm},
        "obsp": {y: self.obsp[y].toarray().tolist() for y in self.obsp},
    }

    if compress:
        with gzopen(outfile.with_suffix(outfile.suffix + ".gz"), "wb") as out_json:
            out_json.write(dumps(adata_dict))
    else:
        with open(outfile, "wb") as out_json:
            out_json.write(dumps(adata_dict))
