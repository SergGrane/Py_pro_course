# Реализуйте функционал, который будет запрещать установку полей класса любыми значениями, кроме целых чисел.
# Т.е., если тому или иному полю попытаться присвоить, например, строку, то должно быть возбужденно исключение.

import time


class Rectangle:
    """
    class of rectangle
    """

    def __init__(self, a: int, b: int):
        """
        initiator of rectangle class
        :param a: side a
        :param b: side b
        """
        self.a = a
        self.b = b

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if not isinstance(value, int):
            raise TypeError('side a is not a integer ')
        if value <= 0:
            raise ValueError('side must be > 0')
        self.__a = value

    @a.deleter
    def a(self):
        pass

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if not isinstance(value, int):
            raise TypeError('side a is not a integer ')
        if value <= 0:
            raise ValueError('side must be > 0')
        self.__b = value

    @b.deleter
    def b(self):
        pass

    def __str__(self):
        return f'Rectangle: Sides {self.a} {self.b}'

    #  Реализуйте свойство класса, которое обладает следующим функционалом: при установки значения этого свойства
    #  в файл с заранее определенным названием должно сохранятся время (когда устанавливали значение свойства)
    #  и установленное значение.


class Address:
    """
    class of address
    """
    def __init__(self, city: str, street: str, house_num: int, flat: int):
        """
        constructor of address class
        :param city:
        :param street:
        :param house_num:
        :param flat:
        """
        if not isinstance(city, str) or not isinstance(street, str) or not isinstance(house_num, int):
            raise TypeError('Wrong type of parameter')

        self.city = city
        self.street = street
        self.house_num = house_num
        self.flat = flat

    def __str__(self):
        return f'Address: City {self.city} Street {self.street} House No {self.house_num} Flat {self.flat}'

    @property
    def flat(self):
        return self.__flat

    @flat.setter
    def flat(self, value):
        if not isinstance(value, int):
            raise TypeError('flat a is not a integer ')
        if value <= 0:
            raise ValueError('flat must be > 0')
        time_set = time.time()
        try:
            fil1 = open("flat.xt", 'w')
        except Exception as err:
            fil1.close()
            print(err)
        fil1.write(f'Time {time_set} Flat No {value}')
        fil1.close()
        self.__flat = value

    @flat.deleter
    def flat(self):
        pass


if __name__ == '__main__':
    try:
        addr1 = Address('Kiev', 'Bankova', 2, 1)
        q1 = Rectangle(2, 3)
        print(q1)
        print(addr1)
    except Exception as err:
        print('Error: ', err)






