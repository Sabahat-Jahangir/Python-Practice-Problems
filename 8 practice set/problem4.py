# sum(n) = n + sum(n-1) 

def sum(n):
    if(n==1):
        return 1
    return n + sum(n-1)

n = int(input("Enter a number :) "))
print(f"Sum is :) {sum(n)}")