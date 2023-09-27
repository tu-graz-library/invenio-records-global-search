# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Dublin Core PID providers."""

from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2


class DublinCoreRecordProvider(RecordIdProviderV2):
    """DublinCoreRecordProvider."""

    pid_type = "dc"
