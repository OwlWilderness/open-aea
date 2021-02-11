# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gym.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="gym.proto",
    package="aea.fetchai.gym.v0_1_0",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=b'\n\tgym.proto\x12\x16\x61\x65\x61.fetchai.gym.v0_1_0"\x94\x07\n\nGymMessage\x12\x42\n\x03\x61\x63t\x18\x05 \x01(\x0b\x32\x33.aea.fetchai.gym.v0_1_0.GymMessage.Act_PerformativeH\x00\x12\x46\n\x05\x63lose\x18\x06 \x01(\x0b\x32\x35.aea.fetchai.gym.v0_1_0.GymMessage.Close_PerformativeH\x00\x12J\n\x07percept\x18\x07 \x01(\x0b\x32\x37.aea.fetchai.gym.v0_1_0.GymMessage.Percept_PerformativeH\x00\x12\x46\n\x05reset\x18\x08 \x01(\x0b\x32\x35.aea.fetchai.gym.v0_1_0.GymMessage.Reset_PerformativeH\x00\x12H\n\x06status\x18\t \x01(\x0b\x32\x36.aea.fetchai.gym.v0_1_0.GymMessage.Status_PerformativeH\x00\x1a\x18\n\tAnyObject\x12\x0b\n\x03\x61ny\x18\x01 \x01(\x0c\x1a\x61\n\x10\x41\x63t_Performative\x12<\n\x06\x61\x63tion\x18\x01 \x01(\x0b\x32,.aea.fetchai.gym.v0_1_0.GymMessage.AnyObject\x12\x0f\n\x07step_id\x18\x02 \x01(\x05\x1a\xc4\x01\n\x14Percept_Performative\x12\x0f\n\x07step_id\x18\x01 \x01(\x05\x12\x41\n\x0bobservation\x18\x02 \x01(\x0b\x32,.aea.fetchai.gym.v0_1_0.GymMessage.AnyObject\x12\x0e\n\x06reward\x18\x03 \x01(\x02\x12\x0c\n\x04\x64one\x18\x04 \x01(\x08\x12:\n\x04info\x18\x05 \x01(\x0b\x32,.aea.fetchai.gym.v0_1_0.GymMessage.AnyObject\x1a\x9b\x01\n\x13Status_Performative\x12T\n\x07\x63ontent\x18\x01 \x03(\x0b\x32\x43.aea.fetchai.gym.v0_1_0.GymMessage.Status_Performative.ContentEntry\x1a.\n\x0c\x43ontentEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x14\n\x12Reset_Performative\x1a\x14\n\x12\x43lose_PerformativeB\x0e\n\x0cperformativeb\x06proto3',
)


_GYMMESSAGE_ANYOBJECT = _descriptor.Descriptor(
    name="AnyObject",
    full_name="aea.fetchai.gym.v0_1_0.GymMessage.AnyObject",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="any",
            full_name="aea.fetchai.gym.v0_1_0.GymMessage.AnyObject.any",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=414,
    serialized_end=438,
)

_GYMMESSAGE_ACT_PERFORMATIVE = _descriptor.Descriptor(
    name="Act_Performative",
    full_name="aea.fetchai.gym.v0_1_0.GymMessage.Act_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="action",
            full_name="aea.fetchai.gym.v0_1_0.GymMessage.Act_Performative.action",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="step_id",
            full_name="aea.fetchai.gym.v0_1_0.GymMessage.Act_Performative.step_id",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=440,
    serialized_end=537,
)

_GYMMESSAGE_PERCEPT_PERFORMATIVE = _descriptor.Descriptor(
    name="Percept_Performative",
    full_name="aea.fetchai.gym.v0_1_0.GymMessage.Percept_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="step_id",
            full_name="aea.fetchai.gym.v0_1_0.GymMessage.Percept_Performative.step_id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="observation",
            full_name="aea.fetchai.gym.v0_1_0.GymMessage.Percept_Performative.observation",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="reward",
            full_name="aea.fetchai.gym.v0_1_0.GymMessage.Percept_Performative.reward",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="done",
            full_name="aea.fetchai.gym.v0_1_0.GymMessage.Percept_Performative.done",
            index=3,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="info",
            full_name="aea.fetchai.gym.v0_1_0.GymMessage.Percept_Performative.info",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=540,
    serialized_end=736,
)

_GYMMESSAGE_STATUS_PERFORMATIVE_CONTENTENTRY = _descriptor.Descriptor(
    name="ContentEntry",
    full_name="aea.fetchai.gym.v0_1_0.GymMessage.Status_Performative.ContentEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="aea.fetchai.gym.v0_1_0.GymMessage.Status_Performative.ContentEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="aea.fetchai.gym.v0_1_0.GymMessage.Status_Performative.ContentEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=848,
    serialized_end=894,
)

