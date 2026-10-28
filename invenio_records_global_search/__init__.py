# SPDX-FileCopyrightText: 2023-2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Dublin Core data model for InvenioRDM."""

from .ext import InvenioRecordsGlobalSearch
from .proxies import current_records_global_search
from .records import GlobalSearchRecord

__version__ = "0.6.0"

__all__ = (
    "__version__",
    "InvenioRecordsGlobalSearch",
    "GlobalSearchRecord",
    "current_records_global_search",
)
