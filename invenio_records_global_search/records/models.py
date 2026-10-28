# SPDX-FileCopyrightText: 2023-2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Dublin Core database models."""

from invenio_db import db
from invenio_records.models import RecordMetadataBase


class GlobalSearchMetadata(db.Model, RecordMetadataBase):
    """Base class for global search records."""

    __tablename__ = "global_search_metadata"
