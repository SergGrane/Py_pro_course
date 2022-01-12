class People:
    """
    All the people
    """
    def __init__(self, name: str, surname: str, date_of_the_birth: str):
        self.name = name
        self.surname = surname
        self.date_of_the_birth = date_of_the_birth



    def __str__(self):
        return f'Name:  {self.name} Surname: {self.surname} date_of_the_birth: {self.date_of_the_birth} '
