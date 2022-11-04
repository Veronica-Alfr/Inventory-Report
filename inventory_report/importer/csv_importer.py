import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod

    def import_data(cls, path):
        if path.endswith("csv"):
            with open(path) as csv_file:
                return list(csv.DictReader(csv_file))
        raise ValueError("Arquivo inválido")
