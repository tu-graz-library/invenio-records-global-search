# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Facets."""

from invenio_i18n import gettext as _
from invenio_records_resources.services.records.facets import TermsFacet

data_model = TermsFacet(
    field="original.schema",
    label=_("DataModel"),
)

subjects = TermsFacet(
    field="metadata.subjects",
    label=_("Subjects"),
)

publishers = TermsFacet(
    field="metadata.publishers",
    label=_("Publishers"),
)

formats = TermsFacet(
    field="metadata.formats",
    label=_("Formats"),
)

rights = TermsFacet(
    field="metadata.rights",
    label=_("Rights"),
)

types = TermsFacet(
    field="metadata.types",
    label=_("Types"),
)
