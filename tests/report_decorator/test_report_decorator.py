import pytest
from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


@pytest.fixture
def data():
    return [
        {
            "id": 1,
            "nome_da_empresa": "FarmaConde",
            "data_de_fabricacao": "2020-08-12",
            "data_de_validade": "2023-08-11",
        },
        {
            "id": 2,
            "nome_da_empresa": "Petybon",
            "data_de_fabricacao": "2022-09-21",
            "data_de_validade": "2023-09-21",
        },
        {
            "id": 3,
            "nome_da_empresa": "Johnson&Johnson",
            "data_de_fabricacao": "2021-04-05",
            "data_de_validade": "2024-04-05",
        },
    ]


def test_decorar_relatorio(data):
    relatorio_colorido = ColoredReport(SimpleReport)
    relatorio = relatorio_colorido.generate(data)

    assert "\033[32mData de fabricação mais antiga:\033[0m" in relatorio
    assert "\033[36m2020-08-12\033[0m" in relatorio

    assert "\033[32mData de validade mais próxima:\033[0m" in relatorio
    assert "\033[36m2023-08-11\033[0m" in relatorio

    assert "\033[32mEmpresa com mais produtos:\033[0m" in relatorio
    assert "\033[31mFarmaConde\033[0m" in relatorio
