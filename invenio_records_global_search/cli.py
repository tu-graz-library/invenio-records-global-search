# -*- coding: utf-8 -*-
#
# Copyright (C) 2023-2025 Graz University of Technology.
#
# invenio-records-global-search is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""CLI."""

import click
from flask import current_app
from flask.cli import with_appcontext
from invenio_access.permissions import system_identity

from .proxies import current_records_global_search


def _extract_datamodel_from_gs_config(cfg: str) -> list[str]:
    funcs = current_app.config.get(cfg, [])
    func_base_name = cfg.removeprefix("GLOBAL_SEARCH_").lower()
    return [func.__name__.removeprefix(func_base_name) for func in funcs]


@click.group()
def global_search() -> None:
    """CLI-group for "invenio record global search" commands."""


@global_search.command()
@with_appcontext
def rebuild_index() -> None:
    """Reindex all records."""
    click.secho("Reindexing records of global search...", fg="green")

    service = current_records_global_search.records_service  # type: ignore[attr-defined]
    service.rebuild_index(identity=system_identity)

    click.secho("Reindexed records!", fg="green")


@global_search.command()
@click.option(
    "--model",
    default=None,
    help="Run only the rebuild function for this data model.",
)
@with_appcontext
def rebuild_database(model: str | None) -> None:
    """Rebuild database."""
    funcs = current_app.config.get("GLOBAL_SEARCH_REBUILD_DATABASE", [])
    if model:
        funcs = [func for func in funcs if model in func.__name__]

        if not funcs:
            msg = f"No rebuild function for data model '{model}'. Known options: {_extract_datamodel_from_gs_config("GLOBAL_SEARCH_REBUILD_DATABASE")}"
            raise click.ClickException(msg)

    for func in funcs:
        func()


@global_search.command()
@click.option(
    "--model",
    default=None,
    help="Update only missing GS Records for this data model.",
)
@with_appcontext
def update_missing(model: str | None) -> None:
    """Update GS database with missing records from original data-models."""
    funcs = current_app.config.get("GLOBAL_SEARCH_UPDATE_MISSING", [])
    if model:
        funcs = [func for func in funcs if model in func.__name__]

        if not funcs:
            msg = f"No update missing function for data model '{model}'. Known options: {_extract_datamodel_from_gs_config("GLOBAL_SEARCH_UPDATE_MISSING")}"
            raise click.ClickException(msg)

    for func in funcs:
        func()
