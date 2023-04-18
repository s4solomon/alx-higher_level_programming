#!/usr/bin/python3
"""Module for test Base class"""
import json
import unittest

from models import base


class TestBase(unittest.TestCase):
    """Test for Base class"""

    def test_doc_module(self):
        """Module has documentation"""
        doc = base.Base.__doc__
        self.assertGreater(len(doc), 1)

    def test_doc_class(self):
        """Base class has documentation"""
        doc = base.Base.__doc__
        self.assertGreater(len(doc), 1)

    def test_doc_constructor(self):
        """Constructor has documentation"""
        doc = base.Base.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_extra_arguments(self):
        """Pass extra arguments"""
        with self.assertRaises(TypeError):
            base.Base(12, 12)

        with self.assertRaises(TypeError):
            base.Base("hello", 12, 34)

    def test_generate_multiple_bases(self):
        """Create multiple instances"""

        b1 = base.Base()
        self.assertEqual(b1.id, 1)

        b2 = base.Base()
        self.assertEqual(b2.id, 2)

        b3 = base.Base()
        self.assertEqual(b3.id, 3)

        b4 = base.Base(12)
        self.assertEqual(b4.id, 12)

        b5 = base.Base()
        self.assertEqual(b5.id, 4)

        nb_objects = 4
        for i in range(5, 10):
            # id_base is i if i is even, otherwise None
            id_base = i if i % 2 == 0 else None

            with self.subTest(i=i):
                b = base.Base(id_base)
                if i % 2 != 0:
                    nb_objects += 1
                    id_base = nb_objects

                self.assertIs(b.id, id_base)

    def test_get_id(self):
        """Get the id of an instance"""
        b = base.Base(12)
        self.assertIs(b.id, 12)

    def test_attribute_not_exists(self):
        """Get an attribute that doesn't exists"""
        b = base.Base(14)
        with self.assertRaises(AttributeError):
            print(b.size)

    def test_class_attributes(self):
        """Check class attributes"""
        b = base.Base(1001)

        with self.assertRaises(AttributeError):
            print(b.nb_objects)

        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def test_simple_string(self):
        """Simple json string"""
        d1 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        d2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        json_s = base.Base.to_json_string([d1, d2])

        self.assertTrue(type(json_s) is str)

        d = json.loads(json_s)

        self.assertEqual(d, [d1, d2])

    def test_dictionary(self):
        """Test dictionary"""
        b = base.Base(12)

    def test_2_json(self):
        """Static method 2 json"""
        from models.rectangle import Rectangle

        rect = Rectangle(10, 7, 2, 8, 1)
        dictionary = rect.to_dictionary()

        json_dict = base.Base.to_json_string([dictionary])
        json_sorted = sorted(json_dict)
        exp_json = json.dumps([{"x": 2, "width": 10, "id": 1,
                                "height": 7, "y": 8}])
        self.assertEqual(json_sorted, sorted(exp_json))

        json_dict = base.Base.to_json_string([dictionary, dictionary])
        json_sorted = sorted(json_dict)
        exp_json = json.dumps([{"x": 2, "width": 10, "id": 1,
                                "height": 7, "y": 8},
                               {"x": 2, "width": 10, "id": 1,
                                "height": 7, "y": 8}])
        self.assertEqual(json_sorted, sorted(exp_json))

        json_dict = base.Base.to_json_string(None)
        self.assertEqual(json_dict, "[]")

        json_dict = base.Base.to_json_string([])
        self.assertEqual(json_dict, "[]")

        with self.assertRaises(TypeError):
            base.Base.to_json_string([dictionary], 12)

    def test_empty_to_json_string(self):
        """Test for passing empty list/ None"""

        json_s = base.Base.to_json_string([])

        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_None_to_json_String(self):
        json_s = base.Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_from_json_string(self):
        """Tests regular from_json_string"""

        json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
{"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_l = base.Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(json_l[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})

    def test_fjs_empty(self):
        """Tests from_json_string with an empty string"""
        self.assertEqual([], base.Base.from_json_string(""))

    def test_fjs_None(self):
        """Tests from_json_string with an empty string"""
        self.assertEqual([], base.Base.from_json_string(None))

    @staticmethod
    def write_expected(name, contents):
        """Write the expected output in a json file"""
        contents = json.dumps(contents)
        with open(name, 'w') as f:
            f.write(contents)

    @staticmethod
    def open_json(name):
        """Open a json file"""
        with open(name) as f:
            return sorted(f.read())

    def test_save_to_file(self):
        """Save the json string in a file"""
        from models.rectangle import Rectangle
        from models.square import Square
        import filecmp

        with self.subTest(i=0, msg="Empty list"):
            Rectangle.save_to_file(None)
            TestBase.write_expected('expected.json', [])

            self.assertTrue(filecmp.cmp('Rectangle.json', 'expected.json'))

        with self.subTest(i=1, msg="Two elements in the list"):
            r1 = Rectangle(10, 7, 2, 8, 3)
            r2 = Rectangle(2, 4, 6, 9, 15)

            expected = [{"y": 8, "x": 2, "id": 3, "width": 10, "height": 7},
                        {"y": 9, "x": 6, "id": 15, "width": 2, "height": 4}]

            Rectangle.save_to_file([r1, r2])
            TestBase.write_expected('expected.json', expected)
            got = TestBase.open_json('Rectangle.json')
            exp = TestBase.open_json('expected.json')

            self.assertEqual(got, exp)

        with self.subTest(i=2, msg="Rectangle and square in the list"):
            s = Square(12, 2, 5, 55)

            expected = [{"y": 5, "id": 55, "x": 2, "size": 12}]

            Square.save_to_file([s])
            TestBase.write_expected('expected.json', expected)
            got = TestBase.open_json('Square.json')
            exp = TestBase.open_json('expected.json')

            self.assertEqual(got, exp)


if __name__ == '__main__':
    unittest.main()
