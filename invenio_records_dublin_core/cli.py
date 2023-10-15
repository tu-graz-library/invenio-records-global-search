# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""CLI."""

import click
from flask.cli import with_appcontext
from invenio_access.permissions import system_identity

from .proxies import current_records_dublin_core


@click.group()
def dublin_core() -> None:
    """CLI-group for "invenio dublin core" commands."""


@dublin_core.command()
@with_appcontext
def rebuild_index() -> None:
    """Reindex all records."""
    click.secho("Reindexing records of dublinc core...", fg="green")

    service = current_records_dublin_core.records_service
    service.rebuild_index(identity=system_identity)

    click.secho("Reindexed records!", fg="green")
