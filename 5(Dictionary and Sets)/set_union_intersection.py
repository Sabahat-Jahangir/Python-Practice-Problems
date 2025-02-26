s1 = {1,54,76,2,1}
s2 = {1,32,76,34,12,65,32}

a = s1.union(s2)
print(sorted(a))
b = s1.intersection(s2)
print(b)
c = s1.difference(s2)
print(c)