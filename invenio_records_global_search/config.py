# SPDX-FileCopyrightText: 2023-2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Configs."""

from typing import Any

from invenio_i18n import gettext as _

from .services.facets import (
    access,
    data_model,
    formats,
    publishers,
    rights,
    subjects,
    types,
)

GLOBAL_SEARCH_FACETS: dict[str, dict[str, Any]] = {
    "data_model": {
        "facet": data_model,
        "ui": {
            "field": "original.schema",
        },
    },
    "subjects": {
        "facet": subjects,
        "ui": {
            "field": "metadata.subjects",
        },
    },
    "publishers": {
        "facet": publishers,
        "ui": {
            "field": "metadata.publishers",
        },
    },
    "formats": {
        "facet": formats,
        "ui": {
            "field": "metadata.formats",
        },
    },
    "rights": {
        "facet": rights,
        "ui": {
            "field": "metadata.rights",
        },
    },
    "types": {
        "facet": types,
        "ui": {
            "field": "metadata.types",
        },
    },
    "access": {
        "facet": access,
        "ui": {
            "field": "original.access.status",
        },
    },
}

GLOBAL_SEARCH_SORT_OPTIONS = {
    "bestmatch": {
        "title": _("Best match"),
        "fields": ["_score"],  # search defaults to desc on `_score` field
    },
    "newest": {
        "title": _("Newest"),
        "fields": ["-original.created"],
    },
    "version": {
        "title": _("Version"),
        "fields": ["version_id"],
    },
}

GLOBAL_SEARCH_SEARCH = {
    "facets": [
        "data_model",
        "subjects",
        "publishers",
        "formats",
        "rights",
        "types",
        "access",
    ],
    "sort": [
        "bestmatch",
        "newest",
        "version",
    ],
}

GLOBAL_SEARCH_BASE_TEMPLATE = "invenio_records_global_search/base.html"

GLOBAL_SEARCH_NAV_TEMPLATE = None
"""Template injected above the global search app.

Set to a template path to render a custom nav above the search results
e.g. a resource type switcher. ``None`` disables the injection.
"""

GLOBAL_SEARCH_ORIGINAL_SCHEMAS: dict[str, dict[str, str]] = {}
"""Configure the original schema names."""
