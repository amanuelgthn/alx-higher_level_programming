#!/usr/bin/python3
"""
import module unittest
"""


import unittest

from models.base import Base


class BaseTest(unittest.TestCase):
    """
    class to test Base module
    """


    def test_init(self):
        # Test that the `__init__()` method sets the `id` attribute correctly.
        base_1 = Base()
        self.assertEqual(base_1.id, 1)

        base_2 = Base(id=2)
        self.assertEqual(base_2.id, 2)

    def test_to_json_string(self):
        # Test that the `to_json_string()` method returns a valid JSON string.
        base_1 = Base()
        expected_json_string = '{"id": 1}'
        self.assertEqual(Base.to_json_string([base_1]), expected_json_string)

    def test_save_to_file(self):
        # Test that the `save_to_file()` method saves the list of objects to a file in JSON format.
        base_1 = Base()
        base_2 = Base()

        with open('test.json', 'w', encoding='utf-8') as file:
            Base.save_to_file([base_1, base_2])

        with open('test.json', 'r', encoding='utf-8') as file:
            actual_json_string = file.read()

        expected_json_string = '[[{"id": 1}, {"id": 2}]]'
        self.assertEqual(actual_json_string, expected_json_string)

    def test_from_json_string(self):
        # Test that the `from_json_string()` method returns a list of objects from a JSON string.
        expected_list_of_objects = [Base(), Base()]
        actual_list_of_objects = Base.from_json_string('[[{"id": 1}, {"id": 2}]]')
        self.assertEqual(actual_list_of_objects, expected_list_of_objects)

    def test_create(self):
        # Test that the `create()` method creates an instance of the correct class.
        base_1 = Base.create(width=4, height=6)
        self.assertIsInstance(base_1, Rectangle)

        base_2 = Base.create(side=4)
        self.assertIsInstance(base_2, Square)


if __name__ == '__main__':
    unittest.main()