
def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
l =["Sabahat", "at", "Shazia", "Sabgeer", "Wajahat"]
print(rem(l, "at"))
