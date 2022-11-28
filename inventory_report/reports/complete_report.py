from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

    @classmethod
    def generate(cls, products):
        simple_report = super().generate(products)
        empresas_com_produtos = super().quantos_produtos_por_empresa(products)

        complete_report = ""

        for key, value in empresas_com_produtos.items():
            complete_report += f"- {key}: {value}\n"

        return (
            f"{simple_report}\n"
            "Produtos estocados por empresa:\n"
            f"{complete_report}"
        )
