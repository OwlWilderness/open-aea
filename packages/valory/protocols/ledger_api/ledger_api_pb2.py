# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ledger_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x10ledger_api.proto\x12\x1d\x61\x65\x61.valory.ledger_api.v1_0_0"\x86\x15\n\x10LedgerApiMessage\x12W\n\x07\x62\x61lance\x18\x05 \x01(\x0b\x32\x44.aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Balance_PerformativeH\x00\x12S\n\x05\x65rror\x18\x06 \x01(\x0b\x32\x42.aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Error_PerformativeH\x00\x12_\n\x0bget_balance\x18\x07 \x01(\x0b\x32H.aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Get_Balance_PerformativeH\x00\x12o\n\x13get_raw_transaction\x18\x08 \x01(\x0b\x32P.aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Get_Raw_Transaction_PerformativeH\x00\x12[\n\tget_state\x18\t \x01(\x0b\x32\x46.aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Get_State_PerformativeH\x00\x12w\n\x17get_transaction_receipt\x18\n \x01(\x0b\x32T.aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Get_Transaction_Receipt_PerformativeH\x00\x12g\n\x0fraw_transaction\x18\x0b \x01(\x0b\x32L.aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Raw_Transaction_PerformativeH\x00\x12w\n\x17send_signed_transaction\x18\x0c \x01(\x0b\x32T.aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Send_Signed_Transaction_PerformativeH\x00\x12S\n\x05state\x18\r \x01(\x0b\x32\x42.aea.valory.ledger_api.v1_0_0.LedgerApiMessage.State_PerformativeH\x00\x12m\n\x12transaction_digest\x18\x0e \x01(\x0b\x32O.aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Transaction_Digest_PerformativeH\x00\x12o\n\x13transaction_receipt\x18\x0f \x01(\x0b\x32P.aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Transaction_Receipt_PerformativeH\x00\x1a\x18\n\x06Kwargs\x12\x0e\n\x06kwargs\x18\x01 \x01(\x0c\x1a)\n\x0eRawTransaction\x12\x17\n\x0fraw_transaction\x18\x01 \x01(\x0c\x1a/\n\x11SignedTransaction\x12\x1a\n\x12signed_transaction\x18\x01 \x01(\x0c\x1a\x16\n\x05State\x12\r\n\x05state\x18\x01 \x01(\x0c\x1a\x16\n\x05Terms\x12\r\n\x05terms\x18\x01 \x01(\x0c\x1a/\n\x11TransactionDigest\x12\x1a\n\x12transaction_digest\x18\x01 \x01(\x0c\x1a\x31\n\x12TransactionReceipt\x12\x1b\n\x13transaction_receipt\x18\x01 \x01(\x0c\x1a>\n\x18Get_Balance_Performative\x12\x11\n\tledger_id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x1ah\n Get_Raw_Transaction_Performative\x12\x44\n\x05terms\x18\x01 \x01(\x0b\x32\x35.aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Terms\x1a\x85\x01\n$Send_Signed_Transaction_Performative\x12]\n\x12signed_transaction\x18\x01 \x01(\x0b\x32\x41.aea.valory.ledger_api.v1_0_0.LedgerApiMessage.SignedTransaction\x1a\x85\x01\n$Get_Transaction_Receipt_Performative\x12]\n\x12transaction_digest\x18\x01 \x01(\x0b\x32\x41.aea.valory.ledger_api.v1_0_0.LedgerApiMessage.TransactionDigest\x1a:\n\x14\x42\x61lance_Performative\x12\x11\n\tledger_id\x18\x01 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\x02 \x01(\x05\x1aw\n\x1cRaw_Transaction_Performative\x12W\n\x0fraw_transaction\x18\x01 \x01(\x0b\x32>.aea.valory.ledger_api.v1_0_0.LedgerApiMessage.RawTransaction\x1a\x80\x01\n\x1fTransaction_Digest_Performative\x12]\n\x12transaction_digest\x18\x01 \x01(\x0b\x32\x41.aea.valory.ledger_api.v1_0_0.LedgerApiMessage.TransactionDigest\x1a\x83\x01\n Transaction_Receipt_Performative\x12_\n\x13transaction_receipt\x18\x01 \x01(\x0b\x32\x42.aea.valory.ledger_api.v1_0_0.LedgerApiMessage.TransactionReceipt\x1a\x93\x01\n\x16Get_State_Performative\x12\x11\n\tledger_id\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61llable\x18\x02 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x03(\t\x12\x46\n\x06kwargs\x18\x04 \x01(\x0b\x32\x36.aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Kwargs\x1am\n\x12State_Performative\x12\x11\n\tledger_id\x18\x01 \x01(\t\x12\x44\n\x05state\x18\x02 \x01(\x0b\x32\x35.aea.valory.ledger_api.v1_0_0.LedgerApiMessage.State\x1an\n\x12\x45rror_Performative\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x16\n\x0emessage_is_set\x18\x03 \x01(\x08\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\x12\x13\n\x0b\x64\x61ta_is_set\x18\x05 \x01(\x08\x42\x0e\n\x0cperformativeb\x06proto3'
)


