# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Dublin Core data model for InvenioRDM."""

from .ext import InvenioRecordsDublinCore
from .proxies import current_records_dublin_core
from .records import DublinCoreRecord

__version__ = "0.0.1"

__all__ = (
    "__version__",
    "InvenioRecordsDublinCore",
    "DublinCoreRecord",
    "current_records_dublin_core",
)
