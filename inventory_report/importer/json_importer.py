from inventory_report.importer.importer import Importer
import json
import os


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path: str) -> str:
        _, extension = os.path.splitext(path)

        if not extension == ".json":
            raise ValueError("Arquivo inválido")

        try:
            with open(path, encoding="utf-8") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print('Arquivo não encontrado')
