from people_2pro import People

class Student(People):
    """
    Students of University
    """
    def __init__(self, name: str, surname: str, date_of_the_birth: str, speciality: str):
        super().__init__(name, surname, date_of_the_birth)
        self.speciality = speciality


    def __str__(self):
        return 'Student: \n' + super().__str__() + f'Speciality: {self.speciality} '




