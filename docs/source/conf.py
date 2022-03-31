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

sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'whots-annual-report'
copyright = '2022, Fernando Carvalho Pacheco'
author = 'Fernando Carvalho Pacheco'

# The full version, including alpha/beta/rc tags
release = '0.0.1'

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "nbsphinx",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
]

intersphinx_mapping = {
    "cchdo-website": ("https://exchange-format.readthedocs.io/en/latest/", None),
}

myst_url_schemes = ["http", "https", ]

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
templates_path = ['_templates']
source_suffix = '.md'
# master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.env']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_logo = "../source/_static/_images/logo_HOT.png"
html_title = "WHOTS"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
    "repository_url": "https://github.com/hot-dogs/whots-annual-report",
    "use_repository_button": True,
    "use_issues_button": True,
    "home_page_in_toc": False,
}

