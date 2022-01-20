from app.extract_attempt_two import *
from pprint import pprint

# Calling the function to produce an output of the csv, in the form of list of lists
csv_rows = read_csv("imdb_data.csv")

# Calling the function that returns two lists, one with and one without empty values.
rows_w_empty_data = select_row_elements("imdb_data.csv")[0]
rows_wo_empty_data = select_row_elements("imdb_data.csv")[1]

# Calling the function that removes duplicates in the data without empty values
wo_empty_remove_dups = remove_duplicates(rows_wo_empty_data)

# Calling the function that removes duplicates in the data with empty values
w_empty_remove_dups = remove_duplicates(rows_w_empty_data)




# print(len(rows_w_empty_data))
# print(len(rows_wo_empty_data))
#
# print(len(remove_duplicates(rows_w_empty_data)))
# print(len(remove_duplicates(rows_wo_empty_data)))


