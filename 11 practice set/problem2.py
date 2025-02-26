class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        return "Boww Bowww"

d = Dog()
print(d.bark())