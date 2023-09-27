# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio Dublin Core Record Resource Config."""
from typing import ClassVar

from flask_resources import (
    JSONDeserializer,
    JSONSerializer,
    RequestBodyParser,
    ResponseHandler,
)
from invenio_records_resources.resources import (
    RecordResourceConfig,
    SearchRequestArgsSchema,
)
from marshmallow import fields

from .serializers import DublinCoreJSONSerializer


class DublinCoreRecordResourceConfig(RecordResourceConfig):
    """DublinCoreRecordResourceConfig."""

    blueprint_name = "dublin_core"

    url_prefix = "/dublin-core"

    default_accept_mimetype = "application/json"

    response_handlers: ClassVar = {
        "application/json": ResponseHandler(JSONSerializer()),
        "application/vnd.inveniodublincore.v1+json": ResponseHandler(
            DublinCoreJSONSerializer(),
        ),
    }

    routes: ClassVar = {
        "search": "/search",
        "list": "",
    }

    # Request parsing
    request_args = SearchRequestArgsSchema
    request_view_args: ClassVar = {
        "pid_value": fields.Str(),
        "pid_type": fields.Str(),
    }
    request_headers: ClassVar = {
        "if_match": fields.Int(),
    }
    request_body_parsers: ClassVar = {
        "application/json": RequestBodyParser(JSONDeserializer()),
    }
