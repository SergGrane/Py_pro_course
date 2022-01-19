# Реализуйте генераторную функцию, которая будет возвращать по одному члену числовой последовательности,
# закон которой задается с помощью пользовательской функции. Кроме этого параметром генераторной функции
# должны быть значение первого члена прогрессии и количество выдаваемых членов последовательности (n). Г
# енератор должен остановить свою работу или по достижению n — го члена , или при передаче команды на завершение

def exp(j: int, a: int):
    """
    exponentiation with exponent
    :param j: number
    :param a: exponent
    :return: exponentiation
    """
    return j**a


def arifm(j: int, a: int):
    """
    sum numbers
    :param j: number1
    :param a: number2
    :return: sum
    """
    return j+a


def geom(j: int, a: int):
    """
    multiplication of 2 numbers
    :param j: number1
    :param a: number2
    :return: multiplication
    """
    return j*a


def gen_numbseq(first: int, end: int, a: int, func):
    """
    Get the multisequence member
    :param first: begin the seq
    :param end: end of seq
    :param a: param of seq
    :param func: name of seq function
    :return: member of seq
    """
    if not isinstance(first, int) or not isinstance(end, int) or not isinstance(a, int):
        raise TypeError('type of parameter is wrong')
    while first <= end:
        yield func(first, a)
        first += 1
    return None


try:
    x = gen_numbseq(0, 5, 3, arifm)
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
except Exception as err:
    print(err)
