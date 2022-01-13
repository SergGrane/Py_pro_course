from student_2pro import Student


class Group:
    """
    Students of University
    """
    group_size = 0

    def __init__(self, group_number: str):
        self.student = []
        self.group_number = group_number

    def __str__(self):
        res = '\n'.join(map(str, self.student))
        return f'Group_number: {self.group_number} \n{res} {len(self.student)}'

    def add_student(self, value: Student):
        if not isinstance(value, Student):
            raise UserError("Student  is not valid")
        if value in self.student:
            raise UserError("Student " + value.name + ' ' + value.surname + " is already present")
        self.student.append(value)
        self.group_size += 1
        return self

    def del_student(self, value: Student):
        if isinstance(value, Student) and value in self.student:
            self.student.remove(value)
            self.group_size -= 1
        return

    def find_student(self, value: str):
        for item in self.student:
            if value == item.surname:
                return 'Search completed: \n' + str(item)

    def __iter__(self):
        return GroupIterator(self.student)

    def __getitem__(self, item):
        if isinstance(item, slice):
            start = item.start or 0
            stop = item.stop or self.group_size
            step = item.step or 1
            if start < 0 or stop > self.group_size:
                raise IndexError
            else:
                res = []

                for i in range(start, stop, step):
                    res.append(self.student[i])
                return '\n'.join(map(str, res))
        if item < self.group_size:
            return self.student[item]
        raise IndexError

    def __len__(self):
        return self.group_size


class GroupIterator:

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


class UserError(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message


if __name__ == '__main__':
    s1 = Student('aaaaa', 'ssss', '12/12/00', 'rrrrrrr')
    s2 = Student('aaaaa2', 'ssss2', '12/12/00', 'rrrrrrr')
    s3 = Student('aaaaa3', 'ssss3', '12/12/00', 'rrrrrrr')
    s4 = Student('aaaaa4', 'ssss4', '12/12/00', 'rrrrrrr')
    gr1=Group('123')
    gr1.add_student(s1)
    gr1.add_student(s2)
    gr1.add_student(s3)
    gr1.add_student(s4)
    print(gr1)
    for i in gr1:
        print(i)
    print('\n', gr1[1:3:])
