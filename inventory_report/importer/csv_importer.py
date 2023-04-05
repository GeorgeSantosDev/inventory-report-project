from inventory_report.importer.importer import Importer
import csv
import os


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path: str) -> str:
        _, extension = os.path.splitext(path)

        if not extension == ".csv":
            raise ValueError("Arquivo inválido")

        try:
            with open(path, encoding="utf-8") as file:
                products = csv.DictReader(file, delimiter=",", quotechar='"')
                data = [product for product in products]
                return data
        except FileNotFoundError:
            print('Arquivo não encontrado')
