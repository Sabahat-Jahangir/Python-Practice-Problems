def f_to_c(f):
    c = 5*(f-32)/9
    return c

f = int(input("Enter temperature in F :) "))
print(f"The temperature in cencius is :) {f_to_c(f)}")