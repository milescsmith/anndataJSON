# anndataJSON

[![PyPI](https://img.shields.io/pypi/v/anndataJSON.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/anndataJSON.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/anndataJSON)][python version]
[![License](https://img.shields.io/pypi/l/anndataJSON)][license]

[![Read the documentation at https://anndataJSON.readthedocs.io/](https://img.shields.io/readthedocs/anndataJSON/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/milescsmith/anndataJSON/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/milescsmith/anndataJSON/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/anndataJSON/
[status]: https://pypi.org/project/anndataJSON/
[python version]: https://pypi.org/project/anndataJSON
[read the docs]: https://anndataJSON.readthedocs.io/
[tests]: https://github.com/milescsmith/anndataJSON/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/milescsmith/anndataJSON
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

# Why?

I need something that is able to convert back and forth between AnnData/Scanpy and Seurat and
1) the other options do not work (in particular, {hdf5r} has some issues) and
2) I don't entirely understand using the HDF5 format or know how to use Zarr, certainly not 
enough to fix anything

Yes, JSON is slow and the files are bloated, but it is easy.

## Features

- Adds functions for exporting an AnnData object to JSON and importing a scRNAseq dataset into an AnnData object

NOTE: At the moment, only a simple implementation of exporting works.

## Requirements

- TODO

## Installation

Currently, _anndataJSON_ must be installed via [pip] from github:

```console
$ pip install git+https://github.com/milescsmith/anndataJSON
```

## Usage

Through some decorator magic, these functions are added as methods to an AnnData
object, so simply importing the function like

```python
from anndataJSON import to_json

adata.to_json("path/to/file.json")
```

is sufficient.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [GPL 3.0 license][license],
_anndataJSON_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/milescsmith/anndataJSON/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/milescsmith/anndataJSON/blob/main/LICENSE
[contributor guide]: https://github.com/milescsmith/anndataJSON/blob/main/CONTRIBUTING.md
[command-line reference]: https://anndataJSON.readthedocs.io/en/latest/usage.html
