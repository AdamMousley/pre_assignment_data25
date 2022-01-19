from app.extract_csv import *
import numpy as np

# Calls the function that turns the csv to a dataframe
imdb_df = csv_to_dataframe("imdb_data.csv")
# print(imdb_df)

# The column headers
column_headers = col_headers(imdb_df)
#print(column_headers)

# # Check if the values are ture or false
x = check_if_empty(imdb_df)
# print(x)

# Calls the function to remove any duplicates, based on title
imdb_df_wo_dup = drop_duplicates(imdb_df)
# print(imdb_df_wo_dup)

#empty_values_col(imdb_df_wo_dup)

# print(np.where(pd.isnull(imdb_df_wo_dup)))

print(imdb_df_wo_dup.isnull().sum())

