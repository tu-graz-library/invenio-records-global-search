# SPDX-FileCopyrightText: 2023-2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""System Fields for Global Search records."""

from .context import GlobalSearchPIDFieldContext
from .original import OriginalField
from .providers import GlobalSearchRecordProvider

__all__ = ("GlobalSearchRecordProvider", "GlobalSearchPIDFieldContext", "OriginalField")
