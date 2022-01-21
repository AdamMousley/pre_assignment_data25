import csv
from unidecode import unidecode


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

# def remove_duplicates(data_list):
#     no_duplicates = []
#     for i in data_list:
#         if i not in no_duplicates:
#             no_duplicates.append(i)
#     return no_duplicates

def isacii(s):
    try:
        s.encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True

def remove_ascii(filename):
    contains_ascii = []
    no_ascii = select_row_elements(filename)[1]
    for row in select_row_elements(filename)[1]:
        for i in row:
            if isacii(i) is False:
                contains_ascii.append(row)
                no_ascii.remove(row)
                break
    return contains_ascii, no_ascii


