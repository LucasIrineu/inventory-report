from inventory_report.importer.importer import Importer
import csv
import os


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str):
        file_extension = os.path.splitext(path)[1]

        if file_extension == '.csv':
            with open(path, encoding="utf-8") as file:
                if file_extension == ".csv":
                    file_reader = csv.DictReader(file)
                    result = [row for row in file_reader]
                    return result

        else:
            ValueError('Arquivo inválido')
