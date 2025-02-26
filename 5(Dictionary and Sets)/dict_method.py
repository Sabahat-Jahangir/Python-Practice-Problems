d = {} #Empty dictionary
marks = {
    "Harry": 100,
    "Sabahat": 100,
    "Sadia": 100
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry": 99, "Sania": 98})
print(marks["Harry"])
print(marks.get("Harry"))
print(marks.get("Harry2"))
# print(marks["Harry2"])
print(marks.pop("Harry"))
print(marks)
print(len(marks))
print(marks.clear())
