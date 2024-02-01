#!/usr/bin/env python
import unittest


class MyTestCase(unittest.TestCase):
    def test_int_be_mutable(self):
        a = 2
        b = a
        a = 3

        self.assertIsInstance(a, int)
        self.assertNotEqual(a, b)

    def test_float_be_mutable(self):
        a = 2.2
        b = a
        a = 3.1

        self.assertIsInstance(a, float)
        self.assertNotEqual(a, b)

    def test_str_be_mutable(self):
        a = "string"
        b = a
        a = "string2"

        self.assertIsInstance(a, str)
        self.assertNotEqual(a, b)

    def test_list_be_mutable(self):
        a = [0, 3, 5]
        b = a
        a = [2, 3, 5]

        self.assertIsInstance(a, list)
        self.assertNotEqual(a, b)

        a[0] = 0

        self.assertEqual(a, b)

    def test_tuple_be_immutable(self):
        a = (0, 3, 5)
        b = a
        a = (2, 3, 5)

        self.assertIsInstance(a, tuple)
        self.assertNotEqual(a, b)

        with self.assertRaises(TypeError):
            a[0] = 0

    def test_dict_be_mutable(self):
        a = {"test": 3, "test2": 4, "test3": 5}
        b = a
        a = {"a": 1, "b": 2, "c": 3}

        self.assertIsInstance(a, dict)
        self.assertNotEqual(a, b)

        c = {"a": 0, "b": 2, "c": 3}

        a["a"] = 0

        self.assertDictEqual(a, c)


if __name__ == '__main__':
    unittest.main()
