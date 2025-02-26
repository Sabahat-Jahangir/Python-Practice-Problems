class employee:
    Language = "Python" # Here language and salary is class attributes
    salary = 100000

    def __init__(self, name, salary, language): # method that starts with __ are called donder functions, it is automatically called just init(constructor)
        self.name = name
        self.salary = salary
        self.Language = language
        print("I am creating an object ")

    def getInfo(self):
        print(f"The language is {self.Language}.{self.name}")

    @staticmethod # this means greet is the static function and it does not need object
    def greet():
        print("Subha Khair :)")

sabgeer = employee("Sabgeer", 1200000, "C++")
sabgeer.name = "Sabgeer"
print(sabgeer.name, sabgeer.salary, sabgeer.Language)
sabgeer.getInfo()
employee.getInfo(sabgeer)
sabgeer.greet()


