# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio Dublin Core Record Resource."""

from flask_resources import route
from invenio_records_resources.resources import RecordResource


class DublinCoreRecordResource(RecordResource):
    """DublinCoreRecordResource."""

    def create_url_rules(self) -> list:
        """Create url rules for record resource."""
        routes = self.config.routes

        return [
            route("GET", routes["list"], self.search),
        ]
