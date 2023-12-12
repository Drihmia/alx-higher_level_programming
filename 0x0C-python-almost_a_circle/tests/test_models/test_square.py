import unittest
from models.square import Square


class TestId(unittest.TestCase):
    def test_size_and_normal(self):
        r1 = Square(12, 13)
        self.assertEqual(r1.size, 12)
        self.assertEqual(getattr(r1, "size"), 12)

        r1.size = 2
        r1.height = 3
        self.assertEqual(r1.size, 2)
        self.assertEqual(getattr(r1, "size"), 2)

        setattr(r1, "size", 23)
        self.assertEqual(r1.size, 23)
        self.assertEqual(getattr(r1, "size"), 23)

    def test_size_and_size_chars(self):
        """Testing for character values"""

        # TypeError for both size and height
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("Hello")

        # TypeError for float
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(9.1)

        # ValueError for Width
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-9)

        # TypeError for X
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(43, 2.1, 0)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(43, 'c', 2)

        # TypeError for Y
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(43, 2, 2.1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(43, 4, 'y')

        # ValueError for Y
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(43, 4, -2)

        # ValueError for X
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(43, -4, 0)


if __name__ == "__main__":
    unittest.main()
