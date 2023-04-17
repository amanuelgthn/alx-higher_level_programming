import unittest

from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):

    def test_init(self):
        rect = Rectangle(10, 20)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_get_area(self):
        rect = Rectangle(10, 20)
        self.assertEqual(rect.get_area(), 200)

    def test_set_width(self):
        rect = Rectangle(10, 20)
        rect.set_width(30)
        self.assertEqual(rect.width, 30)

    def test_set_height(self):
        rect = Rectangle(10, 20)
        rect.set_height(40)
        self.assertEqual(rect.height, 40)

    def test_str(self):
        rect = Rectangle(10, 20)
        self.assertEqual(str(rect), "Rectangle(width=10, height=20)")

    def test_repr(self):
        rect = Rectangle(10, 20)
        self.assertEqual(repr(rect), "Rectangle(width=10, height=20)")

    def test_to_dictionary(self):
        rect = Rectangle(10, 20)
        expected_dict = {
        "width": 10,
        "height": 20,
        "x": 0,
        "y": 0,
        "id": rect.id}
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_from_dictionary(self):
        expected_rect = Rectangle(10, 20)
        dictionary = expected_rect.to_dictionary()
        actual_rect = Rectangle.from_dictionary(dictionary)
        self.assertEqual(actual_rect, expected_rect)

    def test_save_to_file(self):
        rect = Rectangle(10, 20)
        with open("rect.json", "w") as file:
            rect.save_to_file(file)
        with open("rect.json", "r") as file:
            actual_rect = Rectangle.from_json_string(file.read())
        self.assertEqual(rect, actual_rect)

    def test_load_from_file(self):
        expected_rect = Rectangle(10, 20)
        with open("rect.json", "w") as file:
            expected_rect.save_to_file(file)
        actual_rect = Rectangle.load_from_file("rect.json")
        self.assertEqual(actual_rect, expected_rect)


if __name__ == "__main__":
    unittest.main()