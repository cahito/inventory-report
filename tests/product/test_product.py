import pytest
from inventory_report.inventory.product import Product


@pytest.fixture
def data():
    return {
        "id": 12,
        "nome_do_produto": "Produto teste",
        "nome_da_empresa": "Empresa teste",
        "data_de_fabricacao": "22-11-2022",
        "data_de_validade": "22-11-2023",
        "numero_de_serie": "Quinta série",
        "instrucoes_de_armazenamento": "Guarde em algum lugar apropriado",
    }


def test_cria_produto(data):
    result = Product(**data)
    assert type(result) == Product
    assert result.id == data["id"]
    assert result.nome_do_produto == data["nome_do_produto"]
    assert result.nome_da_empresa == data["nome_da_empresa"]
    assert result.data_de_fabricacao == data["data_de_fabricacao"]
    assert result.data_de_validade == data["data_de_validade"]
    assert result.numero_de_serie == data["numero_de_serie"]
    assert (
        result.instrucoes_de_armazenamento
        == data["instrucoes_de_armazenamento"]
    )
