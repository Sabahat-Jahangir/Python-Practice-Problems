try:
    a = int(input("Enter 1st Number:) "))
    b = int(input("Enter 2nd Number:) "))
    print(a/b)
except ZeroDivisionError as v:
    print("Division by xero ")