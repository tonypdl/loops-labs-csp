import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab5_letter_remover import letter_remover

class TestLab1(unittest.TestCase):

    def test_leapYear(self):
        self.assertEqual(letter_remover(2000), )
        self.assertEqual(letter_remover(2001), )
        self.assertEqual(letter_remover(1900), )
        self.assertEqual(letter_remover(646486), )
        self.assertEqual(letter_remover(99), )
        self.assertEqual(letter_remover(152213770), )
        self.assertEqual(letter_remover(123456789), )
        self.assertEqual(letter_remover(2020), )
        

if __name__ == '__main__':
    unittest.main()