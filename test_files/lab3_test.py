import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab3_divisor_finder import divisor_finder

class TestLab1(unittest.TestCase):

    def test_leapYear(self):
        self.assertEqual(divisor_finder(2000), )
        self.assertEqual(divisor_finder(2001), )
        self.assertEqual(divisor_finder(1900), )
        self.assertEqual(divisor_finder(646486), )
        self.assertEqual(divisor_finder(99), )
        self.assertEqual(divisor_finder(152213770), )
        self.assertEqual(divisor_finder(123456789), )
        self.assertEqual(divisor_finder(2020), )
        

if __name__ == '__main__':
    unittest.main()