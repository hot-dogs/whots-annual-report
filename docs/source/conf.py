# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath("."))

# -- Project information -----------------------------------------------------

project = "whots-annual-report"
copyright = f"{datetime.now().year}, Hawaii Ocean Time-series (HOT)"
author = "Hawaii Ocean Time-series (HOT)"

# The full version, including alpha/beta/rc tags
release = "1.0.0"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "nbsphinx",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinxcontrib.bibtex",
]


bibtex_bibfiles = ["latex_templates/refs.bib"]
bibtex_default_style = "unsrt"
bibtex_reference_style = "author_year"

myst_url_schemes = [
    "http",
    "https",
]

# Added cross reference for headings
myst_heading_anchors = 3

# Add numbered roles
numfig = True

# Enable some MyST extensions.
myst_enable_extensions = [
    "colon_fence",
]

# Make sure the explicity target is unique
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 3

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
# master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "build",
    "thumbs.db",
    ".ds_store",
    ".env",
    ".rst",
    "Thumbs.db",
    ".DS_store",
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_logo = "../source/_static/_images/new_logo_HOT.png"
html_title = "WHOTS"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_theme_options = {
    "repository_url": "https://github.com/hot-dogs/whots-annual-report",
    "use_repository_button": True,
    "use_issues_button": True,
    "home_page_in_toc": False,
}
