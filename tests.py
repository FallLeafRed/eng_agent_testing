import unittest
from game import simple_calculator

class TestSimpleCalculator(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(simple_calculator(2, 3, "Addition"), 5)
        
    def test_subtraction(self):
        self.assertEqual(simple_calculator(5, 3, "Subtraction"), 2)
        
    def test_multiplication(self):
        self.assertEqual(simple_calculator(4, 2, "Multiplication"), 8)
        
    def test_division(self):
        self.assertEqual(simple_calculator(10, 2, "Division"), 5)
        
    def test_division_by_zero(self):
        self.assertEqual(simple_calculator(5, 0, "Division"), "Error: Division by zero")

if __name__ == '__main__':
    unittest.main()