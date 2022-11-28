from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv


class Inventory:
    @classmethod
    def import_data(cls, path, tipo_relatorio):
        with open(path, encoding='utf-8') as file:
            relatorio = csv.DictReader(file, delimiter=',', quotechar='"')
            dados_relatorio = list(relatorio)

        if tipo_relatorio == 'simples':
            return SimpleReport.generate(dados_relatorio)

        return CompleteReport.generate(dados_relatorio)
