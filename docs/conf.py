# -*- coding: utf-8 -*-
#
# Sphinx documentation build configuration file

from atelier.sphinxconf import configure

try:
    import lino
except ImportError:
    lino = None

extlinks = {}
extensions = []

configure(globals())

language = 'en'

extensions += ['atelier.sphinxconf.blog']
extensions += ['atelier.sphinxconf.complex_tables']

if False:
    extensions += ['lino.sphinxcontrib.logo']
    extensions += ['lino.sphinxcontrib.actordoc']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['.templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u"John's blog"
copyright = u'2014 John Doe'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#

# The full version, including alpha/beta/rc tags.
release = ''

# The short X.Y version.
version = ''

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_patterns = [
    'include/*',
]


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


html_style = 'default.css'

html_title = u"John's developer blog"

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = 'logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = 'favicon.ico'

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'
#~ last_updated = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': ['globaltoc.html', 'searchbox.html', 'links.html'],
}


if lino:
    extlinks.update(srcref=(lino.srcref_url, ''))
    extlinks.update(ticket=('http://trac.lino-framework.org/ticket/%s', '#'))

autosummary_generate = True

# http://sphinx.pocoo.org/theming.html
# html_theme = "classic"
# html_theme_options = dict(collapsiblesidebar=True, externalrefs=True)


# def setup(app):
#     app.add_stylesheet('centeredlogo.css')

