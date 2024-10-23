import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab1_reverse_number import reverse_number

class TestLab1(unittest.TestCase):

    def test_leapYear(self):
        self.assertEqual(reverse_number(2000), "0002")
        self.assertEqual(reverse_number(2001), "1002")
        self.assertEqual(reverse_number(1900), "0091")
        self.assertEqual(reverse_number(646486), "684646")
        self.assertEqual(reverse_number(99), "99")  
        self.assertEqual(reverse_number(152213770), "077312251")
        self.assertEqual(reverse_number(646464684643546489138113813), "318311831984645346486464646")
        self.assertEqual(reverse_number(2020), "0202")
        



if __name__ == '__main__':
    unittest.main()