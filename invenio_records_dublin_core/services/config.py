# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Dublin Core Service Config."""

from typing import ClassVar

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

from ..records import DublinCoreRecord
from .components import DefaultRecordsComponents
from .facets import data_model, formats, publishers, rights, subjects, types
from .permissions import DublinCoreRecordPermissionPolicy
from .schemas import DublinCoreRecordSchema


class DublinCoreSearchOptions(SearchOptions, SearchOptionsMixin):
    """Search options for record search."""

    facets: ClassVar = {
        "data_model": data_model,
        "subjects": subjects,
        "publishers": publishers,
        "formats": formats,
        "rights": rights,
        "types": types,
    }


class DublinCoreRecordServiceConfig(RecordServiceConfig, ConfiguratorMixin):
    """Dublin Core record service config class."""

    record_cls = DublinCoreRecord

    schema = FromConfig(
        "DUBLIN_CORE_SCHEMA",
        default=DublinCoreRecordSchema,
    )

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
    components = FromConfig(
        "DUBLIN_CORE_RECORDS_SERVICE_COMPONENTS",
        default=DefaultRecordsComponents,
    )
