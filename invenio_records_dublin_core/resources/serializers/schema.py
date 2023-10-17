# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio Dublin Core Record Resource schema."""

from marshmallow import Schema, fields
from marshmallow_utils.fields import SanitizedUnicode


def access_status(obj: dict) -> dict:
    """Access status."""
    return {
        "id": "open",
        "icon": "unlock",
        "title_l10n": "Open",
    }


class DublinCoreSchema(Schema):
    """Schema for dumping extra information for the dublin core record."""

    id = SanitizedUnicode(data_key="id", attribute="id")

    access_status = fields.Function(access_status)

    class Meta:
        """Meta class to accept unknwon fields."""

        additional = ("metadata", "original")
