from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path: str) -> str:
        try:
            with open(path, encoding="utf-8") as file:
                products = csv.DictReader(file, delimiter=",", quotechar='"')
                data = [product for product in products]
                return data
        except ValueError:
            print("Arquivo inválido")
