# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Dublin Core Metadata Schema."""
from marshmallow import Schema, validate
from marshmallow.fields import String
from marshmallow_utils.fields import SanitizedUnicode


class DublinCoreMetadataSchema(Schema):
    """DublinCoreMetadataSchema."""

    contributor = String()
    title = SanitizedUnicode(required=True, validate=validate.Length(min=3))
    creator = String(required=True)
    identifier = String(required=True)
    relation = String()
    right = String(required=True)
    date = String()
    subject = String()
    description = String()
    publisher = String()
    type = String()
    source = String()
    language = String()
    location = String()
    format = String()
