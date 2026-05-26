""" Unit test for cities functions"""
#Standart_imports
import unittest

#Local imports
from PCC_11_Testing import get_town_desc

class CityTestCases(unittest.TestCase):
    """Unit test for get_town_desc function"""
    def test_two_arguments(self):
        """ Tests two arguments"""
        desc =  get_town_desc('vladimir', 'russia')
        self.assertEqual(desc, 'Vladimir, Russia')
    def test_three_arguments(self):
        """ Tests two arguments"""
        desc =  get_town_desc('vladimir', 'russia',300000)
        self.assertEqual(desc, 'Vladimir, Russia - population 300000')

unittest.main()