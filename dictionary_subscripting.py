grades = {"Anne": 98, "John": 95, "Bella": 97}

grades["Anne"]
grades["John"]

grades["Zoe"]

grades.get("Anne")
grades.get("Zoe", 0)
grades.get("Zoe")

name_to_check = ""
if name_to_check in grades:
    grade = grades[name_to_check]
else:
    grade = "A default value"


def calculate_something(arg0, arg1, **kwargs):
  kwarg0 = kwargs.get("kwarg0", 0)
  kwarg1 = kwargs.get("kwarg1", "normal")
  kwarg2 = kwargs.get("kwarg2", [])
  kwarg3 = kwargs.get("kwarg3", "text")
  
  
grades.setdefault("Anne")
grades.setdefault("Danny", 0)
grades.setdefault("Ashley")

grades

from collections import defaultdict

grades_default = defaultdict(int, grades)

grades_default

grades_default["Lily"]

students_by_initial0 = {}
for name in grades.keys():
  group = students_by_initial0.setdefault(name[0], [])
  group.append(name)
  
print(students_by_initial0)

students_by_initial1 = defaultdict(list)
for name in grades.keys():
  students_by_initial1[name[0]].append(name)
  
print(students_by_initial1)

students_by_initial2 = {}
for name in grades.keys():
  if name[0] in students_by_initial2:
    students_by_initial2[name[0]].append(name)
  else:
    students_by_initial2[name[0]] = [name]

students_by_initial2