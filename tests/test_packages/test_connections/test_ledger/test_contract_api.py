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

"""This module contains the tests of the ledger API connection for the contract APIs."""
import asyncio
import logging
import unittest.mock
from typing import cast

import pytest

from aea.common import Address
from aea.helpers.transaction.base import RawMessage, RawTransaction, State
from aea.mail.base import Envelope
from aea.multiplexer import ConnectionStatus
from aea.protocols.base import Message
from aea.protocols.dialogue.base import Dialogue

from packages.fetchai.connections.ledger.contract_dispatcher import (
    ContractApiRequestDispatcher,
)
from packages.fetchai.protocols.contract_api.dialogues import ContractApiDialogue
from packages.fetchai.protocols.contract_api.dialogues import (
    ContractApiDialogues as BaseContractApiDialogues,
)
from packages.fetchai.protocols.contract_api.message import ContractApiMessage

from tests.conftest import ETHEREUM, ETHEREUM_ADDRESS_ONE


class ContractApiDialogues(BaseContractApiDialogues):
    """This class keeps track of all contract_api dialogues."""

    def __init__(self, agent_address: str) -> None:
        """
        Initialize dialogues.

        :param agent_address: the address of the agent for whom dialogues are maintained
        :return: None
        """

        def role_from_first_message(
            message: Message, receiver_address: Address
        ) -> Dialogue.Role:
            """Infer the role of the agent from an incoming/outgoing first message

            :param message: an incoming/outgoing first message
            :param receiver_address: the address of the receiving agent
            :return: The role of the agent
            """
            return ContractApiDialogue.Role.AGENT

        BaseContractApiDialogues.__init__(
            self,
            agent_address=agent_address,
            role_from_first_message=role_from_first_message,
        )


@pytest.mark.integration
@pytest.mark.ledger
@pytest.mark.asyncio
async def test_erc1155_get_deploy_transaction(erc1155_contract, ledger_apis_connection):
    """Test get state with contract erc1155."""
    # TODO to fix
    address = ETHEREUM_ADDRESS_ONE
    contract_api_dialogues = ContractApiDialogues(address)
    request, contract_api_dialogue = contract_api_dialogues.create(
        counterparty=str(ledger_apis_connection.connection_id),
        performative=ContractApiMessage.Performative.GET_DEPLOY_TRANSACTION,
        ledger_id=ETHEREUM,
        contract_id="fetchai/erc1155:0.9.0",
        callable="get_deploy_transaction",
        kwargs=ContractApiMessage.Kwargs({"deployer_address": address}),
    )
    envelope = Envelope(
        to=request.to,
        sender=request.sender,
        protocol_id=request.protocol_id,
        message=request,
    )

    await ledger_apis_connection.send(envelope)
    await asyncio.sleep(0.01)
    response = await ledger_apis_connection.receive()

    assert response is not None
    assert type(response.message) == ContractApiMessage
    response_message = cast(ContractApiMessage, response.message)
    assert (
        response_message.performative == ContractApiMessage.Performative.RAW_TRANSACTION
    ), "Error: {}".format(response_message.message)
    response_dialogue = contract_api_dialogues.update(response_message)
    assert response_dialogue == contract_api_dialogue
    assert type(response_message.raw_transaction) == RawTransaction
    assert response_message.raw_transaction.ledger_id == ETHEREUM
    assert len(response.message.raw_transaction.body) == 6
    assert len(response.message.raw_transaction.body["data"]) > 0


