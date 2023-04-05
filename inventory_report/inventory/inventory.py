from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict
import os


def read(path: str):
    file_extension = os.path.splitext(path)[1]
    with open(path, encoding="utf-8") as file:
        if file_extension == '.csv':
            file_reader = csv.DictReader(file)
            result = [row for row in file_reader]
            return result
        elif file_extension == '.json':
            file_reader = json.load(file)
            result = [row for row in file_reader]
            return result
        if file_extension == '.xml':
            file_reader = xmltodict.parse(file.read())
            result = file_reader['dataset']['record']
            return result


class Inventory:
    def import_data(path: str, type: str):
        data = read(path)

        if type == 'simples':
            return SimpleReport.generate(data)
        elif type == 'completo':
            return CompleteReport.generate(data)
