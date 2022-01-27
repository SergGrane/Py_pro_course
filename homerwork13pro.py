
# Создайте декоратор, который будет подсчитывать, сколько раз была вызвана декорируемая функция.


def wrap(func):
    b = 0
    """
    wrap function
    :param func:
    :return: number of func calls
    """
    def wrapped():
        nonlocal b
        b += 1
        return b

    return wrapped


@wrap
def text():
    """
    Text function
    :return: "hello world"
    """
    return "hello world"


if __name__ == '__main__':
    print(text())
    print(text())
    print(text())
    print(text())
