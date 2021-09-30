class Person:
  def speak(self):
    print('Just a Person')
    
class Student(Person):
  def speak(self):
    print('Just a Student')
    

student = Student()
student.__class__

student.speak
Student.speak

Person.speak
person = Person()
person.speak

id(person.speak)
id(Person.speak)

student.__class__ = Person
student.speak

id(student.speak)