import math

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n * self.n} :)")
    def cube(self):
        print(f"The cube is {self.n * self.n * self.n} :)")
    def squareroot(self):
        print(f"The square is {math.sqrt(self.n)} :)")

    @staticmethod
    def greet():
        print("Assalamoalaikum :) ")

a = Calculator(36)
a.square()
a.cube()
a.squareroot()
a.greet()