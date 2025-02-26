class Employee:
    salary =234
    increment = 20
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100) )
    


e = Employee()
print(e.salaryAfterIncrement)