# Write a program for selling tickets to IT-events.
# Each ticket has a unique number and a price.
# There are four types of tickets:
# regular ticket,
# advance ticket (purchased 60 or more days before the event),
# late ticket (purchased fewer than 10 days before the event)
# and student ticket.
# -advance ticket - discount 40% of the regular ticket price;
# -student ticket - discount 50% of the regular ticket price;
# -late ticket - additional 10% to the regular ticket price.
# All tickets must have the following properties:
# -the ability to construct a ticket by number;
# -the ability to ask for a ticket’s price;
# -the ability to print a ticket as a String.

class TicketIt:

    """
     describes the tickets to IT-events
    """

    def __init__(self, ticket_number: int):
        self.ticket_number = ticket_number

    def __str__(self):
        return 'Ticket No: ' + str(self.ticket_number) + ' Nominal price: ' + "%.2f" % PRICE


class RegularTicket(TicketIt):

    def __init__(self, ticket_number: int):
        super().__init__(ticket_number)

    def __str__(self):
        return 'Regular ticket: ' + super().__str__()


class AdvanceTicket(TicketIt):
    DISCOUNT = 40

    def __init__(self, ticket_number: int):
        super().__init__(ticket_number)

    def __str__(self):
        return 'Advance ticket: ' + super().__str__() + ' Discount price : ' + "%.2f" % (PRICE * self.DISCOUNT / 100)


class StudentTicket(TicketIt):
    DISCOUNT = 50

    def __init__(self, ticket_number: int):
        super().__init__(ticket_number)

    def __str__(self):
        return 'Student ticket: ' + super().__str__() + ' Discount price : ' + "%.2f" % (PRICE * self.DISCOUNT / 100)


class LateTicket(TicketIt):
    ADD = 10

    def __init__(self, ticket_number: int):
        super().__init__(ticket_number)

    def __str__(self):
        return 'Late ticket: ' + super().__str__() + ' New price : ' + "%.2f" % (PRICE * ((100 + self.ADD) / 100))


if __name__ == '__main__':
    PRICE = 200
    try:
        t1 = TicketIt(1212121)
        print(t1)
        r1 = RegularTicket(34536)
        print(r1)
        a1 = AdvanceTicket(111)
        print(a1)
        s1 = StudentTicket(111)
        print(s1)
        l1 = LateTicket(234)
        print(l1)

    except Exception as error:
        print(error)

