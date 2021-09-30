class Employee:
    company = "Apple111"
    def __init__(self, name):
        self.name = name



employee0 = Employee("John")
employee0.company is Employee.company
employee0.company = "Tesla"

employee0.company = "Apple111"

employee0.company is Employee.company

dir(employee0)