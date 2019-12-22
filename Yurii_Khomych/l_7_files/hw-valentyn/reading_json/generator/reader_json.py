import json
import re
from os import listdir
from os.path import isfile, join

from generator.my_structure import MyStructure

nodes = []


def read_files(dir):
    files = [f for f in listdir(dir) if isfile(join('JSON_files', f))]
    for file in files:
        nodes_schema = python_json_file_to_dict(dir+"/" + file)


    return nodes_schema


def python_json_file_to_dict(file_path):
    source_column = file_path[file_path.index("RSX"): file_path.index("_to_")]
    ind = (re.search("-[0-9][0-9][0-9]", file_path[file_path.index("_to_") + 4:]).start()) + 3
    dest_column = file_path[file_path.index("_to_") + 4:]
    dest_column = dest_column[:24]

    try:
        file_object = open(file_path, 'r')
        dict_object = json.load(file_object)
        get_deeper_child(dict_object, '', nodes, source_column, dest_column)

    except FileNotFoundError:
        print(file_path + " not found. ")

    return nodes


def get_deeper_child(dict_el, str_loop_name, nodes_my, source_column, dest_column):
    for i in dict_el['children']:

        if 'Loop' in i['name']:
            if str_loop_name == i['name']:
                str_loop_name = i['name']

        if str_loop_name[:-1] != '/' and str_loop_name and ('Composite' in i['name'] or 'Loop' in i['name']
                                                            or 'Segment' in i['name'] or i['children']):
            str_loop_name = str_loop_name + "/"
        str_loop_name = str_loop_name.replace('//', '/')

        if i['children']:
            get_deeper_child(i, (str_loop_name + i['name']).replace('//', '/'), nodes_my, source_column, dest_column)
        else:
            nodes_my.append(MyStructure(str_loop_name, source_column, dest_column, i))
