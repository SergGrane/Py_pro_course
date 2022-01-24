#  Создайте декоратор, который зарегистрирует декорируемую функцию в списке функций, для обработки последовательности.


my_function = []


def add_function(f):
    """
    Decorator is registrating function in list
    :param f: function
    :return: function
    """
    my_function.append(f)
    return f


@add_function
def suma(a: list):
    """
    sum of list members
    :param a: list
    :return: sum
    """
    return sum(a)


@add_function
def exp2(a: list):
    """
    squares all the members of list
    :param a: list
    :return: list of squares
    """
    for i in range(len(a)):
        a[i] = a[i] ** 2
    return a


print(my_function)
print(exp2([1, 2, 4, 5]))
print(suma([1, 2, 3, 4]))
