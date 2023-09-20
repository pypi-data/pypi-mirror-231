import abc
import dataclasses
import inspect
import typing
from collections import OrderedDict

from . import utils
from .fields.base import Field
from .fields.fields import AvroField


@dataclasses.dataclass  # type: ignore
class BaseSchemaDefinition(abc.ABC):
    """
    Minimal Schema definition
    """

    __slots__ = (
        "type",
        "klass",
        "parent",
        "matadata",
    )

    type: str
    klass: typing.Any
    parent: typing.Any
    metadata: utils.SchemaMetadata

    @abc.abstractmethod
    def get_rendered_fields(self) -> typing.List[OrderedDict]:
        ...  # pragma: no cover

    @abc.abstractmethod
    def render(self) -> OrderedDict:
        ...  # pragma: no cover

    def get_schema_name(self) -> str:
        return self.klass.metadata.schema_name or self.klass.__name__

    def generate_documentation(self) -> typing.Optional[str]:
        if isinstance(self.metadata.schema_doc, str):
            doc = self.metadata.schema_doc
        else:
            doc = self.klass.__doc__
            # dataclasses create a (in avro context) useless docstring by default,
            # which we don't want in the schema.
            is_dataclass_with_default_docstring = (
                dataclasses.is_dataclass(self.klass)
                # from https://github.com/python/cpython/blob/3.10/Lib/dataclasses.py
                and doc == (self.klass.__name__ + str(inspect.signature(self.klass)).replace(" -> None", ""))
            )
            if is_dataclass_with_default_docstring:
                return None

        if doc is not None:
            return doc.strip()
        return None


@dataclasses.dataclass
class AvroSchemaDefinition(BaseSchemaDefinition):
    fields: typing.List[Field] = dataclasses.field(default_factory=list)
    # mapping of field_name: Field
    fields_map: typing.Dict[str, Field] = dataclasses.field(default_factory=dict)

    def __post_init__(self) -> None:
        self.fields = self.parse_dataclasses_fields()
        self.fields_map = {field.name: field for field in self.fields}

    def parse_dataclasses_fields(self) -> typing.List[Field]:
        exclude = self.metadata.exclude

        if utils.is_faust_model(self.klass):
            return self.parse_faust_fields(exclude=exclude)
        elif utils.is_pydantic_model(self.klass):
            return self.parse_pydantic_fields(exclude=exclude)
        return self.parse_fields(exclude=exclude)

    def parse_fields(self, exclude: typing.List) -> typing.List[Field]:
        return [
            AvroField(
                dataclass_field.name,
                dataclass_field.type,
                default=dataclass_field.default,
                default_factory=dataclass_field.default_factory,  # type: ignore  # TODO: resolve mypy
                metadata=dict(dataclass_field.metadata),
                model_metadata=self.metadata,
                parent=self.parent,
            )
            for dataclass_field in dataclasses.fields(self.klass)
            if dataclass_field.name not in exclude
        ]

    def parse_faust_fields(self, exclude: typing.List) -> typing.List[Field]:
        schema_fields = []

        for dataclass_field in dataclasses.fields(self.klass):
            if dataclass_field.name in exclude:
                continue

            faust_field = dataclass_field.default
            metadata = dataclass_field.metadata
            default_factory = dataclasses.MISSING

            if faust_field is not dataclasses.MISSING:
                if faust_field.required:
                    default = dataclasses.MISSING
                else:
                    default = faust_field.default

                    if isinstance(default, dataclasses.Field):
                        metadata = default.metadata
                        default_factory = default.default_factory  # type: ignore  # TODO: resolve mypy
                        default = dataclasses.MISSING

                schema_fields.append(
                    AvroField(
                        dataclass_field.name,
                        dataclass_field.type,
                        default=default,
                        default_factory=default_factory,
                        metadata=dict(metadata),
                        model_metadata=self.metadata,
                        parent=self.parent,
                    )
                )

        return schema_fields

    def parse_pydantic_fields(self, exclude: typing.List) -> typing.List[Field]:
        return [
            AvroField(
                model_field.name,
                model_field.annotation,
                default=dataclasses.MISSING
                if model_field.required or model_field.default_factory
                else model_field.default,
                default_factory=model_field.default_factory,
                metadata=model_field.field_info.extra.get("metadata", {}),
                model_metadata=self.metadata,
                parent=self.parent,
            )
            for model_field in self.klass.__fields__.values()
            if model_field.name not in exclude
        ]

    def get_rendered_fields(self) -> typing.List[OrderedDict]:
        field_order = self.metadata.field_order

        if field_order is not None:
            for field_name in self.fields_map.keys():
                if field_name not in field_order:
                    field_order.append(field_name)

            return [self.fields_map[field_name].render() for field_name in field_order]
        return [field.render() for field in self.fields]

    def render(self) -> OrderedDict:
        schema = OrderedDict(
            [
                ("type", self.type),
                ("name", self.get_schema_name()),
                ("fields", self.get_rendered_fields()),
            ]
        )

        if self.metadata.schema_doc:
            doc = self.generate_documentation()
            if doc is not None:
                schema["doc"] = doc

        if self.metadata.namespace is not None:
            schema["namespace"] = self.metadata.namespace

        if self.metadata.aliases is not None:
            schema["aliases"] = self.metadata.aliases

        return schema

    def get_fields_map(self) -> typing.Dict[str, Field]:
        return self.fields_map
