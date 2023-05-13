import unittest
from addition import add_numbers

class TestAddition(unittest.TestCase):

    def test_add_numbers_positive(self):
        self.assertEqual(add_numbers(3, 5), 8, "Expected sum of 3 and 5 to be 8")

    def test_add_numbers_negative(self):
        self.assertEqual(add_numbers(-3, -5), -8, "Expected sum of -3 and -5 to be -8")

    def test_add_numbers_mixed(self):
        self.assertEqual(add_numbers(5, -3), 2, "Expected sum of 5 and -3 to be 2")

    def test_add_numbers_zero(self):
        self.assertEqual(add_numbers(0, 0), 0, "Expected sum of 0 and 0 to be 0")
    
    def test_add_fractions(self):
        self.assertEqual(add_numbers(1/2, 1/2), 1, "Expected sum of 1/2 and 1/2 to be 1")

if __name__ == "__main__":
    unittest.main()