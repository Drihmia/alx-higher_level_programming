import unittest
from models.rectangle import Rectangle

class TestId(unittest.TestCase):
    def test_width_and_height_normal(self):
        r1 = Rectangle(12, 13)
        self.assertEqual(r1.width, 12)
        self.assertEqual(getattr(r1, "width"), 12)
        self.assertEqual(r1.height, 13)
        self.assertEqual(getattr(r1, "height"), 13)

        r1.width = 2
        r1.height = 3
        self.assertEqual(r1.width, 2)
        self.assertEqual(getattr(r1, "width"), 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(getattr(r1, "height"), 3)

        setattr(r1, "height", 32)
        setattr(r1, "width", 23)
        self.assertEqual(r1.width, 23)
        self.assertEqual(getattr(r1, "width"), 23)
        self.assertEqual(r1.height, 32)
        self.assertEqual(getattr(r1, "height"), 32)

    def test_width_and_height_chars(self):
        """Testing for character values"""

        # TypeError for both width and height
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Hello", 5)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, "Redouane")

        # TypeError for dict
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"Hello": 3}, "Redouane")

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, {"Redouane": 90})

        # TypeError for list
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(["Hello"], "Redouane")

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, ["Redouane"])

        # TypeError for tuple
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(("Hello",), "Redouane")

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, ("Redouane",))

        # TypeError for float
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(9.1, 0)

        # ValueError for Width
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 0)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-9, 0)

        # ValueError for Height
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -8)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 2.1)

        # TypeError for X
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(43, 21, 2.1, 0)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(43, 2, 'c', 2)

        # TypeError for Y
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(43, 2, 2, 2.1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(43, 2, 4, 'y')

        # ValueError for Y
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(43, 2, 4, -2)

        # ValueError for X
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(43, 2, -4, 0)

if __name__ == "__main__":
    unittest.main()

