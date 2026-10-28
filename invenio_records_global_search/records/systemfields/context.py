# SPDX-FileCopyrightText: 2023-2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Global Search PID context."""

from invenio_records_resources.records.systemfields.pid import PIDFieldContext


class GlobalSearchPIDFieldContext(PIDFieldContext):
    """GlobalSearchPIDFieldContext."""

    pid_type = "gs"
