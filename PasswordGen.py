import os
import random
import sys
import pyperclip

if(len(sys.argv)>1):
    y = int(sys.argv[1])
    strength = int(sys.argv[2])
else:
    y = int(input("How many characters should the password have?"))
    strength = int(input("How strong should the password be? 1 = medium 2 = Strong = 3 = Ultra"))

value = ""
x = 0

while x < y :
    x = x + 1
    #value = str(value) + str(randint(0, 10))
    ucLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    myNumbers = '123456789'
    lcLetters = 'abcdefghijklmnopqrstuvwxyz'
    pCharacters = '£$%&-+={}[]'
    value = value + random.choices(ucLetters, k=1)[0] 
    if(x<y):
        if(strength > 1) :
            value = value + random.choices(lcLetters, k=1)[0] 
            x = x + 1
    if(x<y):
        if(strength > 1) :
            value = value + random.choices(myNumbers, k=1)[0] 
            x = x + 1
    if(x<y):
        if(strength == 3):
            value = value + random.choices(pCharacters, k=1)[0] 
            x = x + 1

pyperclip.copy(value)
pyperclip.paste()
print(value)  
