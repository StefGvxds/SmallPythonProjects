
print("""                                                                 
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88                                                                      
""")

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def greet():
    #User input encode or decode
    action = ""
    while action != "encode" and action != "decode":
        action = (input("Type 'encode' to encrypt, type 'decode' to decrypt: ")).lower()
    print()

    #Message the user want's to encrypt or decrypt
    message = ""
    message = (input("Type your message: ")).lower()
    print()

    #Shift number 
    shift = 0
    while True:
        try:
            shift = int(input("Type the shift number: "))
            #break if a number is given
            break 
        except ValueError:
            print()
            print("Please enter a valid number!")
    print()
    
    return action, message, shift 

def dencrypt(action, message, shift):
    
    #Split message in List
    splitMessage = [char for char in message]
    
    #The result will be saved here
    dencMessage = ""
    
    #Loop for every char in message
    for n in range(len(splitMessage)):
        
        #Check if Char is in Alphabet
        if splitMessage[n] in alphabet:
            
            for x in range(len(alphabet)):
                    
                    #Check in wich place it is
                    if splitMessage[n] == alphabet[x]:
                        #Encode selected
                        if action == "encode":
                            #Shift algorythm
                            dencMessage += alphabet[(x + shift) % 26]
                        #Decode selected    
                        else: 
                            dencMessage += alphabet[(x - shift) % 26]
        else:
            #If there is no char give the symbol back
            dencMessage += splitMessage[n]
    #Encode selected        
    if action == "encode":
        print("Encoded message:")
        print (dencMessage)
        print()
    #Decode selected     
    else:
        print("Decoded message:")
        print (dencMessage)
        print()
    again = ""
    while again != "yes" and again != "no":
        again = input("Use Caesar Cipher again? Type 'yes' or 'no': ").lower()
        print()
    return again

again = True

while again == True:  
    #Get Input from greet function
    action, message, shift  = greet()
    newCaesar = dencrypt(action, message, shift)
    if newCaesar == "yes":
        again = True
    elif newCaesar == "no":
        again = False