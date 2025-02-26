class employee:
    Language = "Python" # Here language and salary is class attributes
    salary = 100000

    def getInfo(self):
        print(f"The language is {self.Language}.{self.name}")

    @staticmethod # this means greet is the static function and it does not need object
    def greet():
        print("Subha Khair :)")

sabgeer = employee()
sabgeer.name = "Sabgeer"
print(sabgeer.name, sabgeer.salary, sabgeer.Language)
sabgeer.getInfo()
employee.getInfo(sabgeer)
sabgeer.greet()


