import sys
import os
import unittest
import doctest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import calculator.calculator as calculator_module
from calculator.calculator import Calculator


doctest.testmod(calculator_module)

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(3), 3)
        self.assertEqual(self.calculator.add(7.5), 10.5)
        self.assertEqual(self.calculator.add(2.33), 12.83)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(2), -2)
        self.assertEqual(self.calculator.subtract(0.24), -2.24)

    def test_multiply(self):
        self.calculator.add(4)
        self.assertEqual(self.calculator.multiply(6), 24)
        self.assertEqual(self.calculator.multiply(1.33), 31.92)

    def test_divide(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(0)
        self.calculator.add(99)
        self.assertEqual(self.calculator.divide(3), 33)
        self.assertEqual(self.calculator.divide(2.5), 13.2)

    def test_n_root(self):
        with self.assertRaises(ValueError):
            self.calculator.n_root(0)
        self.calculator.add(64)
        self.assertEqual(self.calculator.n_root(3), 4)
        self.assertEqual(self.calculator.n_root(2), 2)

    def test_reset(self):
        self.calculator.add(2)
        self.assertEqual(self.calculator.reset(), 0)


if __name__ == '__main__':
    unittest.main()
