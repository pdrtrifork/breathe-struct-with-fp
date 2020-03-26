# Configuration file for the Sphinx documentation builder.


# -- Project information -----------------------------------------------------

project = 'Generating documentation for function pointers inside structs'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
	'breathe',
	'sphinx_rtd_theme',
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']


# -- Breathe -----------------------------------------------------------------

breathe_default_project = "project"
breathe_domain_by_extension = {
	"h" : "c",
}
breathe_projects_source = {
    "project" : ('src/', ['test.h'] )
}
breathe_projects = {
	"project": "doxygen/xml"
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
