# SPDX-FileCopyrightText: 2023-2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""High-level API for working with Dublin Core records, pids, search."""

from .config import GlobalSearchRecordServiceConfig
from .services import GlobalSearchRecordService

__all__ = ("GlobalSearchRecordService", "GlobalSearchRecordServiceConfig")
