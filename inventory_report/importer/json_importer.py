from inventory_report.importer.importer import Importer
import json
import os


class JsonImporter(Importer):
    @staticmethod
    def import_data(path: str):
        file_extension = os.path.splitext(path)[1]

        if file_extension == '.json':
            with open(path, encoding="utf-8") as file:
                if file_extension == ".json":
                    file_reader = json.load(file)
                    return file_reader

        else:
            raise ValueError('Arquivo inválido')
