import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab5_letter_remover import letter_remover

class TestLab1(unittest.TestCase):

    def test_leapYear(self):
        self.assertEqual(letter_remover("I'm a big baby!", "b"), "I'm a ig ay!")
        self.assertEqual(letter_remover("Fantastic Mr. Fox", "F"), "antastic Mr. ox")
        self.assertEqual(letter_remover("Moonrise Kingdom", "o"), "Mnrise Kingdm")
        self.assertEqual(letter_remover("Isle of Dogs", "x"), "Isle of Dogs")
        self.assertEqual(letter_remover("fox jumps over the doggo", "o"), "fx jumps ver the dgg")
        self.assertEqual(letter_remover("abba abba abba", "b"), "aa aa aa")
        self.assertEqual(letter_remover("111111111", "1"), "")
        self.assertEqual(letter_remover("2020", "0"), "22")
        

if __name__ == '__main__':
    unittest.main()