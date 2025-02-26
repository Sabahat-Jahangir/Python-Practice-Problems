class Employee:
    company = "Mictosoft"
    name = "ABC"
    salary = "120000000"
    def show(self):
        print(f"The name of the employee is {self.name} and salary is {self.salary}")

class Coder:
    language = "Python "

    def printLanguage(self):
        print(f"Out of al languagues here is your language {self.language}")

class Programmer(Employee, Coder):
    company = "Google"

    def showLanguage(self):
        print(f"The name of the language is {self.language}")

    

a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()