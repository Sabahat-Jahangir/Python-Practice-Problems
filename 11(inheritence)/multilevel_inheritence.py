class Employee:
    a = 2

class Programmer(Employee):
    b = 3

class Manager(Programmer):
    c = 1

o = Employee()
print(o.a)

o = Programmer()
print(o.a)
print(o.b)

o = Manager()
print(o.a)
print(o.b)
print(o.c)
