# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

import shutil
import subprocess

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'control.ros.org'
copyright = '2021, ros2_control Maintainers'
author = 'ros2_control Maintainers'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx_rtd_theme',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**/CHANGELOG.rst', '**/README.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme_path = ['_themes']
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_context = {
    "display_github": True,
    "github_user": "ros-controls",
    "github_repo": "control.ros.org",
    "github_version": "master",
    "conf_py_path": "/",
    "source_suffix": source_suffix,
    "css_files": ['_static/override.css'],
    "favicon": "favicon_ros-controls.ico",
    "logo": "logo_ros-controls.png"
}

html_logo = "images/logo_ros-controls.png"
logo_only = True
html_favicon = "images/favicon_ros-controls.ico"

github_url = "https://github.com/ros-controls/control.ros.org"

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ros2ControlDocumentation'


# -- Extension configuration -------------------------------------------------
# copy transmission images to ros2_control/doc/_build/xml/ so that breathe picks them up as artifacts
shutil.copytree("ros2_control/transmission_interface/images/", "ros2_control/doc/_build/xml/", dirs_exist_ok=True)
# Copy resources folders
shutil.copytree("resources/", "_build/html/resources/", dirs_exist_ok=True)
# generate doxygen documentation
subprocess.run(['doxygen', 'doc/Doxyfile'], cwd='ros2_control')
# copy doxygen documentation to api subfolder
shutil.copytree("ros2_control/doc/_build/html", "_build/html/api")

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
