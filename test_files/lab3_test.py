import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab3_divisor_finder import divisor_finder

class TestLab1(unittest.TestCase):

    def test_leapYear(self):
        self.assertEqual(divisor_finder(6), "6 has the divisors 1 2 3")
        self.assertEqual(divisor_finder(45), "45 has the divisors 1 3 5 9 15")
        self.assertEqual(divisor_finder(14), "14 has the divisors 1 2 7")
        self.assertEqual(divisor_finder(8128), "8128 has the divisors 1 2 4 8 16 32 64 127 254 508 1016 2032 4064")
        self.assertEqual(divisor_finder(28), "28 has the divisors 1 2 4 7 14")
        self.assertEqual(divisor_finder(1), "1 has the divisors ")
        

if __name__ == '__main__':
    unittest.main()