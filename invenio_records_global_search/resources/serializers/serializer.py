# SPDX-FileCopyrightText: 2023-2026 Graz University of Technology.
# SPDX-License-Identifier: MIT

"""Invenio Dublin Core Record Resource serializers."""

from flask_resources import BaseListSchema, JSONSerializer
from flask_resources.serializers import MarshmallowSerializer

from .schema import GlobalSearchSchema


class GlobalSearchJSONSerializer(MarshmallowSerializer):
    """Dublin Core base serializer implementation."""

    def __init__(self) -> None:
        """Dublin Core Base Serializer Constructor.

        :param schema_cls: Default GlobalSearchSchema
        :param options: Json encoding options.
        """
        super().__init__(
            format_serializer_cls=JSONSerializer,
            object_schema_cls=GlobalSearchSchema,
            list_schema_cls=BaseListSchema,
        )
