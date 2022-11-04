import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith('json'):
            with open(path) as json_file:
                return json.loads(json_file.read())
        raise ValueError("Arquivo inválido")
