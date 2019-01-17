import re
print("one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit.")
p= input("Input a password")
x = True
while x:  
    if (len(p)<8 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        continue

if x:
    print("Not a Valid Password")