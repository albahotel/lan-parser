from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Statuses(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OK: _ClassVar[Statuses]
    Error: _ClassVar[Statuses]

class LighStates(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    On: _ClassVar[LighStates]
    Off: _ClassVar[LighStates]

class DoorLockStates(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Open: _ClassVar[DoorLockStates]
    Close: _ClassVar[DoorLockStates]

class States(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LightOn: _ClassVar[States]
    LightOff: _ClassVar[States]
    DoorLockOpen: _ClassVar[States]
    DoorLockClose: _ClassVar[States]
OK: Statuses
Error: Statuses
On: LighStates
Off: LighStates
Open: DoorLockStates
Close: DoorLockStates
LightOn: States
LightOff: States
DoorLockOpen: States
DoorLockClose: States

class IdentifyRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class GetState(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetInfo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetState(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: States
    def __init__(self, state: _Optional[_Union[States, str]] = ...) -> None: ...

class State(_message.Message):
    __slots__ = ("light_on", "door_lock", "temperature", "pressure", "humidity")
    LIGHT_ON_FIELD_NUMBER: _ClassVar[int]
    DOOR_LOCK_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    PRESSURE_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    light_on: LighStates
    door_lock: DoorLockStates
    temperature: float
    pressure: float
    humidity: float
    def __init__(self, light_on: _Optional[_Union[LighStates, str]] = ..., door_lock: _Optional[_Union[DoorLockStates, str]] = ..., temperature: _Optional[float] = ..., pressure: _Optional[float] = ..., humidity: _Optional[float] = ...) -> None: ...

class Info(_message.Message):
    __slots__ = ("ip", "mac", "ble_name", "token")
    IP_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    BLE_NAME_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ip: str
    mac: str
    ble_name: str
    token: str
    def __init__(self, ip: _Optional[str] = ..., mac: _Optional[str] = ..., ble_name: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class ClientMessage(_message.Message):
    __slots__ = ("get_info", "set_state", "get_state")
    GET_INFO_FIELD_NUMBER: _ClassVar[int]
    SET_STATE_FIELD_NUMBER: _ClassVar[int]
    GET_STATE_FIELD_NUMBER: _ClassVar[int]
    get_info: GetInfo
    set_state: SetState
    get_state: GetState
    def __init__(self, get_info: _Optional[_Union[GetInfo, _Mapping]] = ..., set_state: _Optional[_Union[SetState, _Mapping]] = ..., get_state: _Optional[_Union[GetState, _Mapping]] = ...) -> None: ...

class ControllerResponse(_message.Message):
    __slots__ = ("info", "state", "status")
    INFO_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    info: Info
    state: State
    status: Statuses
    def __init__(self, info: _Optional[_Union[Info, _Mapping]] = ..., state: _Optional[_Union[State, _Mapping]] = ..., status: _Optional[_Union[Statuses, str]] = ...) -> None: ...
