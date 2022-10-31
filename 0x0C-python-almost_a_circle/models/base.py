#!/usr/bin/python3
"""
This is 'base' module.
Functions and Classes:
    class Base()
"""


class Base():
    """
    Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        import json

        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        my_list = []

        if list_objs:
            for item in list_objs:
                if isinstance(item, Base):
                    d = item.to_dictionary()
                    my_list.append(d)

        json_s = Base.to_json_string(my_list)
        with open(filename, "w", encoding="UTF-8") as f:
            f.write(json_s)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        import json

        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if dictionary:

            # initialize a dummy instance
            if cls is Base:
                tmp = cls()
            else:
                tmp = cls(1, 1, 1)

            if isinstance(tmp, Base):
                tmp.update(**dictionary)
            return tmp

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        my_list = []

        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="UTF-8") as f:
                content = f.read()
        except FileNotFoundError:
            return my_list

        json_list = Base.from_json_string(content)
        if json_list:
            for d in json_list:
                my_list.append(cls.create(**d))

        return my_list
