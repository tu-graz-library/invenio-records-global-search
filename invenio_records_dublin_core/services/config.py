# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Dublin Core Service Config."""

from invenio_records_resources.services import (
    RecordServiceConfig,
    SearchOptions,
    pagination_links,
)
from invenio_records_resources.services.base.config import (
    ConfiguratorMixin,
    FromConfig,
    FromConfigSearchOptions,
    SearchOptionsMixin,
)
from invenio_records_resources.services.records.components import MetadataComponent

from ..records import DublinCoreRecord
from .components import OriginalComponent
from .facets import data_model
from .permissions import DublinCoreRecordPermissionPolicy
from .schemas import DublinCoreRecordSchema


class DublinCoreSearchOptions(SearchOptions, SearchOptionsMixin):
    """Search options for record search."""

    facets = {
        "data_model": data_model,
    }


class DublinCoreRecordServiceConfig(RecordServiceConfig, ConfiguratorMixin):
    """Dublin Core record service config class."""

    record_cls = DublinCoreRecord

    schema = DublinCoreRecordSchema

    permission_policy_cls = FromConfig(
        "DUBLIN_CORE_PERMISSION_POLICY",
        default=DublinCoreRecordPermissionPolicy,
    )

    links_search = pagination_links("{+api}/dublin-core{?args*}")

    # Search
    search = FromConfigSearchOptions(
        "DUBLIN_CORE_SEARCH",
        "DUBLIN_CORE_SORT_OPTIONS",
        "DUBLIN_CORE_FACETS",
        search_option_cls=DublinCoreSearchOptions,
    )

    components = [
        MetadataComponent,
        OriginalComponent,
    ]
