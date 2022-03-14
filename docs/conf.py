"""Sphinx configuration."""
from datetime import datetime


project = "Pyalanysis"
author = "Anton Bossenbroek"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "myst_parser",
]
html_static_path = ["_static"]
