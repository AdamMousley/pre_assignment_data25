import pandas as pd
import csv

# with open("imdb_data.csv", encoding='utf8') as csv_file:
#     info = csv.reader(csv_file, delimiter=',')
#     for row in info:
#         print(row)

def extract_csv(filename):
    with open(filename, encoding='utf8') as csv_file:
        info = csv.reader(csv_file, delimiter=',')
        for row in info:
            print(row)

x = "imdb_data.csv"
extract_csv(x)