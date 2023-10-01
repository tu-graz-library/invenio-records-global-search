# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Configs."""

from .services.facets import data_model


# TODO: use invenio-i18n gettext functionality
def _(x):
    """Identity function for string extraction."""
    return x


DUBLIN_CORE_FACETS = {
    "data_model": {
        "facet": data_model,
        "ui": {
            "field": "original.schema",
        },
    },
}

DUBLIN_CORE_SORT_OPTIONS = {
    "bestmatch": {
        "title": _("Best match"),
        "fields": ["_score"],  # search defaults to desc on `_score` field
    },
    "newest": {
        "title": _("Newest"),
        "fields": ["-created"],
    },
}

DUBLIN_CORE_SEARCH = {
    "facets": ["data_model"],
    "sort": [
        "bestmatch",
        "newest",
    ],
}

DUBLIN_CORE_BASE_TEMPLATE = "invenio_records_dublin_core/base.html"
