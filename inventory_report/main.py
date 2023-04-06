from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

import os
import sys

if len(sys.argv) != 2:
    raise ValueError(sys.stderr.write("Verifique os argumentos"))
print('OLLHAAAAAAAAAAAAAAAAAAA AQUI', len(sys.argv))
importers = {
    ".csv": CsvImporter,
    ".json": JsonImporter,
    ".xml": XmlImporter,
}

report_types = {
    "simples": SimpleReport,
    "completo": CompleteReport
}


def main():
    try:
        _, path, report_type = sys.argv
        _, extension = os.path.splitext(path)

        if extension not in importers:
            raise ValueError("Arquivo inválido")

        inventory = InventoryRefactor(importers[extension])
        data = inventory.import_data(path, report_type)

        sys.stdout.write(report_types[report_type].generate(data))
    except ValueError:
        sys.stderr.write("Verifique os argumentos\n")
