# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Dublin Core Metadata Schema."""
from marshmallow import Schema, validate
from marshmallow_utils.fields import SanitizedUnicode


class DublinCoreMetadataSchema(Schema):
    """DublinCoreMetadataSchema."""

    title = SanitizedUnicode(required=True, validate=validate.Length(min=3))