_LEDGERAPIMESSAGE = DESCRIPTOR.message_types_by_name["LedgerApiMessage"]
_LEDGERAPIMESSAGE_KWARGS = _LEDGERAPIMESSAGE.nested_types_by_name["Kwargs"]
_LEDGERAPIMESSAGE_RAWTRANSACTION = _LEDGERAPIMESSAGE.nested_types_by_name[
    "RawTransaction"
]
_LEDGERAPIMESSAGE_SIGNEDTRANSACTION = _LEDGERAPIMESSAGE.nested_types_by_name[
    "SignedTransaction"
]
_LEDGERAPIMESSAGE_STATE = _LEDGERAPIMESSAGE.nested_types_by_name["State"]
_LEDGERAPIMESSAGE_TERMS = _LEDGERAPIMESSAGE.nested_types_by_name["Terms"]
_LEDGERAPIMESSAGE_TRANSACTIONDIGEST = _LEDGERAPIMESSAGE.nested_types_by_name[
    "TransactionDigest"
]
_LEDGERAPIMESSAGE_TRANSACTIONRECEIPT = _LEDGERAPIMESSAGE.nested_types_by_name[
    "TransactionReceipt"
]
_LEDGERAPIMESSAGE_GET_BALANCE_PERFORMATIVE = _LEDGERAPIMESSAGE.nested_types_by_name[
    "Get_Balance_Performative"
]
_LEDGERAPIMESSAGE_GET_RAW_TRANSACTION_PERFORMATIVE = (
    _LEDGERAPIMESSAGE.nested_types_by_name["Get_Raw_Transaction_Performative"]
)
_LEDGERAPIMESSAGE_SEND_SIGNED_TRANSACTION_PERFORMATIVE = (
    _LEDGERAPIMESSAGE.nested_types_by_name["Send_Signed_Transaction_Performative"]
)
_LEDGERAPIMESSAGE_GET_TRANSACTION_RECEIPT_PERFORMATIVE = (
    _LEDGERAPIMESSAGE.nested_types_by_name["Get_Transaction_Receipt_Performative"]
)
_LEDGERAPIMESSAGE_BALANCE_PERFORMATIVE = _LEDGERAPIMESSAGE.nested_types_by_name[
    "Balance_Performative"
]
_LEDGERAPIMESSAGE_RAW_TRANSACTION_PERFORMATIVE = _LEDGERAPIMESSAGE.nested_types_by_name[
    "Raw_Transaction_Performative"
]
_LEDGERAPIMESSAGE_TRANSACTION_DIGEST_PERFORMATIVE = (
    _LEDGERAPIMESSAGE.nested_types_by_name["Transaction_Digest_Performative"]
)
_LEDGERAPIMESSAGE_TRANSACTION_RECEIPT_PERFORMATIVE = (
    _LEDGERAPIMESSAGE.nested_types_by_name["Transaction_Receipt_Performative"]
)
_LEDGERAPIMESSAGE_GET_STATE_PERFORMATIVE = _LEDGERAPIMESSAGE.nested_types_by_name[
    "Get_State_Performative"
]
_LEDGERAPIMESSAGE_STATE_PERFORMATIVE = _LEDGERAPIMESSAGE.nested_types_by_name[
    "State_Performative"
]
_LEDGERAPIMESSAGE_ERROR_PERFORMATIVE = _LEDGERAPIMESSAGE.nested_types_by_name[
    "Error_Performative"
]
LedgerApiMessage = _reflection.GeneratedProtocolMessageType(
    "LedgerApiMessage",
    (_message.Message,),
    {
        "Kwargs": _reflection.GeneratedProtocolMessageType(
            "Kwargs",
            (_message.Message,),
            {
                "DESCRIPTOR": _LEDGERAPIMESSAGE_KWARGS,
                "__module__": "ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Kwargs)
            },
        ),
        "RawTransaction": _reflection.GeneratedProtocolMessageType(
            "RawTransaction",
            (_message.Message,),
            {
                "DESCRIPTOR": _LEDGERAPIMESSAGE_RAWTRANSACTION,
                "__module__": "ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:aea.valory.ledger_api.v1_0_0.LedgerApiMessage.RawTransaction)
            },
        ),
        "SignedTransaction": _reflection.GeneratedProtocolMessageType(
            "SignedTransaction",
            (_message.Message,),
            {
                "DESCRIPTOR": _LEDGERAPIMESSAGE_SIGNEDTRANSACTION,
                "__module__": "ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:aea.valory.ledger_api.v1_0_0.LedgerApiMessage.SignedTransaction)
            },
        ),
        "State": _reflection.GeneratedProtocolMessageType(
            "State",
            (_message.Message,),
            {
                "DESCRIPTOR": _LEDGERAPIMESSAGE_STATE,
                "__module__": "ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:aea.valory.ledger_api.v1_0_0.LedgerApiMessage.State)
            },
        ),
        "Terms": _reflection.GeneratedProtocolMessageType(
            "Terms",
            (_message.Message,),
            {
                "DESCRIPTOR": _LEDGERAPIMESSAGE_TERMS,
                "__module__": "ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Terms)
            },
        ),
        "TransactionDigest": _reflection.GeneratedProtocolMessageType(
            "TransactionDigest",
            (_message.Message,),
            {
                "DESCRIPTOR": _LEDGERAPIMESSAGE_TRANSACTIONDIGEST,
                "__module__": "ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:aea.valory.ledger_api.v1_0_0.LedgerApiMessage.TransactionDigest)
            },
        ),
        "TransactionReceipt": _reflection.GeneratedProtocolMessageType(
            "TransactionReceipt",
            (_message.Message,),
            {
                "DESCRIPTOR": _LEDGERAPIMESSAGE_TRANSACTIONRECEIPT,
                "__module__": "ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:aea.valory.ledger_api.v1_0_0.LedgerApiMessage.TransactionReceipt)
            },
        ),
        "Get_Balance_Performative": _reflection.GeneratedProtocolMessageType(
            "Get_Balance_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _LEDGERAPIMESSAGE_GET_BALANCE_PERFORMATIVE,
                "__module__": "ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Get_Balance_Performative)
            },
        ),
        "Get_Raw_Transaction_Performative": _reflection.GeneratedProtocolMessageType(
            "Get_Raw_Transaction_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _LEDGERAPIMESSAGE_GET_RAW_TRANSACTION_PERFORMATIVE,
                "__module__": "ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Get_Raw_Transaction_Performative)
            },
        ),
        "Send_Signed_Transaction_Performative": _reflection.GeneratedProtocolMessageType(
            "Send_Signed_Transaction_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _LEDGERAPIMESSAGE_SEND_SIGNED_TRANSACTION_PERFORMATIVE,
                "__module__": "ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Send_Signed_Transaction_Performative)
            },
        ),
        "Get_Transaction_Receipt_Performative": _reflection.GeneratedProtocolMessageType(
            "Get_Transaction_Receipt_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _LEDGERAPIMESSAGE_GET_TRANSACTION_RECEIPT_PERFORMATIVE,
                "__module__": "ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Get_Transaction_Receipt_Performative)
            },
        ),
        "Balance_Performative": _reflection.GeneratedProtocolMessageType(
            "Balance_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _LEDGERAPIMESSAGE_BALANCE_PERFORMATIVE,
                "__module__": "ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Balance_Performative)
            },
        ),
        "Raw_Transaction_Performative": _reflection.GeneratedProtocolMessageType(
            "Raw_Transaction_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _LEDGERAPIMESSAGE_RAW_TRANSACTION_PERFORMATIVE,
                "__module__": "ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Raw_Transaction_Performative)
            },
        ),
        "Transaction_Digest_Performative": _reflection.GeneratedProtocolMessageType(
            "Transaction_Digest_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _LEDGERAPIMESSAGE_TRANSACTION_DIGEST_PERFORMATIVE,
                "__module__": "ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Transaction_Digest_Performative)
            },
        ),
        "Transaction_Receipt_Performative": _reflection.GeneratedProtocolMessageType(
            "Transaction_Receipt_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _LEDGERAPIMESSAGE_TRANSACTION_RECEIPT_PERFORMATIVE,
                "__module__": "ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Transaction_Receipt_Performative)
            },
        ),
        "Get_State_Performative": _reflection.GeneratedProtocolMessageType(
            "Get_State_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _LEDGERAPIMESSAGE_GET_STATE_PERFORMATIVE,
                "__module__": "ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Get_State_Performative)
            },
        ),
        "State_Performative": _reflection.GeneratedProtocolMessageType(
            "State_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _LEDGERAPIMESSAGE_STATE_PERFORMATIVE,
                "__module__": "ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:aea.valory.ledger_api.v1_0_0.LedgerApiMessage.State_Performative)
            },
        ),
        "Error_Performative": _reflection.GeneratedProtocolMessageType(
            "Error_Performative",
            (_message.Message,),
            {
                "DESCRIPTOR": _LEDGERAPIMESSAGE_ERROR_PERFORMATIVE,
                "__module__": "ledger_api_pb2"
                # @@protoc_insertion_point(class_scope:aea.valory.ledger_api.v1_0_0.LedgerApiMessage.Error_Performative)
            },
        ),
        "DESCRIPTOR": _LEDGERAPIMESSAGE,
        "__module__": "ledger_api_pb2"
        # @@protoc_insertion_point(class_scope:aea.valory.ledger_api.v1_0_0.LedgerApiMessage)
    },
)
_sym_db.RegisterMessage(LedgerApiMessage)
_sym_db.RegisterMessage(LedgerApiMessage.Kwargs)
_sym_db.RegisterMessage(LedgerApiMessage.RawTransaction)
_sym_db.RegisterMessage(LedgerApiMessage.SignedTransaction)
_sym_db.RegisterMessage(LedgerApiMessage.State)
_sym_db.RegisterMessage(LedgerApiMessage.Terms)
_sym_db.RegisterMessage(LedgerApiMessage.TransactionDigest)
_sym_db.RegisterMessage(LedgerApiMessage.TransactionReceipt)
_sym_db.RegisterMessage(LedgerApiMessage.Get_Balance_Performative)
_sym_db.RegisterMessage(LedgerApiMessage.Get_Raw_Transaction_Performative)
_sym_db.RegisterMessage(LedgerApiMessage.Send_Signed_Transaction_Performative)
_sym_db.RegisterMessage(LedgerApiMessage.Get_Transaction_Receipt_Performative)
_sym_db.RegisterMessage(LedgerApiMessage.Balance_Performative)
_sym_db.RegisterMessage(LedgerApiMessage.Raw_Transaction_Performative)
_sym_db.RegisterMessage(LedgerApiMessage.Transaction_Digest_Performative)
_sym_db.RegisterMessage(LedgerApiMessage.Transaction_Receipt_Performative)
_sym_db.RegisterMessage(LedgerApiMessage.Get_State_Performative)
_sym_db.RegisterMessage(LedgerApiMessage.State_Performative)
_sym_db.RegisterMessage(LedgerApiMessage.Error_Performative)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _LEDGERAPIMESSAGE._serialized_start = 52
    _LEDGERAPIMESSAGE._serialized_end = 2746
    _LEDGERAPIMESSAGE_KWARGS._serialized_start = 1205
    _LEDGERAPIMESSAGE_KWARGS._serialized_end = 1229
    _LEDGERAPIMESSAGE_RAWTRANSACTION._serialized_start = 1231
    _LEDGERAPIMESSAGE_RAWTRANSACTION._serialized_end = 1272
    _LEDGERAPIMESSAGE_SIGNEDTRANSACTION._serialized_start = 1274
    _LEDGERAPIMESSAGE_SIGNEDTRANSACTION._serialized_end = 1321
    _LEDGERAPIMESSAGE_STATE._serialized_start = 1323
    _LEDGERAPIMESSAGE_STATE._serialized_end = 1345
    _LEDGERAPIMESSAGE_TERMS._serialized_start = 1347
    _LEDGERAPIMESSAGE_TERMS._serialized_end = 1369
    _LEDGERAPIMESSAGE_TRANSACTIONDIGEST._serialized_start = 1371
    _LEDGERAPIMESSAGE_TRANSACTIONDIGEST._serialized_end = 1418
    _LEDGERAPIMESSAGE_TRANSACTIONRECEIPT._serialized_start = 1420
    _LEDGERAPIMESSAGE_TRANSACTIONRECEIPT._serialized_end = 1469
    _LEDGERAPIMESSAGE_GET_BALANCE_PERFORMATIVE._serialized_start = 1471
    _LEDGERAPIMESSAGE_GET_BALANCE_PERFORMATIVE._serialized_end = 1533
    _LEDGERAPIMESSAGE_GET_RAW_TRANSACTION_PERFORMATIVE._serialized_start = 1535
    _LEDGERAPIMESSAGE_GET_RAW_TRANSACTION_PERFORMATIVE._serialized_end = 1639
    _LEDGERAPIMESSAGE_SEND_SIGNED_TRANSACTION_PERFORMATIVE._serialized_start = 1642
    _LEDGERAPIMESSAGE_SEND_SIGNED_TRANSACTION_PERFORMATIVE._serialized_end = 1775
    _LEDGERAPIMESSAGE_GET_TRANSACTION_RECEIPT_PERFORMATIVE._serialized_start = 1778
    _LEDGERAPIMESSAGE_GET_TRANSACTION_RECEIPT_PERFORMATIVE._serialized_end = 1911
    _LEDGERAPIMESSAGE_BALANCE_PERFORMATIVE._serialized_start = 1913
    _LEDGERAPIMESSAGE_BALANCE_PERFORMATIVE._serialized_end = 1971
    _LEDGERAPIMESSAGE_RAW_TRANSACTION_PERFORMATIVE._serialized_start = 1973
    _LEDGERAPIMESSAGE_RAW_TRANSACTION_PERFORMATIVE._serialized_end = 2092
    _LEDGERAPIMESSAGE_TRANSACTION_DIGEST_PERFORMATIVE._serialized_start = 2095
    _LEDGERAPIMESSAGE_TRANSACTION_DIGEST_PERFORMATIVE._serialized_end = 2223
    _LEDGERAPIMESSAGE_TRANSACTION_RECEIPT_PERFORMATIVE._serialized_start = 2226
    _LEDGERAPIMESSAGE_TRANSACTION_RECEIPT_PERFORMATIVE._serialized_end = 2357
    _LEDGERAPIMESSAGE_GET_STATE_PERFORMATIVE._serialized_start = 2360
    _LEDGERAPIMESSAGE_GET_STATE_PERFORMATIVE._serialized_end = 2507
    _LEDGERAPIMESSAGE_STATE_PERFORMATIVE._serialized_start = 2509
    _LEDGERAPIMESSAGE_STATE_PERFORMATIVE._serialized_end = 2618
    _LEDGERAPIMESSAGE_ERROR_PERFORMATIVE._serialized_start = 2620
    _LEDGERAPIMESSAGE_ERROR_PERFORMATIVE._serialized_end = 2730
# @@protoc_insertion_point(module_scope)
