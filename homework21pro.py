# Создайте дескриптор, который будет делать поля класса управляемые им доступными только для чтения.

class MyDescriptor:
    """
    Descriptor class for volume in the Box class
    """
    def __init__(self, n):
        self.n = n

    def __get__(self, instance_self, instance_class):
        return self.n * instance_self.p

    def __set__(self, instance_self, value):
        pass


class Box:
    """
    Box volume class
    """
    def __init__(self, x: (int, float), y: (int, float), z: (int, float)):
        """
        Box costructor
        :param x: side
        :param y: side
        :param z: side
        """
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)) or not isinstance(z, (int, float)):
            raise TypeError('sides must be int or float')

        if x <= 0 or y <= 0 or z <= 0:
            raise ValueError('sides must be > 0')

        self.p = x * y * z
    volume = MyDescriptor(2)

    def __str__(self):
        return f'Box volume {self.p}'


if __name__ == '__main__':
    try:
        b1 = Box(1, 5, 3)
        print(b1)
        print(b1.volume)
        b1.volume = 29
        print(b1.volume)

    except Exception as err:
        print('Error: ', err)






