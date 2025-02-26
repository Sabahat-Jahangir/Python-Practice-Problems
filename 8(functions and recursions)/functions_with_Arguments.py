def greet(name, ending="Allah Hafiz"):
    print(f"Have a good day, {name} :)")
    print(ending)
    return "Jazak Allah"
name = input("Enter your name plz :) ")
a = greet(name, "Love you")
print(a)