from time import *
import random as r

print(time())


def mistake(partest, usertest):
    error = 0

    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error
    

test = ["A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.",
        "My name is Altaf Hussain" , "Welcome to our website"]


rest1 = r.choice(test)
print("     ***** typing speed *****")

print(test1)
print()
print()

testinput = input("Enter: ")
