# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Dublin Core PID context."""

from invenio_records.systemfields import RelatedModelFieldContext


class DublinCorePIDFieldContext(RelatedModelFieldContext):
    """DublinCorePIDFieldContext."""

    pid_type = "dc"
