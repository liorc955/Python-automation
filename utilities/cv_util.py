import csv


def read_data(path):
    file = open(path)
    csvreader = csv.reader(file)
    next(csvreader)  # Skip the first row
    rows = []
    for row in csvreader:
        rows.append(row)
    return rows
