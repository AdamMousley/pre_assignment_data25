import csv

def read_csv(filename):
    rows = []
    with open(filename, 'r', encoding='utf8') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
    return rows

def select_row_elements(filename):
    missing_data = []
    complete_data = read_csv(filename)
    for row in read_csv(filename):
        for i in row:
            if i == '':
                missing_data.append(row)
                complete_data.remove(row)
                break
    return missing_data,complete_data

def remove_duplicates(data_list):
    no_duplicates = []
    for i in data_list:
        if i not in no_duplicates:
            no_duplicates.append(i)
    return no_duplicates

