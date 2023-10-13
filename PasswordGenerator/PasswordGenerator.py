#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

totalLength = nr_letters + nr_symbols + nr_numbers
allLetters = [letters, numbers, symbols]
password = ""

for n in range(0, totalLength, 1):
    
    whichList = random.randint(0,2)
    if whichList == 0:
        if nr_letters != 0:
            whichLetter = random.randint(0,51)
            password += letters[whichLetter]
            nr_letters -= 1
            
    elif whichList == 1:
        if nr_numbers != 0:
            whichNumber = random.randint(0,9)
            password += numbers[whichNumber]
            nr_numbers -= 1
    elif whichList == 2:
        if nr_symbols != 0:
            whichSymbol = random.randint(0, 8)
            password += symbols[whichSymbol]
            nr_symbols -= 1
    
print(f"Your Password is: {password}")