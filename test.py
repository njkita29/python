import unittest
class Calculator:
    def plus(self,a,b):
        return a+b
    def minus(self,a,b):
        return a-b
    def diviseon(self,a,b):
        return a/b
    def multiply(selfa,a,b):
        return a*b
    def square(self,a):
        return a*a
class Testcalculator(unittest.TestCase):
    def setUp(self):
        self.calculator=Calculator()
    def testplus(self):
        self.assertEqual(self.calculator.plus(2,3),5)
    def testminus(self):
        self.assertEqual(self.calculator.minus(10,9),1)
    def testminus(self):
        self.assertEqual(self.calculator.diviseon(25,5),5)
    def testmultiply(self):
        self.assertEqual(self.calculator.multiply(58,97),5626)
    def testsquare(self):
        self.assertEqual(self.calculator.square(10),100)