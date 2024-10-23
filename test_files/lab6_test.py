import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab6_even_digit_counter import even_digit_counter

class TestLab1(unittest.TestCase):

    def test_leapYear(self):
        self.assertEqual(even_digit_counter(2000), 4)
        self.assertEqual(even_digit_counter(2001), 3)
        self.assertEqual(even_digit_counter(1900), 2)
        self.assertEqual(even_digit_counter(646486), 6)
        self.assertEqual(even_digit_counter(99), 0)
        self.assertEqual(even_digit_counter(152213770), 3)
        self.assertEqual(even_digit_counter(123456789), 4)
        self.assertEqual(even_digit_counter(2020), 4)
        

if __name__ == '__main__':
    unittest.main()