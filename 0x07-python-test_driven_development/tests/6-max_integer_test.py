#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

"""
Test file for max_integer function
"""

class TestMaxInteger(unittest.TestCase):
    """Testing the max_integer function

    """

    def test_max_integer(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([4]), 4)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer("red"), "r")
        self.assertAlmostEqual(max_integer("reds"), "s")
        self.assertAlmostEqual(max_integer([10, 22, 3,2, 4]), 22)
        self.assertAlmostEqual(max_integer([-10, -22, -3.2, -4]), -3.2)

    def test_values(self):
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, 2)
        self.assertRaises(TypeError, max_integer, 0)
        self.assertRaises(TypeError, max_integer, [1, "3", 4, 2])
        self.assertRaises(TypeError, max_integer, [1, "3", 4, [2, 4]])
        self.assertRaises(TypeError, max_integer, [1, "3", 4, (2, 4)])

     
