class Student:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


student = Student("John", "M")


from collections import namedtuple

Student = namedtuple("Student", ["name", "gender"])
student = Student("John", "M")


from enum import Enum

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    FALL = 3
    WINTER = 4

spring = Season.SPRING
spring.name
spring.value

fetched_season_value = 2
matched_season = Season(fetched_season_value)
matched_season

list(Season)

[x.name for x in Season]


from dataclasses import dataclass

@dataclass
class Student:
    name: str
    gender: str

student = Student("John", "M")
student.name
student.gender
repr(student)
print(student)