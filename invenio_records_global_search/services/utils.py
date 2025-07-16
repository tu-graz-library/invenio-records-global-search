# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 Graz University of Technology.
#
# invenio-records-global-search is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.
"""Utils class."""

import re


def replace_query_params_with_known_schema(full_q: str, known_field_name: str) -> str:
    """Replace query fields.

    Given a default invenio-app-rdm query, replace the queried fields with fields from
    package defined schema.
    """
    result_q = full_q
    pattern = re.compile(r"\bmetadata(?:\.\w+)*(?=[^a-zA-Z0-9_-])")
    matches = re.findall(pattern, full_q)
    for match in matches:
        result_q = result_q.replace(match, f"metadata.{known_field_name}")

    return result_q
