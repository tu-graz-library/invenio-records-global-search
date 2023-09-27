# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio Dublin Core Records module to create REST APIs."""

from .config import DublinCoreRecordResourceConfig
from .resources import DublinCoreRecordResource

__all__ = ("DublinCoreRecordResource", "DublinCoreRecordResourceConfig")
