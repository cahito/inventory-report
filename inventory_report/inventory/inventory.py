from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def import_data(cls, path, tipo_relatorio):
        dados_relatorio = list()

        if path.endswith(".json"):
            relatorio = json.load(open(path, "r"))
            dados_relatorio = list(relatorio)
        elif path.endswith('.xml'):
            with open(path) as file:
                relatorio = xmltodict.parse(file.read())
                dados_relatorio = relatorio['dataset']['record']
        else:
            with open(path, encoding="utf-8") as file:
                relatorio = csv.DictReader(file, delimiter=",", quotechar='"')
                dados_relatorio = list(relatorio)

        if tipo_relatorio == "simples":
            return SimpleReport.generate(dados_relatorio)

        return CompleteReport.generate(dados_relatorio)
