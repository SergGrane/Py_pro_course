
# Создайте класс «Правильная дробь» и реализуйте методы сравнения, сложения, вычитания и произведения
# для экземпляров этого класса.

import math


class Rational:

    """
    performing arithmetic with fractions
    """

    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int)  or not isinstance(denominator, int):
            raise ValueError
        if denominator == 0:
            raise ValueError('Denominator = 0')
        k = math.gcd(numerator, denominator)
        self.numerator = int(numerator/k)
        self.denominator = int(denominator/k)

    def __str__(self):
        return f'Fraction: {self.numerator}/{self.denominator}  or {self.flo()}'

    def flo(self):
        return self.numerator/self.denominator

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.flo() == other.flo()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Rational):
            return self.flo() != other.flo()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Rational):
            return self.flo() > other.flo()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Rational):
            return self.flo() < other.flo()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Rational):
            return self.flo() >= other.flo()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Rational):
            return self.flo() <= other.flo()
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(int(self.numerator*other.denominator+other.numerator*self.denominator),
                            int(self.denominator * other.denominator))
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Rational):
            print(self.numerator * other.denominator + other.numerator * self.denominator)
            print(self.denominator * other.denominator)
            self.numerator = int(self.numerator * other.denominator + other.numerator * self.denominator)
            self.denominator = int(self.denominator * other.denominator)
        return self

    def __radd__(self, other:int):
        if isinstance(other, int):
               return Rational(int(self.numerator + other * self.denominator),
                               int(self.denominator))
        return NotImplemented

    def __sub__(self, other):

        if isinstance(other, Rational):
            return Rational(int(self.numerator * other.denominator-other.numerator * self.denominator),
                            int(self.denominator * other.denominator))
        return NotImplemented

    def __isub__(self, other):

        if isinstance(other, Rational):
            self.numerator = int(self.numerator * other.denominator-other.numerator * self.denominator)
            self.denominator = int(self.denominator * other.denominator)
        return self

    def __rsub__(self, other):

        if isinstance(other, int):
            return Rational(int(other * self.denominator - self.numerator),
                            int(self.denominator))
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(int(self.numerator * other.numerator),
                            int(self.denominator * other.denominator))
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, Rational):
            print(self.numerator * other.numerator)
            print(self.denominator * other.denominator)
            self.numerator = int(self.numerator * other.numerator)
            self.denominator = int(self.denominator * other.denominator)
        return self

    def __rmul__(self, other:int):
        if isinstance(other, int):
            return Rational(int(self.numerator * other),
                            int(self.denominator))
        return NotImplemented


if __name__ == '__main__':
    try:
        rat1 = Rational(-3, 2)
        rat2 = Rational(1, 2)
        a = rat2 <= rat1
        print(a)
        rat1 -= rat2
        rat1 = 3 * rat1
        print(rat1, rat2)
        rat3 = 4 + rat1
        print(rat3)

    except Exception as error:
        print('Error : ', error)


