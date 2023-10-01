# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Original Component."""

from invenio_records_resources.services.records.components.base import ServiceComponent


class OriginalComponent(ServiceComponent):
    """Service component for metadata."""

    def create(self, identity, data=None, record=None, errors=None, **kwargs):
        """Inject parsed view to the record."""
        print(f"OriginalComponent.create data: {data}, record: {record}")
        record.original = data.get("original", "")

    def update(self, identity, data=None, record=None, **kwargs):
        """Inject parsed view to the record."""
        print("OriginalComponent.update")
        record.original = data.get("original", "")
