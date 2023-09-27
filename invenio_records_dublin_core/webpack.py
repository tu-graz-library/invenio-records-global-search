# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""JS/CSS Webpack bundles for theme."""

from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": {
            "entry": {
                "invenio-records-dublin-core-theme": "./less/invenio_records_dublin_core/theme.less",
                "invenio-records-dublin-core-search": "./js/invenio_records_dublin_core/search/index.js",
            },
            "dependencies": {},
            "aliases": {
                "@js/invenio_records_dublin_core": "js/invenio_records_dublin_core",
                "@less/invenio_records_dublin_core": "less/invenio_records_dublin_core",
                "@translations/invenio_records_dublin_core": "translations/invenio_records_dublin_core",
            },
        },
    },
)