@pytest.mark.integration
@pytest.mark.ledger
@pytest.mark.asyncio
async def test_erc1155_get_raw_transaction(erc1155_contract, ledger_apis_connection):
    """Test get state with contract erc1155."""
    address = ETHEREUM_ADDRESS_ONE
    contract_address = "0x250A2aeb3eB84782e83365b4c42dbE3CDA9920e4"
    contract_api_dialogues = ContractApiDialogues(address)
    request, contract_api_dialogue = contract_api_dialogues.create(
        counterparty=str(ledger_apis_connection.connection_id),
        performative=ContractApiMessage.Performative.GET_RAW_TRANSACTION,
        ledger_id=ETHEREUM,
        contract_id="fetchai/erc1155:0.9.0",
        contract_address=contract_address,
        callable="get_create_batch_transaction",
        kwargs=ContractApiMessage.Kwargs(
            {"deployer_address": address, "token_ids": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
        ),
    )
    envelope = Envelope(
        to=request.to,
        sender=request.sender,
        protocol_id=request.protocol_id,
        message=request,
    )

    await ledger_apis_connection.send(envelope)
    await asyncio.sleep(0.01)
    response = await ledger_apis_connection.receive()

    assert response is not None
    assert type(response.message) == ContractApiMessage
    response_message = cast(ContractApiMessage, response.message)
    assert (
        response_message.performative == ContractApiMessage.Performative.RAW_TRANSACTION
    ), "Error: {}".format(response_message.message)

    response_dialogue = contract_api_dialogues.update(response_message)
    assert response_dialogue == contract_api_dialogue
    assert type(response_message.raw_transaction) == RawTransaction
    assert response_message.raw_transaction.ledger_id == ETHEREUM
    assert len(response.message.raw_transaction.body) == 7
    assert len(response.message.raw_transaction.body["data"]) > 0


@pytest.mark.integration
@pytest.mark.ledger
@pytest.mark.asyncio
async def test_erc1155_get_raw_message(erc1155_contract, ledger_apis_connection):
    """Test get state with contract erc1155."""
    address = ETHEREUM_ADDRESS_ONE
    contract_address = "0x250A2aeb3eB84782e83365b4c42dbE3CDA9920e4"
    contract_api_dialogues = ContractApiDialogues(address)
    request, contract_api_dialogue = contract_api_dialogues.create(
        counterparty=str(ledger_apis_connection.connection_id),
        performative=ContractApiMessage.Performative.GET_RAW_MESSAGE,
        ledger_id=ETHEREUM,
        contract_id="fetchai/erc1155:0.9.0",
        contract_address=contract_address,
        callable="get_hash_single",
        kwargs=ContractApiMessage.Kwargs(
            {
                "from_address": address,
                "to_address": address,
                "token_id": 1,
                "from_supply": 10,
                "to_supply": 0,
                "value": 0,
                "trade_nonce": 1,
            }
        ),
    )
    envelope = Envelope(
        to=request.to,
        sender=request.sender,
        protocol_id=request.protocol_id,
        message=request,
    )

    await ledger_apis_connection.send(envelope)
    await asyncio.sleep(0.01)
    response = await ledger_apis_connection.receive()

    assert response is not None
    assert type(response.message) == ContractApiMessage
    response_message = cast(ContractApiMessage, response.message)
    assert (
        response_message.performative == ContractApiMessage.Performative.RAW_MESSAGE
    ), "Error: {}".format(response_message.message)
    response_dialogue = contract_api_dialogues.update(response_message)
    assert response_dialogue == contract_api_dialogue
    assert type(response_message.raw_message) == RawMessage
    assert response_message.raw_message.ledger_id == ETHEREUM
    assert type(response.message.raw_message.body) == bytes


@pytest.mark.integration
@pytest.mark.ledger
@pytest.mark.asyncio
async def test_erc1155_get_state(erc1155_contract, ledger_apis_connection):
    """Test get state with contract erc1155."""
    address = ETHEREUM_ADDRESS_ONE
    contract_address = "0x250A2aeb3eB84782e83365b4c42dbE3CDA9920e4"
    contract_api_dialogues = ContractApiDialogues(address)
    token_id = 1
    request, contract_api_dialogue = contract_api_dialogues.create(
        counterparty=str(ledger_apis_connection.connection_id),
        performative=ContractApiMessage.Performative.GET_STATE,
        ledger_id=ETHEREUM,
        contract_id="fetchai/erc1155:0.9.0",
        contract_address=contract_address,
        callable="get_balance",
        kwargs=ContractApiMessage.Kwargs(
            {"agent_address": address, "token_id": token_id}
        ),
    )
    envelope = Envelope(
        to=request.to,
        sender=request.sender,
        protocol_id=request.protocol_id,
        message=request,
    )

    await ledger_apis_connection.send(envelope)
    await asyncio.sleep(0.01)
    response = await ledger_apis_connection.receive()

    assert response is not None
    assert type(response.message) == ContractApiMessage
    response_message = cast(ContractApiMessage, response.message)
    assert (
        response_message.performative == ContractApiMessage.Performative.STATE
    ), "Error: {}".format(response_message.message)
    response_dialogue = contract_api_dialogues.update(response_message)
    assert response_dialogue == contract_api_dialogue
    assert type(response_message.state) == State
    assert response_message.state.ledger_id == ETHEREUM
    result = response_message.state.body.get("balance", None)
    expected_result = {token_id: 0}
    assert result is not None and result == expected_result


@pytest.mark.asyncio
async def test_run_async():
    """Test run async error handled."""
    # for pydocstyle
    def _raise():
        raise Exception("Expected")

    contract_api_dialogues = ContractApiDialogues("address")
    request, dialogue = contract_api_dialogues.create(
        counterparty="str(ledger_apis_connection.connection_id)",
        performative=ContractApiMessage.Performative.GET_RAW_TRANSACTION,
        ledger_id=ETHEREUM,
        contract_id="fetchai/erc1155:0.9.0",
        contract_address="test addr",
        callable="get_create_batch_transaction",
        kwargs=ContractApiMessage.Kwargs(
            {
                "deployer_address": "test_addr",
                "token_ids": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            }
        ),
    )
    api = None
    msg = await ContractApiRequestDispatcher(ConnectionStatus()).run_async(
        _raise, api, request, dialogue
    )
    assert msg.performative == ContractApiMessage.Performative.ERROR


@pytest.mark.asyncio
async def test_get_handler():
    """Test failed to get handler."""
    with pytest.raises(Exception, match="Performative not recognized."):
        ContractApiRequestDispatcher(ConnectionStatus()).get_handler(
            ContractApiMessage.Performative.ERROR
        )


@pytest.mark.integration
@pytest.mark.ledger
@pytest.mark.asyncio
async def test_callable_wrong_number_of_arguments_api_and_contract_address(
    erc1155_contract, ledger_apis_connection
):
    """
    Test a contract callable with wrong number of arguments.

    Test the case of either GET_STATE, GET_RAW_MESSAGE or GET_RAW_TRANSACTION.
    """
    address = ETHEREUM_ADDRESS_ONE
    contract_api_dialogues = ContractApiDialogues(address)
    token_id = 1
    contract_address = "0x250A2aeb3eB84782e83365b4c42dbE3CDA9920e4"
    request, _ = contract_api_dialogues.create(
        counterparty=str(ledger_apis_connection.connection_id),
        performative=ContractApiMessage.Performative.GET_STATE,
        ledger_id=ETHEREUM,
        contract_id="fetchai/erc1155:0.9.0",
        contract_address=contract_address,
        callable="get_balance",
        kwargs=ContractApiMessage.Kwargs(
            {"agent_address": address, "token_id": token_id}
        ),
    )
    envelope = Envelope(
        to=request.to,
        sender=request.sender,
        protocol_id=request.protocol_id,
        message=request,
    )

    with unittest.mock.patch(
        "inspect.getfullargspec", return_value=unittest.mock.MagicMock(args=[None])
    ):
        with unittest.mock.patch.object(
            ledger_apis_connection._logger, "error"
        ) as mock_logger:
            await ledger_apis_connection.send(envelope)
            await asyncio.sleep(0.01)
            response = await ledger_apis_connection.receive()
            mock_logger.assert_any_call(
                "Expected two or more positional arguments, got 1"
            )
            assert (
                response.message.performative == ContractApiMessage.Performative.ERROR
            )
            assert (
                response.message.message
                == "Expected two or more positional arguments, got 1"
            )


@pytest.mark.integration
@pytest.mark.ledger
@pytest.mark.asyncio
async def test_callable_wrong_number_of_arguments_apis(
    erc1155_contract, ledger_apis_connection
):
    """
    Test a contract callable with wrong number of arguments.

    Test the case of either GET_DEPLOY_TRANSACTION.
    """
    address = ETHEREUM_ADDRESS_ONE
    contract_api_dialogues = ContractApiDialogues(address)
    request, _ = contract_api_dialogues.create(
        counterparty=str(ledger_apis_connection.connection_id),
        performative=ContractApiMessage.Performative.GET_DEPLOY_TRANSACTION,
        ledger_id=ETHEREUM,
        contract_id="fetchai/erc1155:0.9.0",
        callable="get_deploy_transaction",
        kwargs=ContractApiMessage.Kwargs({}),
    )
    envelope = Envelope(
        to=request.to,
        sender=request.sender,
        protocol_id=request.protocol_id,
        message=request,
    )

    with unittest.mock.patch(
        "inspect.getfullargspec", return_value=unittest.mock.MagicMock(args=[])
    ):
        with unittest.mock.patch.object(
            ledger_apis_connection._contract_dispatcher, "_call_stub", return_value=None
        ):
            with unittest.mock.patch.object(
                ledger_apis_connection._contract_dispatcher.logger, "error"
            ) as mock_logger:
                await ledger_apis_connection.send(envelope)
                await asyncio.sleep(0.01)
                response = await ledger_apis_connection.receive()
                mock_logger.assert_any_call(
                    "Expected one or more positional arguments, got 0"
                )
                assert (
                    response.message.performative
                    == ContractApiMessage.Performative.ERROR
                )
                assert (
                    response.message.message
                    == "Expected one or more positional arguments, got 0"
                )


@pytest.mark.integration
@pytest.mark.ledger
@pytest.mark.asyncio
async def test_callable_wrong_number_of_arguments_apis_method_call(
    erc1155_contract, ledger_apis_connection, caplog
):
    """
    Test a contract callable with wrong number of arguments.

    Test the case of either GET_DEPLOY_TRANSACTION.
    """
    address = ETHEREUM_ADDRESS_ONE
    contract_api_dialogues = ContractApiDialogues(address)
    request, _ = contract_api_dialogues.create(
        counterparty=str(ledger_apis_connection.connection_id),
        performative=ContractApiMessage.Performative.GET_DEPLOY_TRANSACTION,
        ledger_id=ETHEREUM,
        contract_id="fetchai/erc1155:0.9.0",
        callable="get_deploy_transaction",
        kwargs=ContractApiMessage.Kwargs({}),
    )
    envelope = Envelope(
        to=request.to,
        sender=request.sender,
        protocol_id=request.protocol_id,
        message=request,
    )

    with unittest.mock.patch.object(
        ledger_apis_connection._contract_dispatcher, "_call_stub", return_value=None
    ):
        with caplog.at_level(logging.DEBUG, "aea.packages.fetchai.connections.ledger"):
            await ledger_apis_connection.send(envelope)
            await asyncio.sleep(0.01)
            assert (
                "An error occurred while processing the contract api request: 'get_deploy_transaction() missing 1 required positional argument: 'deployer_address''."
                in caplog.text
            )


@pytest.mark.integration
@pytest.mark.ledger
@pytest.mark.asyncio
async def test_callable_generic_error(erc1155_contract, ledger_apis_connection):
    """Test error messages when an exception is raised while processing the request."""
    address = ETHEREUM_ADDRESS_ONE
    contract_api_dialogues = ContractApiDialogues(address)
    token_id = 1
    contract_address = "0x250A2aeb3eB84782e83365b4c42dbE3CDA9920e4"
    request, _ = contract_api_dialogues.create(
        counterparty=str(ledger_apis_connection.connection_id),
        performative=ContractApiMessage.Performative.GET_STATE,
        ledger_id=ETHEREUM,
        contract_id="fetchai/erc1155:0.9.0",
        contract_address=contract_address,
        callable="get_balance",
        kwargs=ContractApiMessage.Kwargs(
            {"agent_address": address, "token_id": token_id}
        ),
    )
    envelope = Envelope(
        to=request.to,
        sender=request.sender,
        protocol_id=request.protocol_id,
        message=request,
    )

    with unittest.mock.patch(
        "inspect.getfullargspec", side_effect=Exception("Generic error")
    ):
        with unittest.mock.patch.object(
            ledger_apis_connection._logger, "error"
        ) as mock_logger:
            await ledger_apis_connection.send(envelope)
            await asyncio.sleep(0.01)
            response = await ledger_apis_connection.receive()
            mock_logger.assert_any_call(
                "An error occurred while processing the contract api request: 'Generic error'."
            )
            assert (
                response.message.performative == ContractApiMessage.Performative.ERROR
            )
            assert response.message.message == "Generic error"


@pytest.mark.integration
@pytest.mark.ledger
@pytest.mark.asyncio
async def test_callable_cannot_find(erc1155_contract, ledger_apis_connection, caplog):
    """Test error messages when an exception is raised while processing the request."""
    address = ETHEREUM_ADDRESS_ONE
    contract_api_dialogues = ContractApiDialogues(address)
    token_id = 1
    contract_address = "0x250A2aeb3eB84782e83365b4c42dbE3CDA9920e4"
    request, _ = contract_api_dialogues.create(
        counterparty=str(ledger_apis_connection.connection_id),
        performative=ContractApiMessage.Performative.GET_STATE,
        ledger_id=ETHEREUM,
        contract_id="fetchai/erc1155:0.9.0",
        contract_address=contract_address,
        callable="unknown_callable",
        kwargs=ContractApiMessage.Kwargs(
            {"agent_address": address, "token_id": token_id}
        ),
    )
    envelope = Envelope(
        to=request.to,
        sender=request.sender,
        protocol_id=request.protocol_id,
        message=request,
    )

    with caplog.at_level(logging.DEBUG, "aea.packages.fetchai.connections.ledger"):
        await ledger_apis_connection.send(envelope)
        await asyncio.sleep(0.01)
        assert f"Cannot find {request.callable} in contract" in caplog.text
