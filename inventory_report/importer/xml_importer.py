from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path: str) -> str:
        try:
            with open(path, encoding="utf-8") as file:
                products = xmltodict.parse(file.read())
                data = products["dataset"]["record"]
                return data
        except ValueError:
            print("Arquivo inválido")
