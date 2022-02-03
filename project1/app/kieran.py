# called his csv_cleaner
import csv
from definitions import ROOT_DIR


class ImdbCsvCleaner:
    def __init__(self, csv_file_location, missing_record_file_location, cleaned_csv_name_and_location):
        self.csv_file_location = ROOT_DIR + csv_file_location
        self.missing_record_file_location = ROOT_DIR + missing_record_file_location
        self.cleaned_imdb_csv_location = ROOT_DIR + cleaned_csv_name_and_location

    def imdb_csv_missing_data_cleaner(self):
        with open(self.csv_file_location, encoding='utf8') as open_csv:
            imdb_data = csv.reader(open_csv, delimiter=',')
            imdb_data.__next__()  # ignore the headers using this line
            for movie_data_line in imdb_data:
                if self.imdb_line_clean_check(movie_data_line):
                    self.missing_data_object_writer(movie_data_line)
                else:
                    self.clean_data_object_writer(movie_data_line)

    def clean_data_object_writer(self, completed_data_line):
        with open(self.cleaned_imdb_csv_location, "+a", encoding='utf8', newline='\n') as cleaned_data_file:
            clean_data_writer = csv.writer(cleaned_data_file)
            clean_data_writer.writerow(completed_data_line)

# Changing one thing ever so slightly

    def imdb_line_clean_check(self, imdb_data_line):
        item_empty_flag = None
        for item in imdb_data_line:
            if not item:
                item_empty_flag = True
        return item_empty_flag

    def missing_data_object_writer(self, missing_data_line):
        with open(self.missing_record_file_location, '+a', encoding='utf8', newline='\n') as missing_record_file:
            missing_record_writer = csv.writer(missing_record_file)
            missing_record_writer.writerow(missing_data_line)


# A stand alone place to run just in this file, another file wont run this section
if __name__ == '__main__':
    imdb_csv_cleaner = ImdbCsvCleaner("/resources/imdb_data.csv", "/resources/imdb_missing_records.csv", "/resources/imdb_cleaned_data.csv")
    imdb_csv_cleaner.imdb_csv_missing_data_cleaner()