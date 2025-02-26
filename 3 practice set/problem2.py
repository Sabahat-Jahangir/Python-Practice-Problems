letter = '''
     Dear <|Name|>,
     You are selected!
     <|Date|>'''
name = input("Enter your name:) ")
date = input("Enter the date:) ")
print(letter.replace("<|Name|>", name).replace("<|Date|>",date))