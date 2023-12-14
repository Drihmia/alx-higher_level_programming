import unittest
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Unittest class for Rectangle class.
    """
    def test_init(self):
        """
        Test the __init__ method.
        """
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(10, 20, 30, 40)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 20)
        self.assertEqual(r2.x, 30)
        self.assertEqual(r2.y, 40)

    def test_area(self):
        """
        Test the area method.
        """
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.area(), 200)

        r2 = Rectangle(10, 20, 30, 40)
        self.assertEqual(r2.area(), 200)

    @patch('builtins.print')
    def test_display(self, mock_print):
        """
        Test the display method.
        """
        r1 = Rectangle(4, 5)
        r1.display()
        mock_print.assert_called_with("####\n####\n####\n####\n####")

        r1 = Rectangle(4, 5, 1, 2)
        r1.display()
        mock_print.assert_called_with("\n\n ####\n ####\n ####\n ####\n ####")

    def test_str__(self):
        """
        Test the __str__ method.
        """
        # test for rectangle
        r1 = Rectangle(10, 20)
        self.assertEqual(str(r1), "[Rectangle] (55) 0/0 - 10/20")

        r2 = Rectangle(10, 20, 30, 40)
        self.assertEqual(str(r2), "[Rectangle] (56) 30/40 - 10/20")

    def test_update(self):
        """
        Test the update method.
        """
        r1 = Rectangle(10, 20)
        r1.update(1, 3, 4, 5, 6)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 6)

        r2 = Rectangle(10, 20, 30, 40)
        r2.update(id=1, width=3, height=4, x=5, y=6)
        self.assertEqual(r2.id, 1)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 5)
        self.assertEqual(r2.y, 6)

        r3 = Rectangle(10, 20, 30, 40)
        r3.update(width=3, height=4)
        self.assertEqual(r3.id, 60)
        self.assertEqual(r3.width, 3)
        self.assertEqual(r3.height, 4)
        self.assertEqual(r3.x, 30)
        self.assertEqual(r3.y, 40)

        r4 = Rectangle(10, 20, 30, 40)
        r4.update(x=5, y=6)
        self.assertEqual(r4.id, 61)
        self.assertEqual(r4.width, 10)
        self.assertEqual(r4.height, 20)
        self.assertEqual(r4.x, 5)
        self.assertEqual(r4.y, 6)

        r5 = Rectangle(10, 20, 30, 40)
        r5.update(**{"id": 1, "width": 3, "height": 4, "x": 5, "y": 6})
        self.assertEqual(r5.id, 1)
        self.assertEqual(r5.width, 3)
        self.assertEqual(r5.height, 4)
        self.assertEqual(r5.x, 5)
        self.assertEqual(r5.y, 6)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method.
        """
        r1 = Rectangle(10, 20, 2, 3, 5)
        dict_r1 = r1.to_dictionary()
        self.assertEqual(dict_r1["id"], 5)
        self.assertEqual(dict_r1["width"], 10)
        self.assertEqual(dict_r1["height"], 20)
        self.assertEqual(dict_r1["x"], 2)
        self.assertEqual(dict_r1["y"], 3)

        r2 = Rectangle(10, 20, 30, 40)
        dict_r2 = r2.to_dictionary()
        self.assertEqual(dict_r2["id"], 57)
        self.assertEqual(dict_r2["width"], 10)
        self.assertEqual(dict_r2["height"], 20)
        self.assertEqual(dict_r2["x"], 30)
        self.assertEqual(dict_r2["y"], 40)


if __name__ == '__main__':
    unittest.main()
