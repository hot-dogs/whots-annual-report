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

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.env']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_logo = "../build/html/_images/logo_HOT.jpg"
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

# -- Options for LaTeX output ---------------------------------------------
latex_engine = 'pdflatex'

latex_elements = {'papersize': 'a4paper', 'releasename': " ", 'fncychap': '\\usepackage{fncychap}',
                  'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}', 'figure_align': 'htbp',
                  'pointsize': '10pt',
                  'preamble': '\\usepackage[margin=1in]{geometry}\n' + \
                              '\\usepackage[nodayofweek,level]{datetime}\n' + \
                              '\\usepackage{authblk}\n' + \
                              '\\usepackage{graphicx} % Include Images\n' + \
                              '\\graphicspath{ {2.Figures/} }\n' + \
                              '\\setlength{\parskip}{1em}% Add Space between paragraphs\n' + \
                              '\\setlength{\parindent}{0em}\n' + \
                              '\\usepackage[backend=biber, style=authoryear]{biblatex} % Allow Citations\n' + \
                              '\\addbibresource{whots16.bib}\n' + \
                              '\\usepackage{appendix} % Add Appendix to document\n' + \
                              '\\usepackage[labelfont=bf, skip=5pt, font=small]{caption}%Add extra functions to captions\n' + \
                              '\\usepackage{subcaption} % Allow for subcaptions on subfigure encironments\n' + \
                              '\\usepackage{soul} % Allows use of `\hl{}` command for highlighting text\n' + \
                              '\\usepackage[utf8]{inputenc} % Ensure UTF8 Encoding\n' + \
                              '\\usepackage{hyperref} % Hyper links\n' + \
                              '\\hypersetup{colorlinks=true,linkcolor=blue, filecolor=magenta, urlcolor=cyan, citecolor=blue, pdfnewwindow=true}\n',
                  'maketitle': r'''
        \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1

        \begin{titlepage}
                \centering
                
                {\scshape\Large {University of Hawaii at Manoa} \par}
                
                \rule{\textwidth}{0.4pt}\vspace*{-\baselineskip}\vspace{3.2pt} 
                \rule{\textwidth}{1.6pt}
                
                \vspace{1cm}
                
                \hbox{\hspace{0em} \includegraphics[width=16cm]{2.Figures/logos/alll_whot_report.png}}
                \rule{\textwidth}{1.6pt}\vspace*{-\baselineskip}\vspace*{2pt} % Thick 
                \rule{\textwidth}{0.4pt} % Thin horizontal rule
                
                {\Large \textbf{Hydrographic Observations At the Woods Hole Oceanographic Institution Hawaii Ocean Time-series Site: 2019 - 2020} \par}
                
                by\par
                
                {\normalsize \ 
                Fernando Carvalho Pacheco\footnote{The University of Hawaii at Manoa}, 
                Fernando Santiago-Mandujano\footnotemark[\value{footnote}], 
                Albert Plueddemann\footnote{Woods Hole Oceanographic Institution},
                Robert Weller\footnotemark[\value{footnote}],
                James Potemra\footnotemark[1],
                Daniel Fitzgerald\footnotemark[1] 
                and Nan Galbraith\footnotemark[2] \par}
                
                \vspace{0.25cm}
                {\normalsize \today\par} 
                {\Large\bfseries Technical Data Report - 15 \par}
                
                \vspace{1cm}
                
                {\normalsize \ Approved for public release; distribution unlimited. \par}
            
            % Bottom of the page
                \vspace{1.5cm}
                
                {\normalsize \ The University of Hawaii at Manoa \\
                School of Ocean and Earth Science and Technology \\
                1000 Pope Road, Honolulu, Hawaii 96822\par}
                \vspace{1cm}
                
                {\large\ SOEST Publication no.  \par} 
                
                \vspace{0.25cm}

        \end{titlepage}

        \clearpage
        \pagenumbering{roman}
        \tableofcontents
        \listoffigures
        \listoftables
        \clearpage
        \pagenumbering{arabic}

        ''', 'sphinxsetup': 'hmargin={0.7in,0.7in}, vmargin={1in,1in}, \
        verbatimwithframe=true, \
        TitleColor={rgb}{0,0,0}, \
        HeaderFamily=\\rmfamily\\bfseries, \
        InnerLinkColor={rgb}{0,0,1}, \
        OuterLinkColor={rgb}{0,0,1}', 'tableofcontents': ' '}
