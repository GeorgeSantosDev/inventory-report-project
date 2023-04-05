from inventory_report.importer.importer import Importer

import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path: str) -> str:
        try:
            with open(path, encoding="utf-8") as file:
                data = json.load(file)
                return data
        except ValueError:
            print("Arquivo inválido")
