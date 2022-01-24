#  в классе определен метод __str__, который возвращает строку на основании класса. Создайте такой декоратор для
#  этого метода, чтобы полученная строка сохранялась в текстовый файл, имя которого совпадает с именем класса,
#  метод которого вы декорировали.

def file_outp(f):
    """
    Decorator of __str__
    :param f: __str__
    :return: string
    """
    def wrap1(args):
        try:
            fil1 = open(args.__class__.__name__ + ".txt", 'w')
        except Exception as err:
            fil1.close()
            print(err)
        fil1.write(f(args))
        fil1.close()
        return 'All res are in file'
    return wrap1


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

    @file_outp
    def __str__(self):
        return f'Author {self.author} Name {self.name} ISBN {self.isbn}'


if __name__ == "__main__":

    b = Book('sasas', 'wwwwww', '1212-212/23')
    print(b)

