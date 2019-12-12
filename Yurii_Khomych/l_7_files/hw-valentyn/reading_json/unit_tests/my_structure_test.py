import unittest

from generator.my_structure import MyStructure


class MyStructureTest(unittest.TestCase):

    def setUp(self):
        self.ms = MyStructure('IT1_loop', 'RSXv7m7', 'X12',
                              {'hasEnum': False, 'validation': [], 'name': 'IT101', 'minOccurs': '1', 'children': [], 'visible': True, 'sourcing': {'hasEnum': False, 'documentation': 'For an initiated document, this is a unique number for the line item[s]. For a return transaction, this number should be the same as what was received from the source transaction. Example: You received a Purchase Order with the first LineSequenceNumber of 10. You would then send back an Invoice with the first LineSequenceNumber of 10.', 'name': 'LineSequenceNumber', 'location': 'Invoice/LineItem/InvoiceLine/LineSequenceNumber'}, 'attributes': [{'hasEnum': False, 'validation': [], 'minOccurs': '1', 'text': 'Alphanumeric characters assigned for differentiation within a transaction set', 'children': [], 'visible': True, 'attributes': [], 'elementType': 'documentation', 'id': 1209}, {'hasEnum': False, 'validation': [], 'displayName': 'String', 'minOccurs': '1', 'minLength': '1', 'children': [], 'visible': True, 'ediId': '350', 'EDIDataType': 'AN', 'base': 'EDI-Element-String-Type', 'maxLength': '20', 'attributes': [], 'elementType': 'restriction', 'id': 1210}], 'elementType': 'element', 'id': 1208})

    def test_get_name(self):
        name = "IT101"
        self.assertEqual(self.ms.get_name(), name)

    def test_get_sourcing(self):
        sourcing = 'RSXv7m7|X12|IT1_loop/IT101:Invoice/LineItem/InvoiceLine/LineSequenceNumber'
        self.assertEqual(self.ms.get_sourcing(),sourcing)
