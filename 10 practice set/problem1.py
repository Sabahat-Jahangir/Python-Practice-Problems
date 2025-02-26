class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode
p1 = programmer("Sabgeer", 1200000, 1243212)
print(p1.company, p1.name, p1.salary, p1.pincode)
p2 = programmer("Shaz", 2000000, 2345123)
print(p2.company, p2.name, p2.salary, p2.pincode)