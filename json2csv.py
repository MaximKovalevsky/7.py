import json
import csv
import sys
import os

def json_to_csv(json_file):

    with open(json_file, 'r') as file:
        data = json.load(file)

    csv_file = os.path.splitext(json_file)[0] + '.csv'

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(data[0].keys())

        for item in data:
            writer.writerow(item.values())

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Формат для работы программы: python json2csv.py example.json.')
    else:
        json_file = sys.argv[1]
        json_to_csv(json_file)
