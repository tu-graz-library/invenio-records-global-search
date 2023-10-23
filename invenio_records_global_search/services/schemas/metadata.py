# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-global-search is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Dublin Core Metadata Schema."""
from marshmallow import Schema, validate
from marshmallow.fields import List, String
from marshmallow_utils.fields import SanitizedUnicode


class GlobalSearchMetadataSchema(Schema):
    """GlobalSearchMetadataSchema."""

    contributors = List(String())
    titles = List(SanitizedUnicode(required=True, validate=validate.Length(min=3)))
    creators = List(String(required=True))
    identifiers = List(String(required=True))
    relations = List(String())
    rights = List(String(required=True))
    dates = List(String())
    subjects = List(String())
    descriptions = List(String())
    publishers = List(String())
    types = List(String())
    sources = List(String())
    languages = List(String())
    locations = List(String())
    formats = List(String())
