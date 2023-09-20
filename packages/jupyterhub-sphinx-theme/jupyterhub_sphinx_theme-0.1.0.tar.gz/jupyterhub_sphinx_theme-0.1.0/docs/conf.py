# Configuration file for Sphinx to build our documentation to HTML.
#
# Configuration reference: https://www.sphinx-doc.org/en/master/usage/configuration.html
#
from datetime import datetime

# -- Project information -----------------------------------------------------
# ref: https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
#
project = "JupyterHub Sphinx Theme"
copyright = f"2022 - {datetime.now().year}, JupyterHub"
author = "JupyterHub"


# -- General Sphinx configuration ---------------------------------------------------
# ref: https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
#
extensions = [
    "myst_parser",
    "jupyterhub_sphinx_theme",
]
root_doc = "index"
source_suffix = [".rst", ".md"]


# -- Options for HTML output ----------------------------------------------
# ref: http://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
#
html_static_path = ["_static"]

# theme related configuration
html_theme = "jupyterhub_sphinx_theme"
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/jupyterhub/jupyterhub-sphinx-theme",
            "icon": "fa-brands fa-github",
        },
    ]
}
html_context = {
    "github_user": "jupyterhub",
    "github_repo": "jupyterhub-sphinx-theme",
    "github_version": "main",
}
