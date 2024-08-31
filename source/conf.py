# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Small Technical Practices Workshop'
copyright = '2023, nikkie'
author = 'nikkie'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.githubpages',
    "sphinx_copybutton",
    "sphinx_new_tab_link",
    "sphinxcontrib.mermaid",
    "sphinxext.opengraph",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_css_files = ["https://fonts.googleapis.com/css2?family=BIZ+UDGothic"]
html_theme_options = {"font_family": "BIZ UDGothic"}

ogp_social_cards = {
    "enable": False,
}
