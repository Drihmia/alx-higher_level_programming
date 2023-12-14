import unittest
from models.square import Square
import pep8


class TestSquare(unittest.TestCase):
    """
    Unittest class for Square class.
    """

    def test_init(self):
        """
        Test the __init__ method.
        """
        s1 = Square(10)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(20, 30, 40)
        self.assertEqual(s2.size, 20)
        self.assertEqual(s2.x, 30)
        self.assertEqual(s2.y, 40)

    def test_str__(self):
        """
        Test the __str__ method.
        """
        s1 = Square(10)
        self.assertEqual(str(s1), "[Square] (78) 0/0 - 10")

        s2 = Square(20, 30, 40)
        self.assertEqual(str(s2), "[Square] (79) 30/40 - 20")

    def test_size(self):
        """
        Test the size property.
        """
        s1 = Square(40)
        self.assertEqual(s1.size, 40)

        s2 = Square(20)
        s2.size = 60
        self.assertEqual(s2.size, 60)

    def test_update(self):
        """
        Test the update method.
        """
        s1 = Square(10)
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

        s2 = Square(10)
        s2.update(size=3)
        self.assertEqual(s2.id, 83)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.x, 0)
        self.assertEqual(s2.y, 0)

        s3 = Square(10)
        s3.update(x=3, y=4)
        self.assertEqual(s3.id, 84)
        self.assertEqual(s3.size, 10)
        self.assertEqual(s3.x, 3)
        self.assertEqual(s3.y, 4)

        s4 = Square(10)
        s4.update(**{"id": 1, "size": 3, "x": 4, "y": 5})
        self.assertEqual(s4.id, 1)
        self.assertEqual(s4.size, 3)
        self.assertEqual(s4.x, 4)
        self.assertEqual(s4.y, 5)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method.
        """
        s1 = Square(10)
        dict_s1 = s1.to_dictionary()
        self.assertEqual(dict_s1["id"], 80)
        self.assertEqual(dict_s1["size"], 10)
        self.assertEqual(dict_s1["x"], 0)
        self.assertEqual(dict_s1["y"], 0)

        s2 = Square(20, 30, 40)
        dict_s2 = s2.to_dictionary()
        self.assertEqual(dict_s2["id"], 81)
        self.assertEqual(dict_s2["size"], 20)
        self.assertEqual(dict_s2["x"], 30)
        self.assertEqual(dict_s2["y"], 40)

    def test_pep8_base(self):
        """Test that the base module conforms to PEP8."""
        style = pep8.StyleGuide()
        result = style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
