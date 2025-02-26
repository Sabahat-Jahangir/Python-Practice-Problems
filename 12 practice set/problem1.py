try:
    with open("t1.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open("t2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)
try:
    with open("t3.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e)