import unittest
import os

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test the Base class.
    """

    def test_init(self):
        """
        Test the __init__() method.
        """
        # Test with no id
        base = Base()
        self.assertEqual(base.id, 12)

        # Test with an id
        base = Base(id=2)
        self.assertEqual(base.id, 2)

    def test_to_json_string(self):
        """
        Test the to_json_string() method.
        """
        # Test with no list of dictionaries
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

        # Test with a list of dictionaries
        list_dictionaries = [{"id": 1, "width": 2, "height": 3},
                             {"id": 4, "size": 5}]
        json_string = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_string,
                         "[{\"id\": 1, \"width\": 2, \"height\": 3},"
                         " {\"id\": 4, \"size\": 5}]")

    def test_save_to_file(self):
        """
        Test the save_to_file() method.
        """
        # remove file rectangle that has been created by old tests.
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        # Test with for Rectangle's class
        # no list of objects
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))

        # remove file ectangle that has been created by old tests.
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        # Test with for Rectangle's class
        # an empty list of objects
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))

        # remove file square that has been created by old tests.
        if os.path.exists("Square.json"):
            os.remove("Square.json")

        # Test with for Square's class
        # no list of objects
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))

        # remove file square that has been created by old tests.
        if os.path.exists("Square.json"):
            os.remove("Square.json")

        # Test with for Square's class
        # an empty list of objects
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))

        # VALIDE TESTS
        # Test with a list of rectngle's objects
        R = Rectangle
        list_objects = [R(width=45, height=98), R(width=77, height=88)]
        Rectangle.save_to_file(list_objects)
        self.assertTrue(os.path.exists("Rectangle.json"))

        # Test with a list of rectngle's objects
        list_objects = [Square(size=98), Square(size=88)]
        Square.save_to_file(list_objects)
        self.assertTrue(os.path.exists("Square.json"))

        # Test with a list of rectngle's objects
        list_objects = [Square(1)]
        Square.save_to_file(list_objects)
        self.assertTrue(os.path.exists("Square.json"))
    def test_from_json_string(self):
        """
        Test the from_json_string() method.
        """
        # Test with no json_string case for rectangle
        list_objects = Rectangle.from_json_string(None)
        self.assertEqual(list_objects, [])

        # Test with no json_string case for square
        list_objects = Square.from_json_string(None)
        self.assertEqual(list_objects, [])

        # Test with a json_string case for rectangle
        list_dictionaries = [{"id": 1, "width": 2, "height": 3}]
        json_string = Base.to_json_string(list_dictionaries)
        list_objects = Rectangle.from_json_string(json_string)
        self.assertEqual(list_objects, [{"id": 1, "width": 2, "height": 3}])

        # Test with a json_string case for square
        list_dictionaries = [{"id": 4, "size": 5}]
        json_string = Base.to_json_string(list_dictionaries)
        list_objects = Square.from_json_string(json_string)
        self.assertEqual(list_objects, [{"id": 4, "size": 5}])

    def test_create(self):
        """
        Test the create() method.
        """
        # Test with no dictionary
        rectangle = Rectangle.create()
        self.assertEqual(rectangle, None)

        # Test with a dictionary for a Rectangle
        dictionary = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        rectangle = Rectangle.create(**dictionary)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)

        # Test with a dictionary for a Square
        dictionary = {"id": 1, "size": 4, "x": 5, "y": 6}
        square = Square.create(**dictionary)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 5)
        self.assertEqual(square.y, 6)

    def test_load_from_file(self):
        """
        Test the load_from_file() method.
        """
        # remove file square and rectangle that has been created by old tests.
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

        # Test with a non-existent file using square class
        list_objects = Square.load_from_file()
        self.assertEqual(list_objects, [])

        # Test with a non-existent file using Rectangle class
        list_objects = Rectangle.load_from_file()
        self.assertEqual(list_objects, [])

        # Test with an existing file using square class
        with open("Square.json", "w") as f:
            f.write("[{\"id\": 4, \"size\": 5}]")

        list_objects = Square.load_from_file()
        self.assertEqual(list_objects[0].to_dictionary(),
                         {'id': 4, 'size': 5, 'x': 0, 'y': 0})

        # Test with an existing file using Rectangle class
        with open("Rectangle.json", "w") as f:
            f.write("[{\"id\": 1, \"width\": 2, \"height\": 3}]")

        list_objects = Rectangle.load_from_file()
        self.assertEqual(list_objects[0].to_dictionary(),
                         {"id": 1, "width": 2, "height": 3, 'x': 0, 'y': 0})

    def test_save_to_file_csv(self):
        """
        Test the save_to_file_csv() method.
        """
        # remove file square and rectangle that has been created by old tests.
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")

        # Test with no list of objects for Rectangle class
        Rectangle.save_to_file_csv(None)
        self.assertTrue(os.path.exists("Rectangle.csv"))

        if os.path.exists("Square.csv"):
            os.remove("Square.csv")

        # Test with no list of objects for Square class
        Square.save_to_file_csv(None)
        self.assertTrue(os.path.exists("Square.csv"))

        # Test with a list of objects for Rectangle class
        R = Rectangle
        list_objects = [R(width=22, height=44), R(width=66, height=77)]
        Rectangle.save_to_file_csv(list_objects)
        self.assertTrue(os.path.exists("Rectangle.csv"))

        # Test with a list of objects for Square class
        list_objects = [Square(size=55), Square(size=99)]
        Square.save_to_file_csv(list_objects)
        self.assertTrue(os.path.exists("Square.csv"))

    def test_load_from_file_csv(self):
        """
        Test the load_from_file_csv() method.
        """
        # remove file square and rectangle that has been created by old tests.
        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")

        # Test with a non-existent file for Rectangle class
        list_objects = Rectangle.load_from_file_csv()
        self.assertEqual(list_objects, [])

        # Test with a non-existent file for Square class
        list_objects = Square.load_from_file_csv()
        self.assertEqual(list_objects, [])

        # Test with an existing file for Rectangle class
        with open("Rectangle.csv", "w") as f:
            f.write("1,2,3,4,5\n6,7,8,9,10")

        list_objects = Rectangle.load_from_file_csv()
        dictionaries = map(lambda obj: obj.to_dictionary(), list_objects)
        self.assertEqual(list(dictionaries),
                         [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                          {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}])

        # Test with an existing file for Square class
        with open("Square.csv", "w") as f:
            f.write("2,3,4,5\n7,8,9,10")

        list_objects = Square.load_from_file_csv()
        dictionaries = map(lambda obj: obj.to_dictionary(), list_objects)
        self.assertEqual(list(dictionaries),
                         [{"id": 2, "size": 3, "x": 4, "y": 5},
                          {"id": 7, "size": 8, "x": 9, "y": 10}])


if __name__ == "__main__":
    unittest.main()
