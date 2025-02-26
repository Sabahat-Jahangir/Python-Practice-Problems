marks = {
    "Harry": 100,
    "Sabahat": 100,
    "Sadia": 100
}

print(marks, type(marks))
print(marks["Sabahat"])

# Define the menu
menu = {
    "Pizza": 15,
    "Burger": 10,
    "Fries": 5,
    "Salad": 8,
    "Pasta": 12,
    "Soup": 7,
    "Steak": 25,
    "Sushi": 18,
    "Tacos": 9,
    "Wings": 14,
    "Shrimp": 16,
    "Salmon": 20,
    "Coffee": 4,
    "Tea": 3,
    "Coke": 2
}

print("Welcome to SABGEER RESTURENT :)")
for item in menu.items():
    print(f"{item[0]}: Rs.{item[1]}")