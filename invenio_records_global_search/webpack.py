# SPDX-FileCopyrightText: 2023-2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""JS/CSS Webpack bundles for theme."""

from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": {
            "entry": {
                "invenio-records-global-search-theme": "./less/invenio_records_global_search/theme.less",
                "invenio-records-global-search-search": "./js/invenio_records_global_search/search/index.js",
            },
            "dependencies": {},
            "aliases": {
                "@js/invenio_records_global_search": "js/invenio_records_global_search",
                "@less/invenio_records_global_search": "less/invenio_records_global_search",
                "@translations/invenio_records_global_search": "translations/invenio_records_global_search",
            },
        },
    },
)
