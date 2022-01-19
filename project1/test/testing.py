import unittest
from app.extract_csv import *
from pandas.testing import assert_frame_equal

class imdb_test(unittest.TestCase):

    # A test on the dummy data to see if duplicates are successfully removed
    def test_drop_duplicates(self):
        dummy_data = "testingcsv.csv"
        dummy_df = csv_to_dataframe(dummy_data)
        test = drop_duplicates(dummy_df)
        print(test)

if __name__ == '__main__':
    unittest.main()
