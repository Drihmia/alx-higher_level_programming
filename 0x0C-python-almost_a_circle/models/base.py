#!/usr/bin/python3
"""
This module contains a class called Base
"""
import json
import turtle


class Base:
    """
    This class will be the “base” of all other classes in this project.

    Attributes:
        nb_objects : private class attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        A method that returns the JSON string representation
            of list_dictionaries.
        """
        if list_dictionaries is None or type(list_dictionaries) is not list\
                or len(list_dictionaries) == 0:
            return "[]"

        list_dict_copy = []
        for dct in list_dictionaries:
            if type(dct) is dict:
                list_dict_copy.append(dct)

        st = "["
        for dict_l in list_dict_copy:
            st += json.dumps(dict_l) + ", "
        return st[:-2] + "]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        A class method that writes the JSON string representation of
        list_objs to a file.

        attrs:
        - list_objs (list): a list of instances who inherits of Base.
        - example: list of Rectangle or list of Square instances.

        Name of the file is <Class name>.json - example: Rectangle.json

        """
        a = 1
        lst_dc = []
        if list_objs is None:
            list_objs = []
        for objcet in list_objs:
            if not type(objcet) is cls:
                a = 0
                break
        if a:
            lst_dc = [obj.to_dictionary() for obj in list_objs]
        StringListDictionaries = Base.to_json_string(lst_dc)

        file_name = f"{cls.__name__}.json"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(StringListDictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        A staticmethod that returns the list of the JSON string
            representation json_string.
        attrs:
            json_string (str): a string representing a list of dictionaries.
        Note:
            If json_string is None or empty, an empty list will be returned.
        """
        if type(json_string) is not str or len(json_string) == 0:
            return []

        # checking if json_string has the correct syntax.
        json_obj = []
        try:
            json_obj = json.loads(json_string)
        except Exception as e:
            print("error from_json_string_Base: ", e,
                  " - to be set right later")
        return json_obj

    @classmethod
    def create(cls, **dictionary):
        """ A classmethod that create and return a new instance with
            all attributes already set.

        attrs:
            dictionary : a group of key-worded parameters.
            that should contain for:
            -Rectangle: id, widht, height, x and y, id (optional)
            -Square: id, size, x and y, id (optional)

        """
        if dictionary is None or len(dictionary) == 0:
            return None

        if cls.__name__ == "Rectangle":
            list_d = ["id", "width", "height", "x", "y"]
            list_d_mandatory = ["width", "height"]
        elif cls.__name__ == "Square":
            list_d = ["id", "size", "x", "y"]
            list_d_mandatory = ["size"]
        else:
            list_d_mandatory = []
            list_d = []

        # check if the minimum of positional argument are given.
        for mand in list_d_mandatory:
            if mand not in dictionary:
                return None

        # check if key in dictionary is a actual argument of that object.
        for key in dictionary:
            if key not in list_d:
                return None

        dummy = cls(1, 1)
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
        A classmethod that returns a list of instances:
        Notes:

           - The filename will be: <Class name>.json - example: Rectangle.json
           - If the file doesn't exist, an empty list will be returned.
        """
        file_name = "{}.json".format(cls.__name__)
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                list_dict_str = f.read()
        except (FileNotFoundError, FileExistsError):
            return []
        list_dict_obj = cls.from_json_string(list_dict_str)
        list_objs = [cls.create(**di) for di in list_dict_obj]
        return list_objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        A class method that serializes into a CSV file.
        Note:
            - The file name will be as : <Class name>.csv
                - example: Rectangle.csv
        """
        if list_objs is None:
            list_objs = []

        # making a list of dictionaries from list of objects/instances.
        lst_dc = [obj.to_dictionary() for obj in list_objs]

        # extracting the values of each dictionary as string that consiste
        # of list of values in each line.

        if cls.__name__ == "Rectangle":
            list_d = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            list_d = ["id", "size", "x", "y"]
        else:
            list_d = []

        st_lines = ""
        for dic in lst_dc:
            for key in list_d:
                st_lines += "{},".format(dic[key])
            st_lines = st_lines[:-1] + "\n"

        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as csvfile:
            csvfile.write(st_lines)

    @classmethod
    def load_from_file_csv(cls):
        """
        A class method that deserializes fr'm a CSV file.
        """
        try:
            with open(cls.__name__ + ".csv", "r", encoding="utf-8") as csvfile:
                list_csv = csvfile.read().split("\n")

        except (FileNotFoundError, FileExistsError):
            list_csv = []

        if cls.__name__ == "Rectangle":
            list_d = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            list_d = ["id", "size", "x", "y"]
        else:
            list_d = []

        list_d_csv = []
        for row in list_csv:
            if len(row) == 0:
                continue
            row = row.split(",")
            try:
                dic_csv = {list_d[i]: int(row[i]) for i in range(len(row))}
            except Exception as e:
                dic_csv = {}
                print(e)
            list_d_csv.append(dic_csv)

        return [cls.create(**final) for final in list_d_csv]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        A static method that opens a window and draws all
        the Rectangles and Squares.

        attrs:
            -list of rectangle's instances.
            -list of square's instances.
        """
        screen = turtle.Screen()
        # screen.bgcolor("blue")
        screen.setup(width=1.0, height=1.0, startx=0, starty=0)
        screen.screensize()

        if list_rectangles is None or len(list_rectangles) == 0:
            list_rectangles = []
        if list_squares is None or len(list_squares) == 0:
            list_squares = []
        list_rect_cpy = []
        for obj_rect in list_rectangles:
            if type(obj_rect).__name__ == "Rectangle":
                list_rect_cpy.append(obj_rect)

        list_sqrt_cpy = []
        for obj_sqrt in list_squares:
            if type(obj_sqrt).__name__ == "Square":
                list_sqrt_cpy.append(obj_sqrt)

        [Base.draw_rectangle(**(rect_obj.to_dictionary()))
         for rect_obj in list_rectangles]
        [Base.draw_rectangle(**(sqrt_obj.to_dictionary()))
         for sqrt_obj in list_squares]
        turtle.done()

    @staticmethod
    def draw_rectangle(**dictionary):
        """
        A static helper method that draw a rectangle to the screen.

        attrs:
            **dictionary : a group of key-worded parameters.
            that should contain for:
            -Rectangle: id, widht, height, x and y, id (optional)
            -Square: id, size, x and y, id (optional)
        """
        pen_size = 1
        if "size" in dictionary:
            w, h = dictionary["size"], dictionary["size"]
            color = "green"
        elif "width" in dictionary and "height" in dictionary:
            w, h = dictionary["width"], dictionary["height"]
            color = "red"
        else:
            return

        y, x = dictionary["y"], dictionary["x"]

        t = turtle.Turtle()
        t.pen(fillcolor=color, pencolor="green", pensize=pen_size,
              resizemode="auto", outline=pen_size, speed=3)
        t.penup()
        t.setposition(x, y)
        t.pendown()

        t.setposition(x, y)
        t.begin_fill()
        for _ in range(2):
            t.forward(w)
            t.left(90)
            t.forward(h)
            t.left(90)
        t.end_fill()

        t.penup()
        t.setposition(0, 0)
        t.pendown()
