from random import randint
class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(slf, fro, to):
        print(f"Ticket is booked in train no: {slf.trainNo}, from {fro} to {to} :) ")

    def getStatus(slf):
        print(f"Tain no: {slf.trainNo} is okay to go :) ")

    def getFare(slf, fro, to):
        print(f"Ticket fare in train no: {slf.trainNo}, from {fro} to {to} is {randint(500,5000)} :) ")

p1 = Train(127654)
p1.book("DGKHAN", "Faisalabad")
p1.getStatus()
p1.getFare("DGKHAN", "Faisalabad")