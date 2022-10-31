import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

    def test_type(self):
        a = Base()
        self.assertEqual(type(a), Base)

    def test_init(self):
        a = Base()
        tmp = Base(33)
        b = Base()
        self.assertEqual(a.id, 2)
        self.assertEqual(b.id, 3)
        self.assertEqual(tmp.id, 33)

    def test_exception(self):
        with self.assertRaises(TypeError):
            Base(2, "foo")

        c = Base()
        with self.assertRaises(AttributeError):
            print(c.nb_objects)
        with self.assertRaises(AttributeError):
            print(c.__nb_objects)
        with self.assertRaises(AttributeError):
            print(Base.nb_objects)
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_to_json_string(self):
        a = Square(5)
        a_dict = a.to_dictionary()
        b = Square(10)
        b_dict = b.to_dictionary()
        c = Square(15)
        c_dict = c.to_dictionary()
        json_s = Base.to_json_string([a_dict, b_dict, c_dict])
        my_list = ['"size": 5', '"size": 15', '"x": 0']
        for i in my_list:
            self.assertIn(i, json_s)
        
        d = Rectangle(3, 2, id=400)
        d_dict = d.to_dictionary()
        json_s = Base.to_json_string([a_dict, b_dict, d_dict, c_dict])
        self.assertIn('"width"', json_s)

        json_s = Base.to_json_string([])
        self.assertEqual(json_s, "[]")


if __name__ == '__main__':
    unitest.main()
