class Person:
   def __init__(self, name, age):
     self.name = name
     self.age = age

   def myfunc(self):
     print("Hello my name is " + self.name + "and I am " + self.age)

p1 = Person('norman', 67)

print(p1.myfunc())




