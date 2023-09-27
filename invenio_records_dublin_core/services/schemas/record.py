# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Dublin Core Schemas."""

from invenio_records_resources.services.records.schema import BaseRecordSchema
from marshmallow_utils.fields import NestedAttribute

from .metadata import DublinCoreMetadataSchema


class DublinCoreRecordSchema(BaseRecordSchema):
    """DublinCoreRecordSchema."""

    metadata = NestedAttribute(DublinCoreMetadataSchema)
