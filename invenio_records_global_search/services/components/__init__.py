# SPDX-FileCopyrightText: 2023-2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Components."""

from invenio_records_resources.services.records.components import MetadataComponent

from .original import OriginalComponent

DefaultRecordsComponents = [
    MetadataComponent,
    OriginalComponent,
]


__all__ = ("DefaultRecordsComponents",)
