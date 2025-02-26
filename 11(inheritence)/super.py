class Employee:
    def __init__(self):
        print("Constructor of Employee :)")
    a = 2

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer :)")
    b = 3

class Manager(Programmer):
    def __init__(self):
        super().__init__() # if you want to access constructor of parent class
        print("Constructor of Manager :)")
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
