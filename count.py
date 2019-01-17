print('####Counting by 2####')

while True:
    myName = input('your name?').capitalize()
    if len(myName) <= 10:
        break
    else:
        print("Too long! Try again")


if myName.isdigit():
    print ("Not a name and you smell bad! GoodBye")
    restart_program()
else:
    print ("Hello " + myName)

while True:
    endNum = input('Enter a number: ')
    if len(endNum) <= 3:
        break
    else:
        print("Too long! Try again")

if endNum.isdigit():
    print(endNum + " is your number")
    endNum=int(endNum)
else:
    print("Bad Number and you smell really bad! Goodbye")
    quit()

input('counting to '+ str(endNum)+' -press Enter to start:')

if endNum % 2 == 0:
    startNum=0
else:
    startNum=1

for x in range(startNum,endNum+1,2):
    print(x)

print('Done!')


