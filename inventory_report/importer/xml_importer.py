from inventory_report.importer.importer import Importer
import xmltodict
import os


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path: str) -> str:
        _, extension = os.path.splitext(path)

        if not extension == ".xml":
            raise ValueError("Arquivo inválido")
        try:
            with open(path, encoding="utf-8") as file:
                products = xmltodict.parse(file.read())
                data = products["dataset"]["record"]
                return data
        except FileNotFoundError:
            print('Arquivo não encontrado')
