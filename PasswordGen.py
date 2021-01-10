import os
import random
import sys
import pyperclip

class Password:

    length = 0
    strength = 0
    value = ''

    def __init__(self, length,strength):
        self.length = length
        self.strength = strength
        
        
    

    
    def generate_password(self):
        x=0
        value = ''
        while x < int(self.length) :
            x = x + 1
            #value = str(value) + str(randint(0, 10))
            ucLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            myNumbers = '123456789'
            lcLetters = 'abcdefghijklmnopqrstuvwxyz'
            pCharacters = '£$%&-+={}[]'
            value = value + random.choices(ucLetters, k=1)[0] 
            if(x<int(self.length)):
                if(self.strength > 1) :
                    value = value + random.choices(lcLetters, k=1)[0] 
                    x = x + 1
            if(x<int(self.length)):
                if(self.strength > 1) :
                    value = value + random.choices(myNumbers, k=1)[0] 
                    x = x + 1
            if(x<int(self.length)):
                if(self.strength == 3):
                    value = value + random.choices(pCharacters, k=1)[0] 
                    x = x + 1
            self.value = value
        return(value)

    def password_to_clibpoard(self):
        print(self.value)
        pyperclip.copy(self.value)
        pyperclip.paste()

if(len(sys.argv)>1):
    l = int(sys.argv[1])
    s = int(sys.argv[2])
else:
    l = input("How many characters should the password have?")
    s = int(input("How strong should the password be? 1 = medium 2 = Strong = 3 = Ultra"))    

newpass = Password(l,s)
print(newpass.generate_password())
newpass.password_to_clibpoard()



#print(value)  
