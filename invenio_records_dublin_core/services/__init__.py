# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""High-level API for working with Dublin Core records, pids, search."""

from .config import DublinCoreRecordServiceConfig
from .services import DublinCoreRecordService

__all__ = ("DublinCoreRecordService", "DublinCoreRecordServiceConfig")