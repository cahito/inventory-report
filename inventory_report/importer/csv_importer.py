from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path: str):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")

        with open(path, encoding="utf-8") as file:
            relatorio = csv.DictReader(file, delimiter=",", quotechar='"')
            dados_relatorio = list(relatorio)
            return dados_relatorio
