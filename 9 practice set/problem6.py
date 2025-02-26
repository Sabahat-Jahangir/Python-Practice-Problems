with open("log.txt") as f:
    content = f.read()
    c = "python"

    if(c in content):
        print(f"{c} is present in content :)")
    else: 
        print(f"{c} is not present in content :) ")
