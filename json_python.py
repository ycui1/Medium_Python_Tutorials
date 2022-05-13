{
  "firstName": "John",
  "lastName": "Smith",
  "age": 35,
  "city": "San Francisco"
}

import json

json.dumps((1, 2, 3))

employee_json_data = """{
  "employee0": {
    "firstName": "John",
    "lastName": "Smith",
    "age": 35,
    "city": "San Francisco"
  },
  "employee1": {
    "firstName": "Zoe",
    "lastName": "Thompson",
    "age": 32,
    "city": "Los Angeles"
  }
}"""

import json

employee_data = json.loads(employee_json_data)
print(employee_data)

employee_json_array = """[
{"employee2": "data"},
{"employee3": "data"}
]"""
employee_list = json.loads(employee_json_array)
print(employee_list)
# [{'employee2': 'data'}, {'employee3': 'data'}]

json_to_write='{"name": "John", "age": 35}'
with open("json_test.txt", "w") as file:
    file.write(json_to_write)

employee_data = [{"name": "John", "age": 35, "city": "San Francisco"}, {"name": "Zoe", "age": 34, "city": "Los Angeles"}]

print(json.dumps(employee_data, indent=2))

employee_info = {"name": "John", "age": 35, "city": "San Francisco", "home": "123 Main St.", "zip_code": 12345, "sex": "Male"}
print(json.dumps(employee_info, indent=2, sort_keys=True))

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

employee = Employee("John Smith", 40)
json.dumps(employee)

json.dumps(employee, default=lambda x: x.__dict__)

def outer(a):
  b = 5
  def inner():
    return a + b
  return inner

close = outer(100)
close()

def monitor(func):
    def monitored():
        print(f"*** {func.__name__} is called")
        func()

    return monitored

@monitor
def example0():
    pass

example0()
# output: *** example0 is called

@monitor
def example1(param0):
    pass

example1("a string")
