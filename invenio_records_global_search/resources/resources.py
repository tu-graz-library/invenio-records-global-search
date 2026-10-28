# SPDX-FileCopyrightText: 2023-2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Invenio Global Search Record Resource."""

from flask_resources import route
from invenio_records_resources.resources import RecordResource


class GlobalSearchRecordResource(RecordResource):
    """GlobalSearchRecordResource."""

    def create_url_rules(self) -> list:
        """Create url rules for record resource."""
        routes = self.config.routes

        return [
            route("GET", routes["list"], self.search),
        ]
