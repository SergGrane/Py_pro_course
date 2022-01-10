# 1) Создайте класс  «Прямоугольник», у которого присутствуют два поля (ширина и высота).
# Реализуйте метод сравнения прямоугольников по площади. Также реализуйте методы сложения прямоугольников
# (площадь суммарного прямоугольника должна быть равна сумме площадей прямоугольников, которые вы складываете).
# Реализуйте методы умножения прямоугольника на число n (это должно увеличить площадь базового прямоугольника в n раз).


class Rectangle:
    """
    descibes rectangle
    """

    def __init__(self, length, width):
        if length <= 0 and width <= 0:
            raise ValueError('length, width must be > 0')
        self.length = length
        self.width = width

    def __str__(self):
        return f'Rect: len is {self.length } width is {self.width} square is {self.square()}\n'

    def perim(self):
        return self.width * 2 + self.length * 2

    def square(self):
        return self.width * self.length

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.square() == other.square()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Rectangle):
            return self.square() != other.square()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.square() > other.square()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.square() < other.square()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Rectangle):
            return self.square() >= other.square()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.square() <= other.square()
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return Rectangle(self.square() * other/self.width, self.width)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle((self.square() + other.square())/self.width, self.width)
        return NotImplemented

    def __iadd__(self, other):
        self.length = (self.square() + other.square())/self.width
        self.width = self.width
        return self

    def __radd__(self, other):
        if isinstance(other, int):
            return Rectangle ((self.square() + other)/self.width, self.width )
        return NotImplemented


if __name__ == '__main__':
    rect1 = Rectangle(10, 20)
    rect2 = Rectangle(5, 5)
    rect3 = rect1 + rect2

    rect4 = rect1 * 3
    s = rect1 > rect2
    print(s)

    print(rect1, rect2, rect3, rect4)
    rect4 += rect1
    print('\n', rect4)
