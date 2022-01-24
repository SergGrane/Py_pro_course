#   Для класса Box напишите статический метод, который будет подсчитывать суммарный объем двух ящиков,
#   которые будут его параметрами

class Cube:
    """
    Cube class
    """

    def __init__(self, a: (int, float), b: (int, float), c: (int, float)):
        """
        Initial of Cube class
        :param a: side
        :param b: side
        :param c: side
        """

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
            raise TypeError
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'a = {self.a} b = {self.b} c = {self.c} volume = {self.a * self.b * self.c}'

    @staticmethod
    def cube_sum(a1, b1, c1, a2, b2, c2):
        """
        sum of 2 cubes volumes
        :param a1: int ot float
        :param b1: int ot float
        :param c1: int ot float
        :param a2: int ot float
        :param b2: int ot float
        :param c2: int ot float
        :return: sum of volumes
        """
        if not isinstance(a1, (int, float)) or not isinstance(b1, (int, float)) or not isinstance(c1, (int, float))\
                or not isinstance(a2, (int, float)) or not isinstance(b2, (int, float)) or not isinstance(c2, (int, float)):
            raise TypeError
        return a1 * b1 * c1 + a2 * b2 * c2


if __name__ == "__main__":
    c1 = Cube(2, 3, 4)
    print(c1)
    print(c1.cube_sum(1, 2, 3, 4, 5, 6))
