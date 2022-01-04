# Pizzeria offers pizza-of-the-day for business lunch. The type of pizza-of-the-day depends on the day of week.
# Having a pizza-of-the-day simplifies ordering for customers. They don't have to be experts on specific types of pizza.
# Also, customers can add extra ingredients to the pizza-of-the-day. Write a program that will
# form orders from customers.


class Inredients:

    """
    describes extra ingredients to the pizza
    """
    def __init__(self, name: str, price: float):
        self.name = name
        if not isinstance(price, (int, float)):
            raise TypeError('Price is not int or float')
        self.price = price

    def __str__(self):
        return 'Xtra ingredient: ' + self.name + ', Price: ' + str(self.price) + ' UAH'


class PizzaOfTheDay:

    """
     describes pizza-of-the-day for business lunch
    """

    def __init__(self, name: str, base_price: float):

        self.name = name
        self.base_price = base_price
        self.__adds = []

    def add_xtraingredient(self, xtra_ingr: Inredients):
        if not isinstance(xtra_ingr, Inredients):
            raise TypeError('Ingredient does not exist!')
        self.__adds.append(xtra_ingr)

    def total_price(self):
        s = self.base_price
        for item in self.__adds:
            s += item.price
        return s

    def __str__(self):
        res = '\n'.join(map(str, self.__adds))
        return f'{self.name}, Base price: {self.base_price} UAH\n{res} \nTotal price: {self.total_price()} UAH '


if __name__ == '__main__':
    try:
        ing1 = Inredients('Salami', 22.0)
        print(ing1)
        ing2 = Inredients('Mushrooms', 25.0)
        print(ing2)
        ing3 = Inredients('Olives', 18.0)
        print(ing3)
        sunday = PizzaOfTheDay('Salami pizza', 120.0)
        sunday.add_xtraingredient(ing2)
        sunday.add_xtraingredient(ing3)
        print(sunday)

    except Exception as error:
        print(error)

