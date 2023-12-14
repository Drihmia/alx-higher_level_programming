"""Simple unittest module"""
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8


class TestBaseClass(unittest.TestCase):
    def test_to_json_string(self):
        Rectangle(765, 32)
        json_string = Rectangle.to_json_string([{"id": 1}])
        self.assertEqual(json_string, '[{"id": 1}]')

    def test_save_to_file(self):
        b1 = Rectangle(54, 23)
        Rectangle.save_to_file([b1])
        with open("Rectangle.json", "r") as file:
            file_content = file.read()
            st = '[{"id": 2, "width": 54, "height": 23, "x": 0, "y": 0}]'
        self.assertEqual(file_content, st)

    def test_from_json_string(self):
        json_string = '[{"id": 1}]'
        list_of_dicts = Base.from_json_string(json_string)
        self.assertEqual(list_of_dicts, [{'id': 1}])

    @patch('builtins.print')
    def test_create(self, mock_print):
        r1 = Rectangle.create(**{'height': 4, 'width': 10, "id": 1})
        print(str(type(r1)))
        mock_print.assert_called_with('<class \'models.rectangle.Rectangle\'>')

    def test_load_from_file(self):
        with open("Rectangle.json", "w") as file:
            file.write('[{"id": 12}]')
        loaded_instances = Rectangle.load_from_file()
        self.assertEqual(len(loaded_instances), 1)

    def test_save_to_file_csv(self):
        b1 = Rectangle(98, 65)
        Rectangle.save_to_file_csv([b1])
        with open("Rectangle.csv", "r") as file:
            file_content = file.read()
            self.assertEqual(file_content, '3,98,65,0,0\n')

    def test_load_from_file_csv(self):
        with open("Rectangle.csv", "w") as file:
            file.write('1,10,20,30,40\n')
            file.write('2,15,25,35,45\n')


class TestId(unittest.TestCase):
    """simple test unit for id"""

    def test_id(self):
        """Test if id is an integer"""
        b1 = Base()
        self.assertEqual(b1.id, int(5))

        a1 = Rectangle(34, 42)
        self.assertEqual(a1.id, int(6))

        c1 = Square(23, 23)
        self.assertEqual(c1.id, int(7))

        b1 = Base()
        self.assertEqual(b1.id, int(8))

        b1 = Base(32)
        self.assertEqual(b1.id, int(32))

        b1 = Base()
        self.assertEqual(b1.id, int(9))

    def test_pep8_base(self):
        """Test that the base module conforms to PEP8."""
        style = pep8.StyleGuide()
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
