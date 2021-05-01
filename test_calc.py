import unittest
import calc

class TestStringMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(5, 10), 15) # Pass
        #self.assertEqual(calc.add(4, 3), 10) # Fail

    def test_sub(self):
        self.assertEqual(calc.subtract(4, 3), 1) #Pass
        #self.assertEqual(calc.subtract(5, 7), -4) # Fail

    def test_mult(self):
        self.assertEqual(calc.multiply(4, 3), 12) # Pass
        #self.assertEqual(calc.multiply(-5, 0), 1) # Fail

    def test_div(self):
        self.assertEqual(calc.divide(3, 6), 0.5) # pass
        #self.assertEqual(calc.divide(25, 5), 50) # Fail


if __name__ == '__main__':
    unittest.main()