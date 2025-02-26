a = int(input("Enter 1st Number:) "))
b = int(input("Enter 2nd Number:) "))

if(b == 0):
    raise ZeroDivisionError("Divisor must not be zero")
else:
    print(f"The Division a/b is {a/b}")