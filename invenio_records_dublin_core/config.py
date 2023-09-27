# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Configs."""

from enum import Enum

from invenio_records_resources.services.records.facets import TermsFacet


# TODO: use invenio-i18n gettext functionality
def _(x):
    """Identity function for string extraction."""
    return x


# copied from rdm-records
class AccessStatusEnum(Enum):
    """Enum defining access statuses."""

    OPEN = "open"

    EMBARGOED = "embargoed"

    RESTRICTED = "restricted"

    METADATA_ONLY = "metadata-only"


# copied from rdm-records
access_status = TermsFacet(
    field="access.status",
    label=_("Access status"),
    value_labels={
        AccessStatusEnum.OPEN.value: _("Open"),
        AccessStatusEnum.EMBARGOED.value: _("Embargoed"),
        AccessStatusEnum.RESTRICTED.value: _("Restricted"),
        AccessStatusEnum.METADATA_ONLY.value: _("Metadata-only"),
    },
)

DUBLIN_CORE_FACETS = {
    "access_status": {
        "facet": access_status,
        "ui": {
            "field": "access.status",
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
    "facets": ["access_status"],
    "sort": [
        "bestmatch",
        "newest",
    ],
}

DUBLIN_CORE_BASE_TEMPLATE = "invenio_records_dublin_core/base.html"
