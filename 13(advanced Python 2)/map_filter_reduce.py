from functools import reduce
# Map Usage
l = [1, 2, 3, 4, 5, 6, 7, 8]

square = lambda x: x*x

sqList = map(square, l)
print(list(sqList))

# Filter Example
even = lambda x: x%2 == 0
onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce Usage
sum = lambda a,b:a+b
print(reduce(sum, l))