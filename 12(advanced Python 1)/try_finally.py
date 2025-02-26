try:
    a = int(input("Enter a number :) "))


except Exception as e:
    print(e)

finally:
    print("If try run run successfully it will eneter in else")