import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab4_perfect_number import perfect_number

class TestLab1(unittest.TestCase):

    def test_leapYear(self):
        self.assertEqual(perfect_number(6), True)
        self.assertEqual(perfect_number(45), False)
        self.assertEqual(perfect_number(14), False)
        self.assertEqual(perfect_number(8128), True)
        self.assertEqual(perfect_number(33550336), True)
        self.assertEqual(perfect_number(28), True)
        

if __name__ == '__main__':
    unittest.main()