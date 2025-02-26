with open("file.txt") as f:
    content = f.read()
    c = input("Enter the str you want to check :) ")

    if(c in content):
        print(f"{c} is present in content :)")
    else: 
        print(f"{c} is not present in content :) ")

