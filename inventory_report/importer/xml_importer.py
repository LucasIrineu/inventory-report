from inventory_report.importer.importer import Importer
import xmltodict
import os


class xmlImporter(Importer):
    @staticmethod
    def import_data(path: str):
        file_extension = os.path.splitext(path)[1]

        if file_extension == ".xml":
            with open(path, encoding="utf-8") as file:
                file_reader = xmltodict.parse(file.read())
                result = file_reader["dataset"]["record"]
            return result
        else:
            ValueError("Arquivo inválido")
