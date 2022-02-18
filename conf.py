# Setup for "autodoc" in MyST powered website
import os
import sys

sys.path.insert(0, os.path.abspath("."))
# End "autodoc" setup.
# Also for "rinohtype"
sys.path.insert(0, os.path.abspath("../.."))
sys.setrecursionlimit(1500)


project = "My Amazing Site"
# This one shows up int the browser tab
html_title = "LOL, It Is A Nice Site"
copyright = "2022, Michael B <gloc.mike@hey.com>"
author = "Michael B <gloc.mike@hey.com>"
language = "en"

extensions = [
    "myst_parser",
    # Setup for "autodoc" in MyST powered website
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "ablog",
    "sphinx.ext.intersphinx",
    "sphinx_ext_substitution",
    "rinoh.frontend.sphinx",
]
myst_update_mathjax = False

# latex_elements = {
#     "papersize" : "letterpaper",
#     "pointsize" : "10pt",
#     "preamble" : "",
#     "figure_align" : "htbp"
# }

exclude_patterns = [
    "_build",
    "_publish",
    "Thumbs.db",
    ".DS_Store",
    "posts/*/.ipynb_checkpoints/*",
    ".github/*",
    ".history",
    "github_submodule/*",
    "LICENSE.md",
    "README.md",
]

html_theme = "alabaster"
# html_theme = "sphinx_book_theme"
# html_theme_options = {
#     "rightsidebar": "true",
#     "relbarbgcolor": "black"
# }
html_static_path = ["_static"]
html_css_files = [
    "custom.css",
    "css/custom_style_autodoc.css",
    "css/custom_style_code_blocks.css",
    "css/asciinema-player.css",
]

# pygments_style = 'monokai'

# For asciimena javascript??
html_js_files = [
    "js/asciinema-player.js",
]
html_logo = "_static/logo/archer_small_405.png"

templates_path = ["_templates"]

# html_sidebars = {
#     "**": ["sbt-sidebar-nav.html", "sbt-sidebar-footer.html"]
# }
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "relations.html",
        "luv_sphinx.html",
        "searchbox.html",
        "donate.html",
    ]
}

# MyST Config Settings
myst_enable_extensions = [
    "colon_fence",
    "substitution",
]

# Auto-generated header anchors
# Ref: https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#syntax-header-anchors
myst_heading_anchors = 2

# Intersphinz settings
intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
myst_url_schemes = [
    "http",
    "https",
]

# Global substitutions
myst_substitutions = {"snippet": "I'm a **substitution**"}
