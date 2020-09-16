import unittest
from unittest import mock

from my_module import examples

class TestJSON2MMD(unittest.TestCase):

    def test_lowercase(self):
        dictin = {'Toto': 'TOTO', 'tata': 2, 'TUTU': 'Hello'}
        self.assertEqual(examples._lowercase(dictin), {'toto': 'TOTO', 'tata': 2, 'tutu': 'Hello'})
        dictin = [{'Toto': 'TOTO', 'tata': 2, 'TUTU': 'Hello'}]
        self.assertEqual(examples._lowercase(dictin), dictin)

    def test_merge_dicts(self):
        # simple merge
        dict1 = {'A': 1, 'B': 2}
        dict2 = {'A': 2, 'C': 3}
        examples._merge_dicts(dict1, dict2)
        self.assertEqual(dict1, {'A': 2, 'B': 2, 'C': 3})
        # nested dictionaries
        dict1 = {'A': 1, 'B': {'B1': 5, 'B2': 6}}
        dict2 = {'A': 2, 'C': 3, 'B': {'B1': 7}}
        examples._merge_dicts(dict1, dict2)
        self.assertEqual(dict1, {'A': 2, 'B':{'B1': 7, 'B2': 6}, 'C': 3})
        # one dictionary key in dict1 is not a dict, but same key in dict2 is a dict
        # -> raise Error
        dict1 = {'A': 1, 'B': {'B1': 5, 'B2': 6}}
        dict2 = {'A': 2, 'C': 3, 'B': 7}
        with self.assertRaises(TypeError) as context:
            examples._merge_dicts(dict1, dict2)
        # one dictionary key in dict2 is not a dict, but same key in dict1 is a dict
        # -> raise Error
        dict1 = {'A': 2, 'C': 3, 'B': 7}
        dict2 = {'A': 1, 'B': {'B1': 5, 'B2': 6}}
        with self.assertRaises(TypeError) as context:
            examples._merge_dicts(dict1, dict2)

if __name__ == '__main__':
    unittest.main()


