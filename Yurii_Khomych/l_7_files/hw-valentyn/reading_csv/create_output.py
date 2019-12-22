import os
import pickle


def create_output(some_dict):
    for key in some_dict.keys():
        os.makedirs("./result/" + key.replace('/', ''), exist_ok=True)
        with open("./result/" + key.replace('/', '') + '/order.pcl', 'wb+') as my_file:
            pickle.dump(some_dict[key], my_file)
