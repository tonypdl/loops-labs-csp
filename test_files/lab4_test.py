import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab4_perfect_number import perfect_number

class TestLab1(unittest.TestCase):

    def test_leapYear(self):
        self.assertEqual(perfect_number(2000), )
        self.assertEqual(perfect_number(2001), )
        self.assertEqual(perfect_number(1900), )
        self.assertEqual(perfect_number(646486), )
        self.assertEqual(perfect_number(99), )
        self.assertEqual(perfect_number(152213770), )
        self.assertEqual(perfect_number(123456789), )
        self.assertEqual(perfect_number(2020), )
        

if __name__ == '__main__':
    unittest.main()