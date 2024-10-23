import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab2_digit_adder import digit_adder

class TestLab1(unittest.TestCase):

    def test_leapYear(self):
        self.assertEqual(digit_adder(2000), "2 is the sum of the digits of 2000")
        self.assertEqual(digit_adder(2001), "3 is the sum of the digits of 2001")
        self.assertEqual(digit_adder(1900), "10 is the sum of the digits of 1900")
        self.assertEqual(digit_adder(646486), "34 is the sum of the digits of 646486")
        self.assertEqual(digit_adder(99), "18 is the sum of the digits of 99")
        self.assertEqual(digit_adder(152213770), "28 is the sum of the digits of 152213770")
        self.assertEqual(digit_adder(123456789), "45 is the sum of the digits of 123456789")
        self.assertEqual(digit_adder(2020), "4 is the sum of the digits of 2020")
        

if __name__ == '__main__':
    unittest.main()