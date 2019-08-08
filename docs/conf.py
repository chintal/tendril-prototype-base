# -*- coding: utf-8 -*-
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
from pkg_resources import get_distribution

_github_repo = 'tendril-prototype-base'
_github_user = 'tendril-framework'

_package_name = u'tendril-prototype-base'
_package_author = u'Tendril Framework'
_package_copyright = u'2015-19'
_package_logo = '_static/logo.png'
_package_favicon = '_static/favicon.ico'

_dist = get_distribution(_package_name)
_package_release = _dist.version
_package_description = ''
for m in _dist._get_metadata(_dist.PKG_INFO):
    if m.startswith('Summary:'):
        _package_description = m.split(':')[1]

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

sys.path.insert(0, os.path.abspath(os.pardir))
autodoc_default_options = {
    'members': None, 'undoc-members': None,
    'private-members': None, 'show-inheritance': None
}
autodoc_member_order = 'bysource'
autoclass_content = 'init'

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.graphviz',
    'sphinx.ext.autosummary',
    'sphinxarg.ext',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = _package_name
copyright = u'{0}, {1}'.format(_package_copyright, _package_author)
author = _package_author

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = _package_release

# The short X.Y version.
version = '.'.join(release.split('.')[:2])

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

import alabaster

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [alabaster.get_path()]

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "alabaster"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'description': _package_description,
    'fixed_sidebar': False,
    'touch_icon': 'favicon.ico',
    'github_repo': _github_repo,
    'github_user': _github_user,
}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = '{0} v{1}'.format(project, version)

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = _package_logo

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = _package_favicon

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'donate.html',
    ]
}

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = '{0}-doc'.format(_package_name)

# -- Options for LaTeX output ---------------------------------------------

from sphinx.highlighting import PygmentsBridge
from pygments.formatters.latex import LatexFormatter


class CustomLatexFormatter(LatexFormatter):
    def __init__(self, **options):
        super(CustomLatexFormatter, self).__init__(**options)
        self.verboptions = r"formatcom=\footnotesize"


PygmentsBridge.latex_formatter = CustomLatexFormatter

latex_maketitle_override = r'''
    \makeatletter
    \renewcommand{\maketitle}{
        \begingroup
            % These \defs are required to deal with multi-line authors; it
            % changes \\ to ', ' (comma-space), making it pass muster for
            % generating document info in the PDF file.
            \def\\{, }
            \def\and{and }
            \pdfinfo{
              /Author (\@author)
              /Title (\@title)
            }
        \endgroup
        \noindent\begin{minipage}{0.3\textwidth}
        \sphinxlogo%
        \end{minipage}
        \thispagestyle{empty}
        \hfill
        \begin{minipage}{0.65\textwidth}
        \begin{flushright}    
            {\rm\Huge\py@HeaderFamily \@title} \par
            \vspace{10pt}
            {\em\large\py@HeaderFamily \py@release\releaseinfo,} {\em\@date}\par
            \vspace{15pt}
            {\large\py@HeaderFamily
            \begin{tabular}[t]{c}
            \@author
            \end{tabular}} \par
            \py@authoraddress \par
        \end{flushright}
        \@thanks
        \end{minipage}
        \setcounter{footnote}{0}
        \let\thanks\relax\let\maketitle\relax
        %\gdef\@thanks{}\gdef\@author{}\gdef\@title{}
    }
    \makeatother
'''

latex_pagestyle_override = r"""
    \makeatletter
      \fancypagestyle{normal}{ 
        \fancyhf{}
        \fancyhead[L]{\rightmark}
        \fancyhead[C]{\@title, \py@release}
        \fancyhead[R]{\thepage}
        \fancyfoot[R]{\includegraphics[width=0.1\textwidth]{logo_packed.png}}
      }
    \makeatother
"""

# \renewcommand{\headrulewidth}{0.4pt}
# \renewcommand{\footrulewidth}{0.4pt}

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '9pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': r'\usepackage{tfrupee}' + '\n' +
                r'\DeclareUnicodeCharacter{20B9}{\rupee}' + '\n' +
                r'\definecolor{VerbatimBorderColor}{rgb}{1,1,1}' + '\n' +
                latex_maketitle_override +
                latex_pagestyle_override,

    'maketitle': r'\maketitle',
    'tableofcontents': r'',
    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
    'extraclassoptions': 'openany',
    'printindex': r'\footnotesize\raggedright\printindex',
    'fncychap': '\\usepackage[Bjornstrup]{fncychap}',
    # 'sphinxsetup': 'vmargin={0.7in,1in}'
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(
    master_doc, 
    '{0}.tex'.format(_package_name),
    u'{0} Documentation'.format(_package_name),
    _package_author, 'howto'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
if _package_logo:
    latex_logo = _package_logo

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
latex_show_urls = 'footnote'

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
latex_domain_indices = False

# latex_toplevel_sectioning = 'chapter'


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(
    master_doc, _package_name, 
    u'{0} documentation'.format(_package_name),
    [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [(
    master_doc, _package_name, u'{0} Documentation'.format(_package_name),
    author, _package_name, _package_description,
    'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/3': None}