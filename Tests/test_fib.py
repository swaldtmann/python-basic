#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from fibonacci import fib

class FibonacciTest(unittest.TestCase):

    def testCalculation(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(10), 55)
    
    def testCalculation2(self):
        self.assertEqual(fib(20), 6765)

if __name__ == "__main__": 
    unittest.main()
