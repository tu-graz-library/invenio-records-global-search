# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Views."""

from functools import partial

from flask import Blueprint, Flask, current_app, render_template
from invenio_search_ui.searchconfig import search_app_config

blueprint = Blueprint("invenio_records_dublin_core_ext", __name__)


@blueprint.record_once
def init(state):
    """Init app."""
    app = state.app
    # Register services - cannot be done in extension because
    # Invenio-Records-Resources might not have been initialized.
    registry = app.extensions["invenio-records-resources"].registry
    ext = app.extensions["invenio-records-dublin-core"]
    registry.register(ext.record_service, service_id="dublin-core-record")


def create_blueprint(app: Flask) -> Blueprint:
    """Create Blueprint."""
    routes = {
        "record-search": "/dublin-core/search",
    }

    blueprint = Blueprint(
        "invenio_records_dublin_core",
        __name__,
        template_folder="templates",
    )
    blueprint.add_url_rule(routes["record-search"], view_func=search)
    blueprint.app_context_processor(search_app_context)

    return blueprint


def search_app_context() -> dict:
    """Dublin Core search app context."""
    return {
        "search_app_dublin_core_config": partial(
            search_app_config,
            "DUBLIN_CORE_SEARCH",
            current_app.config["DUBLIN_CORE_FACETS"],
            current_app.config["DUBLIN_CORE_SORT_OPTIONS"],
            "/api/dublin-core",
            {"Accept": "application/vnd.inveniodublincore.v1+json"},
            app_id="DublinCoreRecords.Search",
        ),
    }


def search() -> str:
    """Search help guide."""
    return render_template("invenio_records_dublin_core/search/search.html")


def create_record_bp(app: Flask) -> Blueprint:
    """Create records blueprint."""
    return app.extensions["invenio-records-dublin-core"].record_resource.as_blueprint()
