"""Sphinx configuration."""
project = "anndataJSON"
author = "Miles Smith"
copyright = "2022, Miles Smith"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
