import unittest

from generator.reader_json import read_files, python_json_file_to_dict

nodes = []


class UtilsTestCase(unittest.TestCase):
    def setUp(self):
        self.file_path = 'JSON_files'


    def test_read_files(self):
        listS = ["BIG01",
                 "BIG02",
                 "BIG03",
                 "BIG04",
                 "BIG05",
                 "BIG06",
                 "BIG07",
                 "BIG08",
                 "BIG09",
                 "BIG10"]
        l = []
        nodes = read_files('JSON_files')
        for i in nodes:
             l.append(i.get_name())
        self.assertEqual(l, listS)

    def test_python_json_file_to_dict(self):
        listS = ["BIG01",
                 "BIG02",
                 "BIG03",
                 "BIG04",
                 "BIG05",
                 "BIG06",
                 "BIG07",
                 "BIG08",
                 "BIG09",
                 "BIG10"]

        node1s = python_json_file_to_dict('JSON_files/El_Palacio_de_Hierro_RSX_7.7_Invoices_to_X12_5010_Transaction-810.json')
        l = []
        for i in node1s:
            l.append(i.get_name())
        self.assertEqual(l, listS)

