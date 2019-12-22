from generator.create_out_file import create_output
from generator.reader_json import read_files

if __name__ == '__main__':
    nodes = read_files('JSON_files')
    create_output(nodes)

