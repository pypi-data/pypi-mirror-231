import unittest
from CalculatorTuringAjdin import add, subtract, multiply, divide, nRoot

class TestCalculator(unittest.TestCase):
   def test_addition(self):
        result = add(5.0, 3.0)
        self.assertEqual(result, 8.0)

   def test_subtraction(self):
        result = subtract(10.0, 4.0)
        self.assertEqual(result, 6.0)

   def test_multiplication(self):
        result = multiply(7.0, 2.0)
        self.assertEqual(result, 14.0)

   def test_division(self):
        result = divide(8.0, 2.0)
        self.assertEqual(result, 4.0)

   def test_nRoot(self):
        result = nRoot(16.0, 2.0)
        self.assertEqual(result, 4.0)


if __name__ == '__main__':
    unittest.main()
