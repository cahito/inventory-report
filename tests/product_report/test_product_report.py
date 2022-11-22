import pytest
from inventory_report.inventory.product import Product


@pytest.fixture
def data():
    return [
        {
            "id": 12,
            "nome_do_produto": "Produto teste",
            "nome_da_empresa": "Empresa teste",
            "data_de_fabricacao": "22-11-2022",
            "data_de_validade": "22-11-2023",
            "numero_de_serie": "Quinta série",
            "instrucoes_de_armazenamento": "Guarde em algum lugar apropriado",
        },
        "O produto Produto teste"
        " fabricado em 22-11-2022"
        " por Empresa teste com validade"
        " até 22-11-2023 precisa ser"
        " armazenado Guarde em algum lugar apropriado.",
    ]


def test_relatorio_produto(data):
    mock_product, expected = data
    result = Product(**mock_product)
    assert str(result) == expected
