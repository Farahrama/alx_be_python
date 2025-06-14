import unittest
from simple_calculator import SimpleCalculator
calc = SimpleCalculator()
class Testsimplecalculator(unittest.TestCase):
    """Test cases for the SimpleCalculator class."""
    def test_addition(self):
        """Test addition 1, 2"""
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_multiplication(self):
        """Test multiply method"""
        self.assertEqual(self.calc.multiply(2, 3), 6)
    def test_subtraction(self):
        """Test subtract method"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
    def test_division(self):
        """Test divide method"""
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertIsNone(self.calc.divide(6, 0))
