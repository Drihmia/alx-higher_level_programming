import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBaseClass(unittest.TestCase):
    def test_to_json_string(self):
        b1 = Rectangle(765, 32)
        json_string = Rectangle.to_json_string([{"id": 1}])
        self.assertEqual(json_string, '[{"id": 1}]')

    def test_save_to_file(self):
        b1 = Rectangle(54, 23)
        Rectangle.save_to_file([b1])
        with open("Rectangle.json", "r") as file:
            file_content = file.read()
            self.assertEqual(file_content, '[{"id": 4, "width": 54, "height": 23, "x": 0, "y": 0}]')

    def test_from_json_string(self):
        json_string = '[{"id": 1}]'
        list_of_dicts = Base.from_json_string(json_string)
        self.assertEqual(list_of_dicts, [{'id': 1}])

    def test_create(self):
        r1 = Rectangle.create(**{'height': 4, 'width': 10, "id": 1})
        print(type(r1))

    def test_load_from_file(self):
        with open("Rectangle.json", "w") as file:
            file.write('[{"id": 1}]')
        loaded_instances = Rectangle.load_from_file()
        self.assertEqual(len(loaded_instances), 1)

    def test_save_to_file_csv(self):
        b1 = Rectangle(98, 65)
        Rectangle.save_to_file_csv([b1])
        with open("Rectangle.csv", "r") as file:
           file_content = file.read()
           self.assertEqual(file_content, '5,98,65,0,0\n')

    def test_load_from_file_csv(self):
       with open("Rectangle.csv", "w") as file:
           file.write('1,10,20,30,40\n')  # Instance 1 data
           file.write('2,15,25,35,45\n')  # Instance 2 data

       loaded_instances = Rectangle.load_from_file_csv()

if __name__ == '__main__':
    unittest.main()

