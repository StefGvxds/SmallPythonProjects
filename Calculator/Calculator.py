
print(
    """
 _____________________
|  _________________  |                   888                888        888    
| | PythonCalc.  0. | |                   888                888        888  
| |_________________| |                   888                888        888  
|  ___ ___ ___   ___  |    .d8888b 8888b. 888 .d8888b888  888888 8888b. 888888 .d88b. 888d888 
| | 7 | 8 | 9 | | + | |    d88P"       "88b888d88P"   888  888888    "88b888   d88""88b888P"   
| |___|___|___| |___| |    888     .d888888888888     888  888888.d888888888   888  888888     
| | 4 | 5 | 6 | | - | |    Y88b.   888  888888Y88b.   Y88b 888888888  888Y88b. Y88..88P888     
| |___|___|___| |___| |     "Y8888P"Y888888888 "Y8888P "Y88888888"Y888888 "Y888 "Y88P" 888     
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|               
"""
    )


def addFunction(n1, n2):
    return n1 + n2

def subFunction(n1, n2):
    return n1 - n2

def mulFunction(n1, n2):
    return n1 * n2

def divFunction(n1, n2):
    return n1 / n2

cont = False
calcNonStop = True
final = 0

while calcNonStop == True:
    
    #Choose first number
    while True:
        try:
            if cont == False:
                n1 = float(input("What's the first number?: "))
            else:
                 n1 = final    
            break
        except ValueError:
            print("Please enter a valid number")
            
    #Chose operator
    op = input("Pick an operation '+' '-' '*' '/': ")
    while op != "+" and op != "-" and op != "*" and op != "/":
        op = input("Pick an operation '+' '-' '*' '/': ")
    
    #Choose second number
    while True:
        try:
            n2 = float(input("What's the second number?: "))
            break
        except ValueError:
            print("Please enter a valid number")


    #Calc
    if op == "+":
        final = addFunction(n1, n2)
        print(f"{n1} + {n2} = {final}")
    elif op == "-":
        final = subFunction(n1, n2)
        print(f"{n1} - {n2} = {final}")
    elif op == "*":
        final = mulFunction(n1, n2)
        print(f"{n1} * {n2} = {final}")
    elif op == "/":
        final = divFunction(n1, n2)
        print(f"{n1} / {n2} = {final}")
        
    #Calc with previous number or new one
    contOrNot = input(f"Type 'y' to continue calculating with {final}, or type 'n' to start a new calculation: ").lower() 
    while contOrNot != "y" and contOrNot != "n":
        contOrNot = input(f"Type 'y' to continue calculating with {final}, or type 'n' to start a new calculation: ").lower() 
    
    if contOrNot == "y":
        cont = True
        