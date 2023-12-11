from models.rectangle import Rectangle
import unittest

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
        with self.assertRaises(TypeError) as context:
            Rectangle("Hello", 5)
        self.assertEqual(str(context.exception), "width must be an integer")

        r2 = Rectangle(9, 3)
        with self.assertRaises(TypeError) as context:
            r2.width = "width must be an integer"
        self.assertEqual(str(context.exception), "width must be an integer")

        r2 = Rectangle(9, 8)
        with self.assertRaises(TypeError) as context:
            r2.height = "height must be an integer"
        self.assertEqual(str(context.exception), "height must be an integer")

        r2 = Rectangle({"Hello": 3}, "Redouane")
        with self.assertRaises(TypeError) as context:
            r2.width = "width must be an integer"
        self.assertEqual(str(context.exception), "width must be an integer")

        r2 = Rectangle(9, {"Redouane": 90})
        with self.assertRaises(TypeError) as context:
            r2.height = "height must be an integer"
        self.assertEqual(str(context.exception), "height must be an integer")

        r2 = Rectangle(["Hello"], "Redouane")
        with self.assertRaises(TypeError) as context:
            r2.width = "width must be an integer"
        self.assertEqual(str(context.exception), "width must be an integer")

        r2 = Rectangle(9, ["Redouane"])
        with self.assertRaises(TypeError) as context:
            r2.height = "height must be an integer"
        self.assertEqual(str(context.exception), "height must be an integer")

        r2 = Rectangle(("Hello",), "Redouane")
        with self.assertRaises(TypeError) as context:
            r2.width = "width must be an integer"
        self.assertEqual(str(context.exception), "width must be an integer")

        r2 = Rectangle(9, ("Redouane",))
        with self.assertRaises(TypeError) as context:
            r2.height = "height must be an integer"
        self.assertEqual(str(context.exception), "height must be an integer")

        r2 = Rectangle(9.1, 0)
        with self.assertRaises(ValueError) as context:
            r2.width = "width must be an integer"
        self.assertEqual(str(context.exception), "width must be an integer")

        r2 = Rectangle(0, 0)
        with self.assertRaises(ValueError) as context:
            r2.width = "width must be > 0"
        self.assertEqual(str(context.exception), "width must be > 0")

        r2 = Rectangle(-9, 0)
        with self.assertRaises(ValueError) as context:
            r2.width = "width must be > 0"
        self.assertEqual(str(context.exception), "width must be > 0")

        r2 = Rectangle(1, -8)
        with self.assertRaises(ValueError) as context:
            r2.height = "height must be > 0"
        self.assertEqual(str(context.exception), "height must be > 0")

        r2 = Rectangle(1, -8)
        with self.assertRaises(ValueError) as context:
            r2.height = "height must be > 0"
        self.assertEqual(str(context.exception), "height must be > 0")

        r2 = Rectangle(1, 2.1)
        with self.assertRaises(ValueError) as context:
            r2.height = "height must be an integer"
        self.assertEqual(str(context.exception), "height must be an integer")

        r2 = Rectangle(43, 21, 2.1, 0)
        with self.assertRaises(TypeError) as context:
            r2.x = "x must be an integer"
        self.assertEqual(str(context.exception), "x must be an integer")

        r2 = Rectangle(43, 2, 'c', 2)
        with self.assertRaises(TypeError) as context:
            r2.x = "x must be an integer"
        self.assertEqual(str(context.exception), "x must be an integer")

        r2 = Rectangle(43, 2, 2.1, 0)
        with self.assertRaises(TypeError) as context:
            r2.y = "y must be an integer"
        self.assertEqual(str(context.exception), "y must be an integer")

        r2 = Rectangle(43, 2.1, 4, 'y')
        with self.assertRaises(TypeError) as context:
            r2.y = "y must be an integer"
        self.assertEqual(str(context.exception), "y must be an integer")

        r2 = Rectangle(43, 2.1, 4, -2)
        with self.assertRaises(ValueError) as context:
            r2.y = "y must be >= 0"
        self.assertEqual(str(context.exception), "y must be >= 0")

        r2 = Rectangle(43, 2.1, -4, 0)
        with self.assertRaises(ValueError) as context:
            r2.x = "x must be >= 0"
        self.assertEqual(str(context.exception), "x must be >= 0")

if __name__ == "__main__":
    unittest.main()

