l = ["over", "bandar", "shit", "donkey"]

with open("my_file.txt", "r") as f:
    content = f.read()

for word in l:
    content = content.replace(word, "#" * len(word))

with open("my_file.txt", "w") as f:
    f.write(content)