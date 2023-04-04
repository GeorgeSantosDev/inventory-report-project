from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @classmethod
    def import_data(cls, path: str, type: str) -> str:
        try:
            with open(path, encoding="utf-8") as file:
                data = csv.DictReader(file, delimiter=",", quotechar='"')
                products = [product for product in data]
                print(products)
                if type == "simples":
                    return SimpleReport.generate(products)
                else:
                    return CompleteReport.generate(products)

        except FileNotFoundError:
            print("Arquivo não encontrado")
