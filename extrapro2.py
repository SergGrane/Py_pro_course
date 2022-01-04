# Create a class called Rational for performing arithmetic with fractions. Write a program to test your class.
# Use integer variables to represent the private data of the class – the numerator and the denominator.
# Provide a init() method that enables an object of this class to be initialized when it’s declared.
# The init() should contain default parameter values in case no initializers are provided and should
# store the fraction in reduced form.
# For example, the fraction 2/4 would be stored in the object as 1 in the numerator and 2 in the denominator.
# Provide public methods that perform each of the following tasks:
# - printing Rational numbers in the form a/b, where a is the numerator and b is the denominator.
# - printing Rational numbers in floating-point format.
import math


class Rational:

    """
    performing arithmetic with fractions
    """

    def __init__(self, numerator=1, denominator=1):
        k = math.gcd(numerator, denominator)
        self._numerator = numerator/k
        self._denominator = denominator/k

    def __str__(self):
        res = 'Fraction : ' + str(int(self._numerator)) + '/' + str(int(self._denominator))
        return res + '\n' + 'or ' + str(self._numerator/self._denominator)


if __name__ == '__main__':
    try:
        rat1 = Rational(12, 0)
        print(rat1)
    except Exception as error:
        print('Error : ', error)


