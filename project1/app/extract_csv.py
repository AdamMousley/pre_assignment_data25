import pandas as pd
import csv

# def extracting_csv(filename):
#     with open(filename, encoding='utf8') as csv_file:
#         info = csv.reader(csv_file, delimiter=',')
#         for row in info:
#             print(row)
#
# x = "imdb_data.csv"
# extracting_csv(x)

def csv_to_dataframe(filename):
    imdb_df = pd.read_csv(filename)
    return imdb_df

print(csv_to_dataframe("imdb_data.csv"))