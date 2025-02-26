with open("my_file.txt", "r") as f:
    content = f.read()

contentNew = content.replace("bandar", "######")

with open("my_file.txt", "w") as f:
    f.write(contentNew)