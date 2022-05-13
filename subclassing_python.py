class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def register_course(self, course):
        pass

    def load_account(self, amount):
        # fetch the amount from the server
        current_balance = 100
        current_balance += amount
        # save the new balance to the server

    def check_in(self, arriving_time):
        record_time = arriving_time
        required_time = "08:00"
        on_time = record_time <= required_time
        # save the data to the database

class Teacher:
    def __init__(self, name, staff_id, course_covered):
        self.name = name
        self.staff_id = staff_id
        self.course_covered = course_covered

    def request_vacation(self, start_date, duration):
        pass

    def load_account(self, amount):
        # fetch the amount from the server
        current_balance = 100
        current_balance += amount
        # save the new balance to the server

    def check_in(self, arriving_time):
        record_time = arriving_time
        required_time = "07:30"
        on_time = record_time <= required_time
        # save the data to the database

class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    def load_account(self, amount):
        # fetch the amount from the server
        current_balance = 100
        current_balance += amount
        # save the new balance to the server

    def check_in(self, arriving_time):
        record_time = arriving_time

class Student(Person):
    pass

class Teacher(Person):
    pass

student = Student("David", 20020)
student.load_account(100)

teacher = Teacher("Ashley", 1000033)
teacher.load_account(100)


class Student(Person):
    def __init__(self, name, student_id, grade):
        super().__init__(name, student_id)
        self.grade = grade

    def check_in(self, arriving_time):
        super().check_in(arriving_time)
        required_time = "08:00"
        on_time = arriving_time <= required_time
        # save the data to the database
        
student = Student("David", 20020, 3)
print(student.__dict__)

student.test()

Student.mro()


class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    def _login(self):
        pass

    def __logout(self):
        pass


person = Person("David", 20020)

class Student(Person):
    def test_login_logout(self):
        self._login()
        self.__logout()

    
student = Student("David", 20020)
student.test_login_logout()