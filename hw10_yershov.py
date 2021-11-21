# Создать классы Point и Circle, отнаследованные от класса Shape. В классе Shape хранятся только координаты центра
# фигуры.
#
# Создать в классе Circle метод contains, который принимает в качестве параметра точку (экземпляр класса Point) и
# проверяет находится ли данная точка внутри окружности. Координаты центра окружности и точки могут быть произвольными.
# Если точка попадает на окружность, то это считается вхождением.
#
# p = Point(1, 42)
# c = Circle(0, 0, 10)
# c.contains(p) # False
#
# * Для класса Circle переопределить оператор in так чтоб от выполнял те же действия, что и функция contains и можно
# было написать:
#
# p in c

class Shape:
    def __init__(self, x, y):
        for coord in [x, y]:
            if not isinstance(coord, int | float):
                raise TypeError

        self.x = x
        self.y = y


class Point(Shape):

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __contains__(self, item):
        if not isinstance(item, Point):
            raise TypeError

        return (item.get_x() - self.x) ** 2 + (item.get_y() - self.y) ** 2 <= self.radius ** 2

    def contains(self, point):
        """
        Checks if the point is inside the circle.

        :param point: Point-class object
        :type point: Point
        :return: True if the point is inside the circle or False if the point is outside
        :rtype: bool
        """
        if not isinstance(point, Point):
            raise TypeError

        return (point.get_x() - self.x) ** 2 + (point.get_y() - self.y) ** 2 <= self.radius ** 2


p = Point(1, 42)
c = Circle(0, 0, 10)

print(c.contains(p))
print(p in c)

print(Circle(0, 0, 10).contains(Point(1, 42)))
print(Point(1, 42) in Circle(0, 0, 10))
