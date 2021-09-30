class Student:
    def __init__(self, name):
        self.name = name

    def verify_registration(self):
        self.registered = True

    def get_guardian_name(self):
        self.guardian = "Someone"


class Student:
    def __init__(self, name):
        self.name = name
        self.registered = False
        self.guardian = None

class Student:
    def __init__(self, name, bus_rider=True):
        self.name = name
        self.bus_rider = bus_rider

class Student:
    def __init__(self, name, subjects=["maths", "physics"]):
        self.name = name
        self.subjects = subjects

student0 = Student("John")
student0.subjects.append("music")
student0.subjects
student1 = Student("Ashley")
student1.subjects