from typing import Iterable, Literal
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer: Importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def get_report(self, tipo_relatorio: Literal["simples", "completo"]):
        if tipo_relatorio == "simples":
            return SimpleReport.generate(self.data)
        elif tipo_relatorio == "completo":
            return CompleteReport.generate(self.data)

    def import_data(
        self, path: str, tipo_relatorio: Literal["simples", "completo"]
    ):
        self.data += self.importer.import_data(path)
        return self.get_report(tipo_relatorio)
