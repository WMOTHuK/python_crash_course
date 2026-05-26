""" Unit test for Employee class"""
#Standart_imports
import unittest

#Local imports
from PCC_11_Testing import Employee

class EmployeeTestCases(unittest.TestCase):
    """Tests of Employee class"""
    def setUp(self):
        """creates initial data for tests"""
        self.employee = Employee('Varvar','Malysheva',30000)
        self.salary_increase = 10000

    def test_give_default_raise(self):
        """Tests default raise"""
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 35000)

    def test_give_random_raise(self):
        """Tests random raise"""
        self.employee.give_raise(self.salary_increase)
        self.assertEqual(self.employee.salary, 40000)        

unittest.main()