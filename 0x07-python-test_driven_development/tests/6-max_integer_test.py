#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    TestMaxInteger class to unittest max_integer function
    """

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertIsNone(max_integer([]), None)
        self.assertEqual(max_integer([-5, 2, 3]), 3)
        self.assertEqual(max_integer([]), None)
