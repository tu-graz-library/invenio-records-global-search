# SPDX-FileCopyrightText: 2023-2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Invenio Dublin Core Records module to create REST APIs."""

from .config import GlobalSearchRecordResourceConfig
from .resources import GlobalSearchRecordResource

__all__ = ("GlobalSearchRecordResource", "GlobalSearchRecordResourceConfig")
