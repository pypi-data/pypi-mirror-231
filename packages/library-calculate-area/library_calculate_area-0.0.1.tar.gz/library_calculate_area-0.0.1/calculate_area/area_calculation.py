import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Абстрактный базовый класс для представления геометрических фигур и выполнения операций с ними.
    """
    @abstractmethod
    def calculate_area(self):
        """
        Абстрактный метод для вычисления площади фигуры.
        """
        pass


class Circle(Shape):
    """
    Класс для представления круга и выполнения операций с ним.
    """

    def __init__(self, radius):
        """
        Создает объект круга с заданным радиусом.

        :param radius: Радиус круга.

        Edge Cases:
            -ValueError: Если радиус отрицательный или нулевой.
        """
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом и больше нуля")
        self.radius = radius

    def calculate_area(self):
        """
        Вычисляет площадь круга с заданным радиусом.

        Returns:
            float: Площадь круга.
        """
        return math.pi * self.radius**2


class Triangle(Shape):
    """
    Класс для представления треугольника и выполнения операций с ним.
    """

    def __init__(self, side_1, side_2, side_3):
        """
        Создает объект треугольника с заданными сторонами.
        Длины сторон должны быть положительным числом.

        Args:
            side_1 (float): Первая длина стороны треугольника.
            side_2 (float): Вторая длина стороны треугольника.
            side_3 (float): Третья длина стороны треугольника.

        Edge Cases:
            - Если все стороны равны, будет создан равносторонний треугольник, но не прямоугольный.
            - Если одна из сторон равна нулю, это также будет считаться несуществующим треугольником.
        """
        if side_1 <= 0 or side_2 <= 0 or side_3 <= 0:
            raise ValueError("Стороны треугольника должны быть положительными числами")
        if (
            side_1 + side_2 <= side_3
            or side_1 + side_3 <= side_2
            or side_2 + side_3 <= side_1
        ):
            raise ValueError("Несуществующий треугольник")
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def calculate_area(self):
        """
        Вычисляет площадь треугольника по формуле Герона.

        Returns:
            float: Площадь треугольника.
        """
        half_meter = (self.side_1 + self.side_2 + self.side_3) / 2
        area = math.sqrt(
            half_meter
            * (half_meter - self.side_1)
            * (half_meter - self.side_2)
            * (half_meter - self.side_3)
        )
        return round(area, 2)

    def right_triangle(self):
        """
        Проверяет, является ли треугольник прямоугольным.

        Returns:
            str: "Треугольник прямоугольный." или "Треугольник не прямоугольный"
        """
        sides = sorted([self.side_1, self.side_2, self.side_3])
        if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
            return "Треугольник прямоугольный"
        else:
            return "Треугольник не прямоугольный"
