import pytest
import requests
from Atividade import *
from unittest.mock import MagicMock

#TESTES
@pytest.fixture
def banco_simulado():
    banco = BancoDeDados()
    banco.buscar_pedido = MagicMock(return_value={"id": 1, "cliente": "João"})
    return banco

@pytest.fixture
def mock_resposta_api(mocker):
    mock_resposta = mocker.patch('requests.get')
    mock_resposta.return_value.json.return_value = [
        {"preco": 100, "quantidade": 2},
        {"preco": 50, "quantidade": 3}
    ]
    return mock_resposta

def test_calcular_valor_total(mock_resposta_api):
    pedido_id = 1
    total = calcular_valor_total(pedido_id)
    assert total == 350 
def test_obter_pedido_com_valor_total(banco_simulado, mock_resposta_api):
    pedido_id = 1
    pedido_completo = obter_pedido_com_valor_total(pedido_id, banco_simulado)
    assert pedido_completo["id"] == pedido_id
    assert pedido_completo["cliente"] == "João"
    assert pedido_completo["valor_total"] == 350