import abc


class Aprime(abc.ABC):
    """
    Abstr class of prime number
    """

    def __init__(self, number: int):
        if not isinstance(number, int):
            raise TypeError('Number must be integer')
        if not number > 0:
            raise ValueError
        self.number = number

    @abc.abstractmethod
    def number_check(self):
        """
        have to check number to be prime
        :return: true or false
        """
        pass


class Numb1(Aprime):

    def __init__(self, number):
        super().__init__(number)
        self.number = number + 1

    def number_check(self):
        if self.number == 1:
            return True
        for i in range(2, self.number // 2):
            if not self.number % i:
                return False
        return True

    def __str__(self):
        if self.number_check():
            return f'Number +1 {self.number} is simple'
        return f'Number +1  {self.number} is not simple'


class Nnn:

    def __init__(self, number: int):

        if not isinstance(number, int):
            raise TypeError('Number must be integer')
        if not number > 0:
            raise ValueError
        self.number = number+2

    def number_check(self):
        for i in range(2, self.number//2):
            if not self.number % i:
                return False
        return True

    def __str__(self):
        if self.number_check():
            return f'Number +2 {self.number} is simple'
        return f'Number +2  {self.number} is not simple'


if __name__ == "__main__":
    Aprime.register(Nnn)
    n1 = Numb1(6)
    print(n1)
    n2 = Nnn(5)
    print(n2)
    print(isinstance(n2, Aprime))