_GYMMESSAGE_STATUS_PERFORMATIVE = _descriptor.Descriptor(
    name="Status_Performative",
    full_name="aea.fetchai.gym.v0_1_0.GymMessage.Status_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="content",
            full_name="aea.fetchai.gym.v0_1_0.GymMessage.Status_Performative.content",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_GYMMESSAGE_STATUS_PERFORMATIVE_CONTENTENTRY,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=739,
    serialized_end=894,
)

_GYMMESSAGE_RESET_PERFORMATIVE = _descriptor.Descriptor(
    name="Reset_Performative",
    full_name="aea.fetchai.gym.v0_1_0.GymMessage.Reset_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=896,
    serialized_end=916,
)

_GYMMESSAGE_CLOSE_PERFORMATIVE = _descriptor.Descriptor(
    name="Close_Performative",
    full_name="aea.fetchai.gym.v0_1_0.GymMessage.Close_Performative",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=918,
    serialized_end=938,
)

_GYMMESSAGE = _descriptor.Descriptor(
    name="GymMessage",
    full_name="aea.fetchai.gym.v0_1_0.GymMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="act",
            full_name="aea.fetchai.gym.v0_1_0.GymMessage.act",
            index=0,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="close",
            full_name="aea.fetchai.gym.v0_1_0.GymMessage.close",
            index=1,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="percept",
            full_name="aea.fetchai.gym.v0_1_0.GymMessage.percept",
            index=2,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="reset",
            full_name="aea.fetchai.gym.v0_1_0.GymMessage.reset",
            index=3,
            number=8,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="status",
            full_name="aea.fetchai.gym.v0_1_0.GymMessage.status",
            index=4,
            number=9,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[
        _GYMMESSAGE_ANYOBJECT,
        _GYMMESSAGE_ACT_PERFORMATIVE,
        _GYMMESSAGE_PERCEPT_PERFORMATIVE,
        _GYMMESSAGE_STATUS_PERFORMATIVE,
        _GYMMESSAGE_RESET_PERFORMATIVE,
        _GYMMESSAGE_CLOSE_PERFORMATIVE,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="performative",
            full_name="aea.fetchai.gym.v0_1_0.GymMessage.performative",
            index=0,
            containing_type=None,
            fields=[],
        ),
    ],
    serialized_start=38,
    serialized_end=954,
)

