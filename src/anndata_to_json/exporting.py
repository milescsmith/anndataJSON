from pathlib import Path
from typing import Union
from orjson import dump

import numpy as np
import pandas as pd
from anndata import AnnData

from typeguard import typechecked

from .utils import add_method, NumpyEncoder


# TODO: add gzipping on save, provided it isn't difficult to read
# a gzipped JSON file in R
@add_method(AnnData)
@typechecked
def to_json(self, outfile: Union[Path, str] = Path().cwd(), overwrite=True) -> None:
    """Save an Anndata object to disk in JSON format

    Parameters
    ----------
    outfile : Path
        Where to save the file
    """

    if isinstance(outfile, str):
        outfile = Path(outfile)
    
    if outfile.exists() & overwrite == False:
        raise FileExistsError(
            f"{outfile.name} already exists at that location. "
            f"If you really wish to save the file to {outfile.parent}, "
            f"please retry with overwrite set to True"
            )

    obs = self.obs.to_dict()
    var = self.var.to_dict()
    scale_data = adata.X.T.toarray().tolist()
    counts = self.raw.X.toarray().tolist()

    paga_dict = {
        "connectivities": self.uns["paga"]["connectivities"].todense(),
        "connectivities_tree": self.uns["paga"]["connectivities_tree"].todense(),
        "groups": self.uns['paga']['groups'],
        "pos": self.uns['paga']['pos'].tolist(),
    }

    reductions = {
        x[2:]: pd.DataFrame(
            self.obsm[x],
            index=self.obs.index,
            columns=[
                f"{x[2:]}_{y+1}" 
                for y 
                in range(self.obsm[x].shape[1])
            ]
        ).to_dict()
        for x 
        in self.obsm
    }

    # For the most part, I can't see why the information in
    # uns would need to be saved, except for maybe the PCA variance
    # info

    # uns = {
    #     i: j 
    #     for i, j 
    #     in zip(
    #         self.uns,
    #          [
    #              self.uns[x].tolist()
    #             if isinstance(self.uns[x], np.ndarray) 
    #             else self.uns[x] 
    #             for x 
    #             in self.uns
    #           ]
    #         )
    #     }

    adata_dict={
        "flavor": "anndata",
        "obs": obs,
        "var": var,
        "scale_data": scale_data,
        "counts": counts,
        # "uns": uns_dict,
        "obsm": reductions,
        "paga": paga_dict,
        "varm": {x: self.varm[x].tolist() for x in self.varm},
        "obsp": {y: self.obsp[y].toarray().tolist() for y in self.obsp},
    }

    with open(outfile, "w+") as out_json:
        json.dump(adata_dict, out_json, cls=NumpyEncoder)