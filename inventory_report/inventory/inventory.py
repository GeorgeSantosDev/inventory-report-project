from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

import os


class Inventory:
    @classmethod
    def import_data(cls, path: str, report_type: str) -> str:
        _, extension = os.path.splitext(path)
        data = []

        if extension == ".csv":
            data = CsvImporter.import_data(path)
        elif extension == ".json":
            data = JsonImporter.import_data(path)
        else:
            data = XmlImporter.import_data(path)

        report = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate,
        }

        return report[report_type](data)
