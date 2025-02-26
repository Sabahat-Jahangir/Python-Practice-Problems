class employee:
    Language = "Python" # Here language and salary is class attributes
    salary = 100000

sabgeer = employee()
sabgeer.name = "Sabgeer"
print(sabgeer.name, sabgeer.salary, sabgeer.Language)

Shaz = employee()
Shaz.name = "Shaz" # Here name is object attribute
Shaz.Language = "C++" # instance attribute take preference over class attribute
print(Shaz.name, Shaz.salary, Shaz.Language)

# instance = object
