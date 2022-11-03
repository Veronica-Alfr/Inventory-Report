import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, report):
        data = cls.change_path(path)
        if report == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)

    @classmethod
    def change_path(cls, path):
        if path.endswith('csv'):
            with open(path) as csv_file:
                return list(csv.DictReader(csv_file))
        elif path.endswith('json'):
            with open(path) as json_file:
                return json.loads(json_file.read())
        elif path.endswith('xml'):
            with open(path) as xml_file:
                return xmltodict.parse(xml_file.read())["dataset"]["record"]
