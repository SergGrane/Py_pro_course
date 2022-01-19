# Напишите функцию, которая применит к списку чисел произвольную пользовательскую функцию
# и вернет суммы элементов полученного списка

def sum_str(list1: list, func):

    if not isinstance(list1, list):
        raise TypeError('must be list')
    """
    sum list numbers
    :param list1: list of numbers
    :param func: exp3, arifm, geom
    :return: sum of new list
    """
    return sum((func(list1[i]) for i in range(len(list1))))


def exp3(j: int):
    """
    exponentiation with 3
    :param j: number
    :return: exponentiation
    """
    return j**3


def arifm(j: int):
    """
    sum number with self
    :param j: number
    :return: sum
    """
    return j+j


def geom(j: int):
    """
    multiplication of  number with self
    :param j: number
    :return: multiplication
    """
    return j*2


if __name__ == "__main__":
    try:
        a = sum_str([1, 2, 4], geom)
        print(a)
    except Exception as err:
        print(err)
