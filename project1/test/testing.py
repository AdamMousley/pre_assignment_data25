import unittest
from app.extract_csv import *
from app.extract_attempt_two import *
from pandas.testing import assert_frame_equal

class imdb_test(unittest.TestCase):

    # A test on the dummy data to see if duplicates are successfully removed
    def test_drop_duplicates(self):
        dummy_data = "testingcsv.csv"
        dummy_df = csv_to_dataframe(dummy_data)
        test = drop_duplicates(dummy_df)
        #print(test)

    def test_select_row_elements(self):
        dummy_data = "testingcsv.csv"
        i = read_csv(dummy_data)
        x = select_row_elements(i)
        print(x[0])
        print(x[1])

if __name__ == '__main__':
    unittest.main()
