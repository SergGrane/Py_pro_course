#    Создайте декоратор класса с параметром. Параметром должна быть строка,
#    которая должна дописываться (слева) к результату работы метода __str__.



def dec(libr: str):
    """
    Decorator of Book class
    :param libr: string for adding in __str__ result
    :return: result of __str__
    """
    def dec1(cls):
        def dec2(*args):
            return f'{libr} {cls(*args)}'
        return dec2
    return dec1


@dec('Library book: ')
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


if __name__ == "__main__":
    b=Book('qwqwq','qwqwqw','2121')
    print(b)

