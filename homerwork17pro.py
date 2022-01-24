#   Создайте декоратор, который зарегистрирует декорируемый класс в списке классов.


my_class = []


def add_class(cls):
    """
    Decorator is registrating function in list
    :param cls: function
    :return: function
    """
    my_class.append(cls)
    return cls


@add_class
class Book:
    """
    class of book
    """

    def __init__(self, name: str, author: str, isbn: str):
        if not isinstance(name, str) or not isinstance(author, str) or not isinstance(isbn, str):
            raise TypeError
        self.name = name
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f'Author {self.author} Name {self.name} ISBN {self.isbn}'


@add_class
class Customer:
    """
    class of library customer
    """
    def __init__(self, name: str, surname: str):
        if not isinstance(name, str) or not isinstance(surname, str):
            raise TypeError
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'name {self.name} surname {self.surname}'


if __name__ == "__main__":
    print(my_class)

