import unittest
import math

from calculate_area.area_calculation import Triangle


class TestTriangle(unittest.TestCase):
    def test_area_triangle(self):
        triangle = Triangle(3, 5, 7)
        self.assertEqual(triangle.calculate_area(), 6.50)

    def test_area_negative_sides(self):
        with self.assertRaises(ValueError):
            triangle1 = Triangle(3, 4, -5)

    def test_area_incorrect_sides(self):
        with self.assertRaises(ValueError):
            triangle2 = Triangle(1, 1, 2)

    def test_right_triangle(self):
        triangle1 = Triangle(3, 4, 5)
        triangle2 = Triangle(5, 12, 13)
        triangle3 = Triangle(3, 3, 3)

        self.assertTrue(triangle1.right_triangle() == "Треугольник прямоугольный")
        self.assertTrue(triangle2.right_triangle() == "Треугольник прямоугольный")
        self.assertTrue(triangle3.right_triangle() == "Треугольник не прямоугольный")


if __name__ == "__main__":
    unittest.main()
