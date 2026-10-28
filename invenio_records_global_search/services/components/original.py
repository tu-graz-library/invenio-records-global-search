# SPDX-FileCopyrightText: 2023-2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Original Component."""

from flask_principal import Identity
from invenio_records_resources.records.api import Record
from invenio_records_resources.services.records.components.base import ServiceComponent


class OriginalComponent(ServiceComponent):
    """Service component for metadata."""

    def create(
        self,
        _: Identity,
        data: dict,
        record: Record,
        errors: dict | None = None,  # noqa: ARG002
        **__: dict,
    ) -> None:
        """Inject parsed view to the record."""
        record.original = data.get("original", "")

    def update(
        self,
        _: Identity,
        data: dict,
        record: Record,
        **__: dict,
    ) -> None:
        """Inject parsed view to the record."""
        record.original = data.get("original", "")
