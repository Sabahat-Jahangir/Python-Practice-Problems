friends = ["Apple", "Orange", 5, 345.06, False, "Alia", "Rehana"]
print(friends[1])

friends.append("Sabgeer")
print(friends)

l1 = [1, 9, 34, 12, 11, 87, 65, 55, 34, 24]
# l1.sort()
print(l1)

# l1.reverse()
print(l1)

l1.insert(4, 444444444) # insert 444444444 such that its index in the list is 3.
print(l1)

# Pop will delete the particular value and prints the result.
value = l1.pop(3)
print(value)
print(l1.pop(4))
print(l1)
l1.remove(24)
print(l1)

