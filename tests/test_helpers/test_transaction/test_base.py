# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This module contains the tests for the base module."""

from aea.helpers.transaction.base import (
    RawMessage,
    RawTransaction,
    SignedTransaction,
    Terms,
    TransactionReceipt,
)


def test_init_terms():
    """Test the terms object initialization."""
    ledger_id = "some_ledger"
    sender_addr = "SenderAddress"
    counterparty_addr = "CounterpartyAddress"
    amount_by_currency_id = {"FET": -10}
    quantities_by_good_id = {"good_1": 20}
    is_sender_payable_tx_fee = True
    nonce = "somestring"
    terms = Terms(
        ledger_id=ledger_id,
        sender_address=sender_addr,
        counterparty_address=counterparty_addr,
        amount_by_currency_id=amount_by_currency_id,
        quantities_by_good_id=quantities_by_good_id,
        is_sender_payable_tx_fee=is_sender_payable_tx_fee,
        nonce=nonce,
    )
    assert terms.ledger_id == ledger_id
    assert terms.sender_address == sender_addr
    assert terms.counterparty_address == counterparty_addr
    assert terms.amount_by_currency_id == amount_by_currency_id
    assert terms.quantities_by_good_id == quantities_by_good_id
    assert terms.is_sender_payable_tx_fee == is_sender_payable_tx_fee
    assert terms.nonce == nonce
    assert (
        str(terms)
        == "Terms: ledger_id=some_ledger, sender_address=SenderAddress, counterparty_address=CounterpartyAddress, amount_by_currency_id={'FET': -10}, quantities_by_good_id={'good_1': 20}, is_sender_payable_tx_fee=True, nonce=somestring, fee=None"
    )
    assert terms == terms


def test_init_raw_transaction():
    """Test the raw_transaction object initialization."""
    ledger_id = "some_ledger"
    body = "body"
    rt = RawTransaction(ledger_id, body)
    assert rt.ledger_id == ledger_id
    assert rt.body == body
    assert str(rt) == "RawTransaction: ledger_id=some_ledger, body=body"
    assert rt == rt


def test_init_raw_message():
    """Test the raw_message object initialization."""
    ledger_id = "some_ledger"
    body = "body"
    rm = RawMessage(ledger_id, body)
    assert rm.ledger_id == ledger_id
    assert rm.body == body
    assert not rm.is_deprecated_mode
    assert (
        str(rm)
        == "RawMessage: ledger_id=some_ledger, body=body, is_deprecated_mode=False"
    )
    assert rm == rm


def test_init_signed_transaction():
    """Test the signed_transaction object initialization."""
    ledger_id = "some_ledger"
    body = "body"
    st = SignedTransaction(ledger_id, body)
    assert st.ledger_id == ledger_id
    assert st.body == body
    assert str(st) == "SignedTransaction: ledger_id=some_ledger, body=body"
    assert st == st


def test_init_transaction_receipt():
    """Test the transaction_receipt object initialization."""
    ledger_id = "some_ledger"
    receipt = "receipt"
    transaction = "transaction"
    tr = TransactionReceipt(ledger_id, receipt, transaction)
    assert tr.ledger_id == ledger_id
    assert tr.receipt == receipt
    assert tr.transaction == transaction
    assert (
        str(tr)
        == "TransactionReceipt: ledger_id=some_ledger, receipt=receipt, transaction=transaction"
    )
    assert tr == tr
