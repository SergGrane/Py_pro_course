
def geom_prog(a: int, limit: int):
    """
    Generator of geometric progression
    :param a: factor
    :param limit: limit
    :return:
    """
    if not isinstance(a, int) or not isinstance(limit, int):
        raise TypeError('All the arguments must be integer')
    i = 1
    while i <= limit:
        yield i * a
        i += 1
    return


def primes(n: int):
    """
    Generator of a prime numbers
    :param n: limit of the primes
    :return:
    """
    if not isinstance(n, int):
        raise TypeError('All the arguments must be integer')
    if n < 0:
        raise ValueError('Limit must be >0')
    i = 2
    while i <= n:
        yield i
        i += 1
    return


def my_range(start: int, stop: int, step: int):
    """
    Generator of the range
    :param start:
    :param stop:
    :param step:
    :return:
    """
    if not isinstance(stop, int) or not isinstance(step, int):
        raise TypeError('All the arguments must be integer')

    while start < stop:
        start += step
        yield start
    return


def str_cube(y: int, num: int):
    """
    Generator of the cubes
    :param y: start
    :param num: limit
    :return: list of the cubes
    """
    if not isinstance(y, int) or not isinstance(num, int):
        raise TypeError('All the arguments must be integer')
    res = [x**3 for x in range(y, num)]
    return res


if __name__ == '__main__':

    print('cube ', str_cube(2, 5))

    g = my_range(0, 20, 1)
    print('range ')
    print(next(g))
    print(next(g))

    s = geom_prog(3, 6)
    print('Geom progress ')

    for j in range(3):
        if j == 3:
            s.close()
        print(next(s))
    h = 5
    d = primes(h)
    print('Primes ')
    for j in range(h-1):
        print(next(d))
