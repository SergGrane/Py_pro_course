#   Создайте декоратор с параметрами для проведения хронометража работы той или иной функции.
#   Параметрами должны выступать то, сколько раз нужно запустить декорируемую функцию и в какой файл
#   сохранить результаты хронометража. Цель - провести хронометраж декорируемой функции

import time


def dec(n: int, fil: str):
    """
    Decorator of function chronometration
    :param n: number of steps
    :param fil: name of output file
    :return: result of function
    """
    def dec1(f):
        def dec2(*args):
            try:
                fil1 = open(fil + ".txt", 'w')
            except Exception as err:
                fil1.close()
                print(err)
            for i in range(n):
                start = time.time()
                res = f(*args)
                finish = time.time()
                fil1.write(f'Start: {start} Finish: {finish} \n')
            fil1.close()
            return res
        return dec2
    return dec1


@dec(10, 'test')
def suma(a: int, b: int):
    """
    sum of two int numbers
    :param a:
    :param b:
    :return: sum
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError
    return a + b


if __name__ == "__main__":
    print(suma(2, 3))

