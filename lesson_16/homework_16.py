import math
from abc import ABC, abstractmethod


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

def test_teamlead_attributes():
    tl = TeamLead("Alice", 5000, "Engineering", "Python", 5)

    assert hasattr(tl, "name")
    assert hasattr(tl, "salary")
    assert hasattr(tl, "department")
    assert hasattr(tl, "programming_language")
    assert hasattr(tl, "team_size")



class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def area(self):
        s = (self.__a + self.__b + self.__c) / 2
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

    def perimeter(self):
        return self.__a + self.__b + self.__c


figures = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]

for f in figures:
    print(f"{f.__class__.__name__}: area_square = {f.area():.2f}, perimetr = {f.perimeter():.2f}")