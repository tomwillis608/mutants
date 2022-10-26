"""Sphinx configuration."""
project = "Mutants"
author = "Tom Willis"
copyright = "2022, Tom Willis"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
