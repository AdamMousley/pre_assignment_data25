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

def appending(df):
    dfObj = pd.DataFrame()
    if df.isnull() == False:
        dfObj.append(df.isnull())
    return dfObj

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



import numpy as np
#
# # Calls the function that turns the csv to a dataframe
# imdb_df = csv_to_dataframe("imdb_data.csv")
# # print(imdb_df)
#
# # The column headers
# column_headers = col_headers(imdb_df)
# #print(column_headers)
#
# # # Check if the values are ture or false
# empty_values = check_if_empty(imdb_df)
# print(empty_values)
#
# # Calls the function to remove any duplicates, based on title
# imdb_df_wo_dup = drop_duplicates(imdb_df)
# #print(imdb_df_wo_dup)