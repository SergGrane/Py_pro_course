
# Создайте декоратор, который будет подсчитывать, сколько раз была вызвана декорируемая функция.
a = [0]


def text():
    """
    Text function
    :return: "hello world"
    """
    return "hello world"


def wrap(func):
    """
    wrap function
    :param func:
    :return: number of func calls
    """
    def wrapped():
        a[0] += 1
        return a[0]
    return wrapped


if __name__ == '__main__':
    print(wrap(text)())
    print(wrap(text)())
    print(wrap(text)())
    print(text())
