from t2iapi.activation_state import types_pb2 as _types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetComponentActivationRequest(_message.Message):
    __slots__ = ["handle", "activation"]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_FIELD_NUMBER: _ClassVar[int]
    handle: str
    activation: _types_pb2.ComponentActivation
    def __init__(self, handle: _Optional[str] = ..., activation: _Optional[_Union[_types_pb2.ComponentActivation, str]] = ...) -> None: ...

class SetAlertActivationRequest(_message.Message):
    __slots__ = ["handle", "activation"]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_FIELD_NUMBER: _ClassVar[int]
    handle: str
    activation: _types_pb2.AlertActivation
    def __init__(self, handle: _Optional[str] = ..., activation: _Optional[_Union[_types_pb2.AlertActivation, str]] = ...) -> None: ...

class ComponentActivationTransitionRequest(_message.Message):
    __slots__ = ["handle", "start_activation", "end_activation"]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    START_ACTIVATION_FIELD_NUMBER: _ClassVar[int]
    END_ACTIVATION_FIELD_NUMBER: _ClassVar[int]
    handle: str
    start_activation: _types_pb2.ComponentActivation
    end_activation: _types_pb2.ComponentActivation
    def __init__(self, handle: _Optional[str] = ..., start_activation: _Optional[_Union[_types_pb2.ComponentActivation, str]] = ..., end_activation: _Optional[_Union[_types_pb2.ComponentActivation, str]] = ...) -> None: ...

class SetSystemSignalActivationRequest(_message.Message):
    __slots__ = ["handle", "manifestation", "activation"]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    MANIFESTATION_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_FIELD_NUMBER: _ClassVar[int]
    handle: str
    manifestation: _types_pb2.AlertSignalManifestation
    activation: _types_pb2.AlertActivation
    def __init__(self, handle: _Optional[str] = ..., manifestation: _Optional[_Union[_types_pb2.AlertSignalManifestation, str]] = ..., activation: _Optional[_Union[_types_pb2.AlertActivation, str]] = ...) -> None: ...
