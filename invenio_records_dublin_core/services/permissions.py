# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Dublin Core permission policy."""
from invenio_records_permissions.generators import AnyUser, SystemProcess
from invenio_records_permissions.policies.records import RecordPermissionPolicy


class DublinCoreRecordPermissionPolicy(RecordPermissionPolicy):
    """DublinCoreRecordPermissionPolicy."""

    can_create = [SystemProcess()]

    can_search = [AnyUser(), SystemProcess()]
