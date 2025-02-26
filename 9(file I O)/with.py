f = open("my_file.txt")
data = f.read()
print(data)
f.close()

# This same can be written using with statement
with open("file.txt") as f:
    print(f.read())

# We donot have to explicitly close the file
