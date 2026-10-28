# SPDX-FileCopyrightText: 2023-2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Global Search Schemas."""

from invenio_records_resources.services.records.schema import BaseRecordSchema
from marshmallow.fields import Dict
from marshmallow_utils.fields import NestedAttribute

from .metadata import GlobalSearchMetadataSchema


class GlobalSearchRecordSchema(BaseRecordSchema):
    """GlobalSearchRecordSchema."""

    metadata = NestedAttribute(GlobalSearchMetadataSchema)

    original = Dict()
