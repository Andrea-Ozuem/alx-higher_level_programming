import unittest
from models.rectangle import Rectangle
"""Test Rctangle properties"""



class TestRectangle(unittest.TestCase):
    def test_area(self):  
        r = Rectangle(10, 2, 3, 2)
        self.assertEqual(r.area(), 20)
    def test_offsets(self):
        r = Rectangle(3, 2, 1, 2)
        self.assertEqual(r.x, 1)
        r.x = 3
        self.assertEqual(r.x, 3)
    def test_except(self):
        with self.assertRaises(ValueError):
           Rectangle(10, 0, 2, 3).area()
        with self.assertRaises(TypeError):
           Rectangle(10, 9, [], 3)

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        pass
