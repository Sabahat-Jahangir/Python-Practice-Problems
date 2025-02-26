from random import randint
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo}, from {fro} to {to} :) ")

    def getStatus(self):
        print(f"Tain no: {self.trainNo} is okay to go :) ")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo}, from {fro} to {to} is {randint(500,5000)} :) ")

p1 = Train(127654)
p1.book("DGKHAN", "Faisalabad")
p1.getStatus()
p1.getFare("DGKHAN", "Faisalabad")