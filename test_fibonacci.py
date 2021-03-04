import unittest
from fibonacci import fibonacci, factorial

class TestFib(unittest.TestCase):
  def test_fibonacci1(self):
    self.assertEqual(fibonacci(1), 0)
  
  def test_fibonacci2(self):
    self.assertEqual(fibonacci(2), 1)
  
  def test_fibonacci3(self):
    self.assertEqual(fibonacci(3), 1)
  
  def test_fibonacci4(self):
    self.assertEqual(fibonacci(4), 2)
  
  def test_fibonacci5(self):
    self.assertEqual(fibonacci(5), 3)
    
  def test_fibonacci6(self):
    self.assertEqual(fibonacci(6), 5)
    
  def test_fibonacci7(self):
    self.assertEqual(fibonacci(7), 8)
  
  def test_fibonacciNeg(self):
    self.assertEqual(fibonacci(-1), None)
    
  def test_factorial1(self):
    self.assertEqual(factorial(0), 1)
    
  def test_factorial2(self):
    self.assertEqual(factorial(3), 6)
  
  def test_factorial3(self):
    self.assertEqual(factorial(5), 120)
    
  def test_factorialNeg(self):
    self.assertEqual(factorial(-1), None)
  
if __name__ == '__main__':
    unittest.main()