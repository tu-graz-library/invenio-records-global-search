# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Dublin Core data model for InvenioRDM."""

from flask import Flask

from . import config
from .resources import DublinCoreRecordResource, DublinCoreRecordResourceConfig
from .services import DublinCoreRecordService, DublinCoreRecordServiceConfig


class InvenioRecordsDublinCore:
    """Invenio-Records-Dublin-Core extension."""

    def __init__(self, app: Flask = None) -> None:
        """Construct InvenioRecordsDublinCore."""
        if app:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """Flask application initialization."""
        self.init_config(app)
        self.init_services(app)
        self.init_resources(app)
        app.extensions["invenio-records-dublin-core"] = self

    def init_config(self, app: Flask) -> None:
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith("DUBLIN_CORE_"):
                app.config.setdefault(k, getattr(config, k))

    def init_services(self, app: Flask) -> None:
        """Initialize services."""
        service_config = DublinCoreRecordServiceConfig.build(app)
        self.records_service = DublinCoreRecordService(config=service_config)

    def init_resources(self, app: Flask) -> None:
        """Initialize resources."""
        self.records_resource = DublinCoreRecordResource(
            service=self.records_service,
            config=DublinCoreRecordResourceConfig,
        )
