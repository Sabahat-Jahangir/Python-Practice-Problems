class Employee:
    company = "Mictosoft"
    def show(self):
        print(f"The name of the employee is {self.name} and salary is {self.salary}")

# class Programmer:
#     company = "Google"
#     def show(self):
#         print(f"The name of the employee is {self.name} and salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name of the language is {self.language}")

class Programmer(Employee):
    company = "Google"

    def showLanguage(self):
        print(f"The name of the language is {self.language}")

    

a = Employee()
b = Programmer()

print(a.company, b.company)