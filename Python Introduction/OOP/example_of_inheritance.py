# class Person(object):
 
#     # Constructor
#     def __init__(self, name):
#         self.name = name
 
#     # To get name
#     def getName(self):
#         return self.name
 
#     # To check if this person is an employee
#     def isEmployee(self):
#         return False
    

# class Employee(Person):
 
#     # Here we return true
#     def isEmployee(self):
#         return True
    
    
    
# emp = Person("Geek1")  # An Object of Person
# print(emp.getName(), emp.isEmployee())
 
# emp = Employee("Geek2")  # An Object of Employee
# print(emp.getName(), emp.isEmployee())


# # parent class
# class Person(object):
 
#     # __init__ is known as the constructor
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber
 
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
 
# # child class
# class Employee(Person):
#     def __init__(self, name, idnumber, salary, post):
#         self.salary = salary
#         self.post = post
#         #Python program to demonstrate error if we forget to invoke __init__() of the parent
#         # invoking the __init__ of the parent class
#         Person.__init__(self, name, idnumber)
 
# # creation of an object variable or an instance
# a = Employee('Rahul', 886012, 200000, "Intern")
 
# # calling a function of the class Person using its instance
# a.display()


# The super() function is a built-in function that returns the objects that represent the parent class. 
# It allows to access the parent class’s methods and attributes in the child class.

# parent class
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def display(self):
     print(self.name, self.age)

# child class
class Student(Person):
  def __init__(self, name, age, id, course):
    self.id = id
    self.course = course
    # inheriting the properties of parent class
    super().__init__(name, age)
 
  def displayInfo(self):
    print(self.id, self.course)


obj = Student("Mayank", 23, 102, "IT")
obj.display()
obj.displayInfo()