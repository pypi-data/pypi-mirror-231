import abc
import copy
import csv
from dataclasses import dataclass, field
from enum import IntEnum, unique
from typing import List, Optional, Protocol, Union

import pandas as pd

from penelope.type_alias import SerializableContent
from penelope.utility import create_class, dictify

# pylint: disable=too-many-instance-attributes


@unique
class ContentType(IntEnum):
    NONE = 0
    TAGGED_FRAME = 1
    TEXT = 2
    TOKENS = 3


@dataclass
class SerializeOpts:
    content_type_code: int = 0

    document_index_name: str = field(default="document_index.csv")
    document_index_sep: str = field(default='\t')

    sep: str = '\t'
    quoting: int = csv.QUOTE_NONE
    custom_serializer_classname: Optional[str] = None
    deserialize_processes: int = field(default=1)
    deserialize_chunksize: int = field(default=4)

    text_column: str = field(default="text")
    lemma_column: str = field(default="lemma")
    pos_column: str = field(default="pos")
    extra_columns: List[str] = field(default_factory=list)
    frequency_column: Optional[str] = field(default=None)
    index_column: Union[int, None] = field(default=0)
    feather_folder: Optional[str] = field(default=None)
    lower_lemma: bool = field(default=True)
    # abort_at_index: int = field(default=None)

    @property
    def props(self):
        return dictify(self)

    @property
    def content_type(self) -> ContentType:
        return ContentType(self.content_type_code)

    @content_type.setter
    def content_type(self, value: ContentType):
        self.content_type_code = int(value)

    def as_type(self, value: ContentType) -> "SerializeOpts":
        opts = copy.copy(self)
        opts.content_type_code = int(value)
        return opts

    @staticmethod
    def create(data: dict) -> "SerializeOpts":
        opts = SerializeOpts()
        for key in data.keys():
            if hasattr(opts, key):
                setattr(opts, key, data[key])
        return opts

    @property
    def custom_serializer(self) -> type:
        if not self.custom_serializer_classname:
            return None
        return create_class(self.custom_serializer_classname)

    @property
    def columns(self) -> List[str]:
        return [self.text_column, self.lemma_column, self.pos_column] + (self.extra_columns or [])

    def text_column_name(self, lemmatized: bool = False):
        return self.lemma_column if lemmatized else self.text_column

    @property
    def tagged_columns(self) -> dict:
        return dict(
            text_column=self.text_column,
            lemma_column=self.lemma_column,
            pos_column=self.pos_column,
        )


class Serializer(Protocol):
    def __call__(self, data: str, options: SerializeOpts) -> pd.DataFrame:
        ...


class IContentSerializer(abc.ABC):
    @abc.abstractmethod
    def serialize(self, *, content: SerializableContent, options: SerializeOpts) -> str:
        ...

    @abc.abstractmethod
    def deserialize(self, *, content: str, options: SerializeOpts) -> SerializableContent:
        ...

    @abc.abstractmethod
    def compute_term_frequency(self, *, content: SerializableContent, options: SerializeOpts) -> dict:
        ...
