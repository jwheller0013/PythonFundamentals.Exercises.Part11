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

Jim = Instructor("Jim", "Heller", "1/13/1986", AliveStatus.Alive)
print (Jim.instructor_id)

Bob = Student("Bob", "Bobby", "1/12/23", AliveStatus.Alive)
print(Bob.student_id)