import pandas as pd
import csv

def csv_to_dataframe(filename):
    imdb_df = pd.read_csv(filename)
    return imdb_df

def check_if_empty(df):
    values = df.isnull()
    return values

def drop_duplicates(df):
    updated_df = df.drop_duplicates()
    return updated_df

def col_headers(df):
    headers = []
    for i in df.columns.values:
        headers.append(i)
    return headers



# def iterate(df):
#     for row in df.iterrows():
#         for i in row:
#             #print(i)
#             x = check_if_empty(i)
#             return(x)

# To do list
# create a store with all the empty records to be reviewed
# remove white space
# create a seperate file for