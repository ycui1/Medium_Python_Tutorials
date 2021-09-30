class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def verify_registration_status(self):
        status = self.get_status()
        self.status_verified = status == "registered"

    def get_guardian_name(self):
        self.guardian = "Goodman"

    def get_status(self):
        # get the registration status from a database
        status = query_database(self.first_name, self.last_name)
        return status

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def name(self):
        print("Getter for the name")
        return f"{self.first_name} {self.last_name}"

    @name.setter
    def name(self, name):
        print("Setter for the name")
        self.first_name, self.last_name = name.split()


student = Student("John", "Smith")
print("Student Name:", student.name)
student.name = "Johnny Smith"
print("After setting:", student.name)

class Student:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def name(self):
        return f"{self._first_name} {self._last_name}"

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"Student({self.first_name!r}, {self.last_name!r})"

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}"

student = Student("David", "Johnson")
student
print(student)

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def begin_study(self):
        print(f"{self.first_name} {self.last_name} begins studying.")

    @classmethod
    def from_dict(cls, name_info):
        first_name = name_info['first_name']
        last_name = name_info['last_name']
        return cls(first_name, last_name)

    @staticmethod
    def show_duties():
        return "Study, Play, Sleep"


class StudentRegular:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class StudentSlot:
    __slots__ = ['first_name', 'last_name']

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


student_r = StudentRegular('John', 'Smith')
student_r.__dict__
student_s = StudentSlot('John', 'Smith')
student_s.__dict__

class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def check_account_balance(self):
        account_number = get_account_number(self.student_id)
        balance = get_balance(account_number)
        return balance

    def load_money(self, amount):
        account = get_account(self.student_id)
        balance = get_balance(account)
        balance += amount
        update_balance(account, balance)


class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.account = Account(self.student_id)

    def check_account_balance(self):
        return self.account.get_balance()

    def load_money(self, amount):
        self.account.load_money(amount)


class Account:
    def __init__(self, student_id):
        self.student_id = student_id
        # get additional information from the database
        self.balance = 400

    def get_balance(self):
        # Theoretically, student.account.balance will work, but just in case
        # we need to have additional steps to check, such as query the database
        # again to make sure the data is up to date
        return self.balance

    def load_money(self, amount):
        # get the balance from the database
        self.balance += amount
        self.save_to_database()


# how many billable hours
a = 6
# the hourly rate
b = 100
# total charge
c = a * b

# The above vs. the below with no comments

billable_hours = 6
hourly_rate = 100
total_charge = billable_hours * hourly_rate

class Student:
    def get_mean_gpa(self):
        grades = self._get_grades()
        gpa_list = Student._converted_gpa_from_grades(grades)
        return sum(gpa_list) / len(gpa_list)

    def _get_grades(self):
        # fetch grades from a database
        grades = [99, 100, 94, 88]
        return grades

    @staticmethod
    def _converted_gpa_from_grades(grades):
        # convert the grades to GPA
        gpa_list = [4.0, 4.0, 3.7, 3.4]
        return gpa_list