import unittest
SimpleCalculator = __import__ ('simple_calculator').SimpleCalculator
class Testsimplecalculator(unittest.TestCase):
    """Test cases for the SimpleCalculator class."""
    def test_add(self):
        """Test add method"""
        self.assertEqual(SimpleCalculator().add(1, 2), 3)
    def test_multiply(self):
        """Test multiply method"""
        self.assertEqual(SimpleCalculator().multiply(2, 3), 6)
    def test_subtract(self):
        """Test subtract method"""
        self.assertEqual(SimpleCalculator().subtract(5, 3), 2)
    def test_divide(self):
        """Test divide method"""
        self.assertEqual(SimpleCalculator().divide(6, 2), 3)
        self.assertIsNone(SimpleCalculator().divide(6, 0))
