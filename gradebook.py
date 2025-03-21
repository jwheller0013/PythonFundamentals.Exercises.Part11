import enum
import uuid

class AliveStatus (enum.Enum):
    Deceased = 0
    Alive = 1

class Person:
    def __init__(self, first_name, last_name, dob, AliveStatus):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = AliveStatus.Alive

    def update_first_name (self, name):
        self.first_name = name

    def update_last_name (self, name):
        self.last_name = name

    def update_dob (self, dob):
        self.dob = dob

    def update_status (self, status):
        self.alive = status

class Instructor(Person):

    def __init__(self, first_name, last_name, dob, AliveStatus, ):
        super().__init__(first_name, last_name, dob, AliveStatus)
        self.instructor_id = ("Instructor_" + str(uuid.uuid4()))

class Student(Person):

    def __init__(self, first_name, last_name, dob, AliveStatus):
        super().__init__(first_name, last_name, dob, AliveStatus)
        self.student_id = ("Student_" + str(uuid.uuid4()))

class ZipCodeStudent(Student):

    def __init__(self, first_name, last_name, dob, AliveStatus):
        super().__init__(first_name, last_name, dob, AliveStatus)

class prek(Student):

    def __init__(self, first_name, last_name, dob, AliveStatus):
        super().__init__(first_name, last_name, dob, AliveStatus)

class middle_school(Student):

    def __init__(self, first_name, last_name, dob, AliveStatus):
        super().__init__(first_name, last_name, dob, AliveStatus)

class college(Student):

    def __init__(self, first_name, last_name, dob, AliveStatus):
        super().__init__(first_name, last_name, dob, AliveStatus)

class Classroom:

    def __init__(self):
        self.students = {}
        self.instructors= {}

    def add_instructor (self, x):
        self.instructors[x.instructor_id] = (x.first_name, x.last_name, x.dob, x.alive)

    def add_student (self, y):
        self.students[y.student_id] = (y.first_name, y.last_name, y.dob, y.alive)

    def remove_instructor (self, z):
        del self.instructors[z]

    def remove_student (self, x):
        del self.students[x]

    def print_instructor (self):
        print(self.instructors)

    def print_students (self):
        print(self.students)


#testing parts

# jim = Instructor("Jim", "Heller", "1/13/1986", AliveStatus.Alive)
# angel = Instructor('Angel', 'Angel', "1/1/2004", AliveStatus.Alive)
# isiah = Student('Isiah', 'Something', '1/1/2020', AliveStatus.Alive)
# print (jim.instructor_id)
# test_class = Classroom()
#
# test_class.add_instructor(jim)
# test_class.add_instructor(angel)
# test_class.add_student(isiah)
#
# test_class.print_students()
# test_class.print_instructor()
#
#
# test_class.remove_instructor(jim.instructor_id)
# test_class.remove_student(isiah.student_id)
# test_class.print_instructor()
# test_class.print_students()