import unittest
import math

from calculate_area.area_calculation import Circle


class TestCircle(unittest.TestCase):
    def test_area_circle(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.calculate_area(), math.pi * 5**2, places=2)

    def test_area_zero_and_negative_radios(self):
        for radius in [0, -2]:
            with self.subTest(radius=radius):
                with self.assertRaises(ValueError):
                    circle = Circle(radius)


if __name__ == "__main__":
    unittest.main()
