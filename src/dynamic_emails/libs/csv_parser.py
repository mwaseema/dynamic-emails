import csv
from os import path


def parse_file(csv_path):
    data = []
    with open(csv_path, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data


def get_csv_data(csv_path):
    assert path.isfile(csv_path) and path.splitext(path.basename(csv_path))[
        1].lower() == '.csv', "Given CSV path should lead to a .csv file"

    data = parse_file(csv_path)
    return data
