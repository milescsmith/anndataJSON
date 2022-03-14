# src/anndata_to_json/__init__.py
"""anndata_to_json."""

from importlib.metadata import metadata, version

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

from .exporting import to_json
__all__ = ["to_json"]