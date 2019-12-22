from create_output import create_output
from read_csv import read_csv

if __name__ == '__main__':
    parsed_by_date = read_csv('./testfiles/example.csv')
    create_output(parsed_by_date)

