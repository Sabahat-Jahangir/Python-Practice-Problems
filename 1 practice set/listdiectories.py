import os

# Specify the directry you want to list
directory_path = '/Users'

# List all files and diectories in the specified path 
contents = os.listdir(directory_path)

# print the file and directories Name
for item in contents:
    print(item)