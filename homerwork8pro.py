from operator import itemgetter


class Goods:
    """
    Goods from internet-shop
    """

    def __init__(self, partnumber, name, price, weight, height, width, description):

        if not isinstance(price, ( int, float)):
            raise TypeError('Price is not a number ')

        if price < 0:
            raise ValueError('Price is negative ')

        self.partnumber = partnumber
        self.name = name
        self.price = price
        self.weight = weight
        self.height = height
        self.width = width
        self.description = description

    def __str__(self):
        return f'Name:  {self.name} Price: {self.price}  Decriptiont: {self.description} '


class Customer:
    """
    Customer of internet-shop
    """
    def __init__(self, name, surname, phone_number, mail, pssw, login):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.mail = mail
        self.pssw = pssw
        self.login = login

    def __str__(self):
        return f'Name:  {self.name}  {self.surname}  Phone number: {self.phone_number} E-mail: {self.mail}'

    def __repr__(self):
        return str(self.__dict__)


class Order:
    """
    Order of internet-shop
    """
    num_of_goods = 0

    def __init__(self, ord_number, order_date, customer: Customer):
        self.ord_number = ord_number
        self.order_date = order_date
        self.customer = customer
        self.products = []

    def __str__(self):
        res = '\n'.join(map(str, self.products))
        return f'{self.ord_number} {self.customer}\n{res} \nTotal price :{self.total_price()} UAH '

    def add_product(self, pr: Goods):
        if not isinstance(pr, Goods):
            raise TypeError('Product is not exist ')
        self.products.append(pr)
        self.num_of_goods += 1
        return self

    def total_price(self):
        s = 0
        for j in self.products:
            s += j.price
        return s

    def __getitem__(self, itm):
        if isinstance(itm, slice):
            start = itm.start or 0
            stop = itm.stop or self.num_of_goods
            step = itm.step or 1
            if start < 0 or stop > self.num_of_goods:
                raise IndexError
            else:
                res = []
                for i in range(start, stop, step):
                    res.append(self.products[i])
                return '\n'.join(map(str, res))
        if isinstance(item, int):
            if item < self.num_of_goods:
                return self.products[item]
            raise IndexError
        raise TypeError

    def __len__(self):
        return self.num_of_goods

    def __iter__(self):
        return OrderIterator(self.products)


class OrderIterator:

    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.iter_obj):
            self.i += 1
            return self.iter_obj[self.i-1]
        raise StopIteration


if __name__ == '__main__':
    try:
        goods1 = Goods('1001', 'phone', 1111, '456', '120', '10', 'Nokia phone....')
        goods2 = Goods('1002', 'phone', 9123 , '340', '100', '8', 'Samsung phone....')
        goods3 = Goods('1003', 'phone', 3213 , '340', '80', '8', 'Xmmx phone....')
        goods4 = Goods('1004', 'phone', 3213, '340', '80', '8', 'Xmx phone....')
        customer1 = Customer('Basil', 'Pupking', '102', 'Basil@gmale.net', 'passw', 'login')
        order1 = Order('2341', '01.01.2022', customer1)
        order1.add_product(goods3)
        order1.add_product(goods2)
        order1.add_product(goods1)
        print(order1)
        for item in order1:
            print(item)
        print(order1[2:3])
    except Exception as err:
        print('Error: ', err)





