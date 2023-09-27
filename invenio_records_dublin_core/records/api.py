# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Records API."""


from invenio_records.systemfields import ConstantField, DictField
from invenio_records_resources.records.api import Record
from invenio_records_resources.records.systemfields import IndexField, PIDField

from .models import DublinCoreMetadata
from .systemfields import DublinCorePIDFieldContext, DublinCoreRecordProvider


class DublinCoreRecord(Record):
    """Dublin Core Record."""

    model_cls = DublinCoreMetadata

    schema = ConstantField(
        "$schema",
        "local://dublin-core/records/dublin-core-record-v1.0.0.json",
    )

    index = IndexField("dublin-core-records-record-v1.0.0", search_alias="dublin-core")

    pids = DictField("pids")

    pid = PIDField(
        key="id",
        create=True,
        provider=DublinCoreRecordProvider,
        context_cls=DublinCorePIDFieldContext,
    )
