from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path: str):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")

        relatorio = json.load(open(path, "r"))
        dados_relatorio = list(relatorio)
        return dados_relatorio
