import os
import pickle
import logging


def create_output(some_dict):
    for key in some_dict.keys():
        logging.info('Trying to write result: ' + key.replace('/', ''))

        os.makedirs("./result/" + key.replace('/', ''), exist_ok=True)
        logging.info('Created folder: ' + key.replace('/', ''))

        with open("./result/" + key.replace('/', '') + '/order.pcl', 'wb+') as my_file:
            pickle.dump(some_dict[key], my_file)
        logging.info('Created pickle file: ' + key.replace('/', '') + '/order.pcl')

