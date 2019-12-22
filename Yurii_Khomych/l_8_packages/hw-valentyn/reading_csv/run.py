import datetime as dt

from create_output import create_output
from read_csv import read_csv
import logging


if __name__ == '__main__':
    logging.basicConfig(filename="sample.log", level=logging.INFO)
    dtime = dt.datetime.now()
    logging.info('Start main: ' + str(dtime))

    parsed_by_date = read_csv('./testfiles/example.csv')
    create_output(parsed_by_date)
    logging.info('End main: ' + str(dtime))


# {'10/20/2019': [('100.0', 'N4000051-N4000058')], '10/21/2019': [('100.0', 'N4000052-N4000058'), ('100.0', 'N4000053-N4000058')], '10/24/2019': [('100.0', 'N4000054-N4000058'), ('1.0', 'N4000055-N4000058')]}
