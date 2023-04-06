from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    def __init__(self, importer) -> None:
        self.importer = importer
        self.data = []

    def import_data(self, path: str, report_type) -> None:
        new_data = self.importer.import_data(path)
        self.data = [*self.data, *new_data]

        return self.data

    def __iter__(self):
        return InventoryIterator(self.data)
