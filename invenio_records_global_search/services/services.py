# SPDX-FileCopyrightText: 2023-2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Global Search Services."""

from typing import Any

from flask import current_app
from flask_principal import Identity
from invenio_drafts_resources.records import Record
from invenio_pidstore.errors import PIDDoesNotExistError
from invenio_rdm_records.proxies import current_rdm_records_service
from invenio_records.errors import RecordsError
from invenio_records_resources.services import RecordService
from invenio_records_resources.services.records.results import (
    RecordBulkList,
    RecordItem,
    RecordList,
)
from invenio_records_resources.services.uow import (
    RecordBulkIndexOp,
    UnitOfWork,
    unit_of_work,
)
from sqlalchemy.exc import NoResultFound

from .utils import (
    build_gs_id_query,
    remove_parent_id_q,
    replace_query_params_with_known_schema,
)


class GlobalSearchRecordService(RecordService):
    """Global search record service."""

    @unit_of_work()
    def create_or_update(
        self,
        identity: Identity,
        data: dict,
        uow: UnitOfWork | None = None,
        *,
        expand: bool = False,
    ) -> RecordItem:
        """Create a record.

        :param identity: Identity of user creating the record.
        :param data: Input data according to the data schema.
        """
        gs_pid = "gs-" + data["original"]["pid"]

        try:
            # only to check if a record exists already
            self.record_cls.pid.resolve(gs_pid)

            return self.update(identity, id_=gs_pid, data=data)
        except PIDDoesNotExistError:
            self.record_cls.gs_pid = gs_pid
            return self._create(self.record_cls, identity, data, uow=uow, expand=expand)

    def create_or_update_batch(
        self,
        identity: Identity,
        data: list[dict],
        uow: UnitOfWork | None = None,
    ) -> RecordBulkList:
        """Create or update a batch of records.

        Args:
            identity: Identity of user creating the record.
            data: Input data according to the data schema.
            uow: Unit of work.

        """
        many_data = []
        for rec in data:
            gs_pid = "gs-" + rec["original"]["pid"]
            many_data.append((gs_pid, rec))

        return self.create_or_update_many(identity, many_data, uow=uow)

    @unit_of_work()
    def create_or_update_many(  # noqa: C901
        self,
        identity: Identity,
        data: list[tuple],
        uow: UnitOfWork | None = None,
    ) -> RecordBulkList:
        """Create or update a list of records.

        This method had to be overridden because for CREATE, the cls.gs_pid has to be set
        to the Original's pid + "gs-" prefix before the action is performed. Because of the
        nested structure of this function, the whole content had to be reproduced here too
        with the necessary addition marked by UPSTREAM DIFFERENCE comments.
        """
        records_processed = []

        self.require_permission(identity, "create_or_update_many")

        def _update_record(record_dict: dict, record: Record) -> None:
            """Update a record."""
            record_data, schema_errors = self.schema.load(
                record_dict,
                context={"identity": identity, "pid": record.pid, "record": record},
                raise_errors=False,
            )

            # If errors we avoid creating the record
            if schema_errors:
                records_processed.append(("update", record_dict, schema_errors, None))
                return

            # Run components
            self.run_components(
                "update",
                identity,
                data=record_data,
                record=record,
                uow=uow,
            )

            records_processed.append(("update", record, schema_errors, None))

        def _create_record(record_dict: dict) -> None:
            """Create a record."""
            # Validate data and create record with pid
            record_data, schema_errors = self.schema.load(
                record_dict,
                context={"identity": identity},
                raise_errors=False,
            )

            # If errors we avoid creating the record
            if schema_errors:
                records_processed.append(("create", record_dict, schema_errors, None))
                return

            # It's the components who saves the actual data in the record
            record = self.record_cls.create({})

            # Run components
            self.run_components(
                "create",
                identity,
                data=record_data,
                record=record,
                errors=schema_errors,
                uow=uow,
            )
            records_processed.append(("create", record, schema_errors, None))

        # We avoid using create and update methods to bulk index all records at once
        for record_id, record_dict in data:
            try:
                record = self.record_cls.pid.resolve(record_id)
                _update_record(record_dict, record)
            except (NoResultFound, PIDDoesNotExistError):
                # UPSTREAM DIFFERENCE START
                self.record_cls.gs_pid = record_id
                # UPSTREAM DIFFERENCE STOP
                _create_record(record_dict)
            except Exception as exc:  # noqa: BLE001
                records_processed.append(("create", record_dict, None, exc))
        valid_records = []

        for i, (action, record, errors, exc_) in enumerate(records_processed):
            if errors == [] and exc_ is None:
                try:
                    # Ideally the commit should be done in the uow,
                    # but since we need to keep track of the errors
                    # that might happen during the commit (e.g. relation errors)
                    # we keep it here.
                    record.commit()
                    valid_records.append(record)
                except RecordsError as exc:
                    # If commit fails we register the error for this record
                    records_processed[i] = (action, record, errors, exc)

        uow.register(RecordBulkIndexOp((r.id for r in valid_records), self.indexer))

        return self.result_bulk_list(self, identity, records_processed)

    def search(
        self,
        identity: Identity,
        params: dict | None = None,
        search_preference: str | None = None,
        expand: bool = False,  # noqa: FBT001, FBT002
        **kwargs: Any,  # noqa: ANN401
    ) -> RecordList:
        """Search for records matching the querystring.

        Method was overriden to rework query params that come as default from invenio-app-rdm
        into the global-search schema structure.
        """
        try:
            schema = self.config.schema
            metadata_field = schema().fields.get("metadata")
            metadata_schema = metadata_field.nested
        except AttributeError:
            current_app.logger("WARN: Schema unknown for query pre-processing")
            return super().search(
                identity,
                params=params,
                search_preference=search_preference,
                expand=expand,
                **kwargs,
            )

        if "q" not in params:
            return super().search(
                identity,
                params=params,
                search_preference=search_preference,
                expand=expand,
                **kwargs,
            )

        query = params["q"]
        if "parent.id" in query:
            # For queries that depend on the original parent record:
            # search for the original record because there is no connection
            # between original-parent.id and gs.record.
            # For now the workaround is implemented only for RDM-Records.
            original_records = current_rdm_records_service.search(
                identity,
                params=params,
                search_preference=search_preference,
                expand=expand,
                **kwargs,
            )

            # the query above returns only the final rdm-record version
            last_version = next(original_records.hits)

            # search for all versions based on the last published version
            original_all_versions = current_rdm_records_service.search_versions(
                identity,
                last_version.get("id") or "",
                params=params,
                search_preference=search_preference,
                expand=expand,
                **kwargs,
            )

            # edit gs query
            query_wo_pid = remove_parent_id_q(query)
            params["q"] = build_gs_id_query(original_all_versions) + query_wo_pid

        for metadata_field_name in metadata_schema().fields:
            if metadata_field_name in params["q"]:
                full_q = params["q"]
                params["q"] = replace_query_params_with_known_schema(
                    full_q,
                    metadata_field_name,
                )

        return super().search(
            identity,
            params=params,
            search_preference=search_preference,
            expand=expand,
            **kwargs,
        )
