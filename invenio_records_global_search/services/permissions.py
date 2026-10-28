# SPDX-FileCopyrightText: 2023-2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Global Search permission policy."""

from typing import ClassVar

from invenio_records_permissions.generators import AnyUser, RecordOwners, SystemProcess
from invenio_records_permissions.policies.records import RecordPermissionPolicy


class GlobalSearchRecordPermissionPolicy(RecordPermissionPolicy):
    """GlobalSearchRecordPermissionPolicy."""

    can_create: ClassVar = [AnyUser(), SystemProcess()]

    can_search: ClassVar = [AnyUser(), SystemProcess()]
    can_read: ClassVar = [AnyUser(), RecordOwners()]

    can_update: ClassVar = [AnyUser(), SystemProcess()]
