from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(path: str):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            relatorio = xmltodict.parse(file.read())
            dados_relatorio = relatorio["dataset"]["record"]
            return dados_relatorio
