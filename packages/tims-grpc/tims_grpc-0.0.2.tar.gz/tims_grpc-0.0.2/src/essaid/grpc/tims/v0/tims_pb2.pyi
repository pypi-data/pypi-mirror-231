from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Concept(_message.Message):
    __slots__ = ["code", "label"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    code: str
    label: str
    def __init__(self, code: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...

class PathRequest(_message.Message):
    __slots__ = ["to", "count", "level"]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    to: Concept
    count: int
    level: int
    def __init__(self, to: _Optional[_Union[Concept, _Mapping]] = ..., count: _Optional[int] = ..., level: _Optional[int] = ..., **kwargs) -> None: ...

class Path(_message.Message):
    __slots__ = ["concepts"]
    CONCEPTS_FIELD_NUMBER: _ClassVar[int]
    concepts: _containers.RepeatedCompositeFieldContainer[Concept]
    def __init__(self, concepts: _Optional[_Iterable[_Union[Concept, _Mapping]]] = ...) -> None: ...
