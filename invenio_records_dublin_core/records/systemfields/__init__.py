# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""System Fields for Dublin Core records."""


from .context import DublinCorePIDFieldContext
from .original import OriginalField
from .providers import DublinCoreRecordProvider

__all__ = ("DublinCoreRecordProvider", "DublinCorePIDFieldContext", "OriginalField")
