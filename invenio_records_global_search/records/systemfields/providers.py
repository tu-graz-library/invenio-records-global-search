# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-global-search is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Global Search PID providers."""

from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2


class GlobalSearchRecordProvider(RecordIdProviderV2):
    """GlobalSearchRecordProvider."""

    pid_type = "gs"

    @classmethod
    def generate_id(cls, options=None):
        """Generate id."""
        return cls.gs_pid

    @classmethod
    def create(cls, object_type=None, object_uuid=None, options=None, **kwargs):
        """Create."""
        cls.gs_pid = kwargs["record"]["gs_pid"]
        return super().create(object_type, object_uuid, options, **kwargs)
