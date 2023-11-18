#python -m unittest test_calculator_func
import unittest
from main import add, subtract, multiply, divide

class TestCalculatorFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3, 2), 10)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0, 1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(5, 3, 2), 30)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(8, 4), 2.0)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(0, 5), 0.0)
        
        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