_GYMMESSAGE_ANYOBJECT.containing_type = _GYMMESSAGE
_GYMMESSAGE_ACT_PERFORMATIVE.fields_by_name[
    "action"
].message_type = _GYMMESSAGE_ANYOBJECT
_GYMMESSAGE_ACT_PERFORMATIVE.containing_type = _GYMMESSAGE
_GYMMESSAGE_PERCEPT_PERFORMATIVE.fields_by_name[
    "observation"
].message_type = _GYMMESSAGE_ANYOBJECT
_GYMMESSAGE_PERCEPT_PERFORMATIVE.fields_by_name[
    "info"
].message_type = _GYMMESSAGE_ANYOBJECT
_GYMMESSAGE_PERCEPT_PERFORMATIVE.containing_type = _GYMMESSAGE
_GYMMESSAGE_STATUS_PERFORMATIVE_CONTENTENTRY.containing_type = (
    _GYMMESSAGE_STATUS_PERFORMATIVE
)
_GYMMESSAGE_STATUS_PERFORMATIVE.fields_by_name[
    "content"
].message_type = _GYMMESSAGE_STATUS_PERFORMATIVE_CONTENTENTRY
_GYMMESSAGE_STATUS_PERFORMATIVE.containing_type = _GYMMESSAGE
_GYMMESSAGE_RESET_PERFORMATIVE.containing_type = _GYMMESSAGE
_GYMMESSAGE_CLOSE_PERFORMATIVE.containing_type = _GYMMESSAGE
_GYMMESSAGE.fields_by_name["act"].message_type = _GYMMESSAGE_ACT_PERFORMATIVE
_GYMMESSAGE.fields_by_name["close"].message_type = _GYMMESSAGE_CLOSE_PERFORMATIVE
_GYMMESSAGE.fields_by_name["percept"].message_type = _GYMMESSAGE_PERCEPT_PERFORMATIVE
_GYMMESSAGE.fields_by_name["reset"].message_type = _GYMMESSAGE_RESET_PERFORMATIVE
_GYMMESSAGE.fields_by_name["status"].message_type = _GYMMESSAGE_STATUS_PERFORMATIVE
_GYMMESSAGE.oneofs_by_name["performative"].fields.append(
    _GYMMESSAGE.fields_by_name["act"]
)
_GYMMESSAGE.fields_by_name["act"].containing_oneof = _GYMMESSAGE.oneofs_by_name[
    "performative"
]
_GYMMESSAGE.oneofs_by_name["performative"].fields.append(
    _GYMMESSAGE.fields_by_name["close"]
)
_GYMMESSAGE.fields_by_name["close"].containing_oneof = _GYMMESSAGE.oneofs_by_name[
    "performative"
]
_GYMMESSAGE.oneofs_by_name["performative"].fields.append(
    _GYMMESSAGE.fields_by_name["percept"]
)
_GYMMESSAGE.fields_by_name["percept"].containing_oneof = _GYMMESSAGE.oneofs_by_name[
    "performative"
]
_GYMMESSAGE.oneofs_by_name["performative"].fields.append(
    _GYMMESSAGE.fields_by_name["reset"]
)
_GYMMESSAGE.fields_by_name["reset"].containing_oneof = _GYMMESSAGE.oneofs_by_name[
    "performative"
]
_GYMMESSAGE.oneofs_by_name["performative"].fields.append(
    _GYMMESSAGE.fields_by_name["status"]
)
_GYMMESSAGE.fields_by_name["status"].containing_oneof = _GYMMESSAGE.oneofs_by_name[
    "performative"
]
DESCRIPTOR.message_types_by_name["GymMessage"] = _GYMMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GymMessage = _reflection.GeneratedProtocolMessageType(
    "GymMessage",
    (_message.Message,),
    {
        "AnyObject": _reflection.GeneratedProtocolMessageType(
            "AnyObject",
            (_message.Message,),
            {
                "DESCRIPTOR": _GYMMESSAGE_ANYOBJECT,
                "__module__": "gym_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.gym.v0_1_0.GymMessage.AnyObject)
            },
        ),
        "Act_Performative": _reflection.GeneratedProtocolMessageType(
            "Act_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _GYMMESSAGE_ACT_PERFORMATIVE,
                "__module__": "gym_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.gym.v0_1_0.GymMessage.Act_Performative)
            },
        ),
        "Percept_Performative": _reflection.GeneratedProtocolMessageType(
            "Percept_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _GYMMESSAGE_PERCEPT_PERFORMATIVE,
                "__module__": "gym_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.gym.v0_1_0.GymMessage.Percept_Performative)
            },
        ),
        "Status_Performative": _reflection.GeneratedProtocolMessageType(
            "Status_Performative",
            (_message.Message,),
            {
                "ContentEntry": _reflection.GeneratedProtocolMessageType(
                    "ContentEntry",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _GYMMESSAGE_STATUS_PERFORMATIVE_CONTENTENTRY,
                        "__module__": "gym_pb2"
                        # @@protoc_insertion_point(class_scope:aea.fetchai.gym.v0_1_0.GymMessage.Status_Performative.ContentEntry)
                    },
                ),
                "DESCRIPTOR": _GYMMESSAGE_STATUS_PERFORMATIVE,
                "__module__": "gym_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.gym.v0_1_0.GymMessage.Status_Performative)
            },
        ),
        "Reset_Performative": _reflection.GeneratedProtocolMessageType(
            "Reset_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _GYMMESSAGE_RESET_PERFORMATIVE,
                "__module__": "gym_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.gym.v0_1_0.GymMessage.Reset_Performative)
            },
        ),
        "Close_Performative": _reflection.GeneratedProtocolMessageType(
            "Close_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _GYMMESSAGE_CLOSE_PERFORMATIVE,
                "__module__": "gym_pb2"
                # @@protoc_insertion_point(class_scope:aea.fetchai.gym.v0_1_0.GymMessage.Close_Performative)
            },
        ),
        "DESCRIPTOR": _GYMMESSAGE,
        "__module__": "gym_pb2"
        # @@protoc_insertion_point(class_scope:aea.fetchai.gym.v0_1_0.GymMessage)
    },
)
_sym_db.RegisterMessage(GymMessage)
_sym_db.RegisterMessage(GymMessage.AnyObject)
_sym_db.RegisterMessage(GymMessage.Act_Performative)
_sym_db.RegisterMessage(GymMessage.Percept_Performative)
_sym_db.RegisterMessage(GymMessage.Status_Performative)
_sym_db.RegisterMessage(GymMessage.Status_Performative.ContentEntry)
_sym_db.RegisterMessage(GymMessage.Reset_Performative)
_sym_db.RegisterMessage(GymMessage.Close_Performative)


_GYMMESSAGE_STATUS_PERFORMATIVE_CONTENTENTRY._options = None
# @@protoc_insertion_point(module_scope)