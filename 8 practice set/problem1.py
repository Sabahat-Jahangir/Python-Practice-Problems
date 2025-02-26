def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
a = 34
b = 32
c = 36
print(f"The greatest value is:) {greatest(a, b, c)}")
