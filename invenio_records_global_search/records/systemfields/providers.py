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

    pid_type = "dc"
