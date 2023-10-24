#Game information
#A Counts as 1 or 11
#J, Q or K count as 10
#Over 21 Player lose
#First Card becomes the Player Second the Dealer, third the player and 4th the dealer. The forth card is not shown
#When the Player has as many points as the dealer the result will be draw (No one wins)
#When the Dealer has  a Hand <17 he have to draw another card (A third one)

from ast import While
from pickle import TRUE
import random

print("""
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                  
""")

#Reset Gamescore
player = 0
dealer = 0

#If someone's score exceeds 21 points, 'didSomeOneWin' will be set to True.
didSomeOneWin = False

def calcScore(oldScore):
    #11 = A
    #12 = B
    #13 = Q
    #14 = K
    drawnCard = random.randint(1, 14)
    #Draw a A (or 11)
    if drawnCard == 11:
        while True:
            try:
                print(f"Current Score: {oldScore}")
                selectA = int(input("You draw A. Chose 1 or 11: "))
                if selectA == 1 or selectA == 11:
                    oldScore += int(selectA)
                    #IF 1 or 11 the Whileloop will break
                    break
                else:
                    print("Invalid input. Please choose 1 or 11.")
            except ValueError:
                print("Invalid input. Please choose 1 or 11.")
                
     #Draw a B, Q or K           
    elif drawnCard == 12 or drawnCard == 13 or drawnCard == 14:
        if drawnCard == 12:
            print("You draw B")
        elif drawnCard == 13:
            print("You draw Q")
        elif drawnCard == 14:
            print("You draw K")
        oldScore += 10
        
    #Draw a number
    else:
        print(f"You draw {drawnCard}")
        oldScore += drawnCard
    print(f"Current Score: {oldScore}")
    return oldScore

#Function to calculate the dealer's score
def calcDealerScore(oldScore):
    #11 = A
    #12 = B
    #13 = Q
    #14 = K
    drawnCard = random.randint(1, 14)
    
    #Draw a A (or 11)
    if drawnCard == 11:
        if oldScore < 11: 
            print("Dealer draw A and chose 11.")
            selectA = 11
        elif oldScore > 10:
           print("Dealer draw A and chose 1.")
           selectA = 1 
        oldScore += int(selectA)   
        
    #Draw a B, Q or K      
    elif drawnCard == 12 or drawnCard == 13 or drawnCard == 14:
        if drawnCard == 12:
            print("Dealer draw B")
        elif drawnCard == 13:
            print("Dealer draw Q")
        elif drawnCard == 14:
            print("Dealer draw K")
        oldScore += 10
    
    #Draw a number    
    else:
        print(f"Dealer draw {drawnCard}")
        oldScore += drawnCard
        print(f"Dealer's Score: {oldScore}'")
    return oldScore

#Player draws 2 cards
print("_____YOUR TURN_____")
player = int(calcScore(player))
print()
player = int(calcScore(player))
print()

#Dealer draws 1 card
print("_____DEALER'S TURN_____")
dealer = int(calcDealerScore(dealer))

#Player's turn again
print()
print("_____YOUR TURN_____")

#IF score is over 21 checkContinue = False to stop Dealer's turn because he wins
checkContinue = True
while True:
    try:
        print()
        drawAgain = input("Draw another card? 'y' or 'n': ").lower()
        print()
        if drawAgain == "y":
            player = int(calcScore(player))
            print()
            if player > 21:
                checkContinue = False
                print()
                print("__________RESULTS__________")
                print("YOU LOSE!")
                didSomeOneWin = True
                print(f"Your Score: {player}")
                #Draw a second card for the dealer
                dealer = int(calcDealerScore(dealer))
                print(f"Dealer's Score: {dealer}")
                break
        elif drawAgain == "n":
            break
        else:
            print("Invalid input. Please choose 'y' or 'n'.")
    except ValueError:
        print("Invalid input. Please choose 'y' or 'n'.")

#Dealer's turn
if checkContinue == True:
    print("_____DEALER'S TURN_____")
    dealer = int(calcDealerScore(dealer))
    while dealer < 17:
        dealer = int(calcDealerScore(dealer))
    if dealer > 21:
        print()
        print("__________RESULTS__________")
        print("YOU WINN!")
        didSomeOneWin = True
        print(f"Your Score: {player}")
        print(f"Dealer's Score: {dealer}")
    
    if didSomeOneWin == False:
        print()
        print("__________RESULTS__________")
        if dealer > player:
            print("YOU LOSE!")
            print(f"Your Score: {player}")
            print(f"Dealer's Score: {dealer}")
        elif dealer == player:
            print("DRAW!")
            print(f"Your Score: {player}")
            print(f"Dealer's Score: {dealer}")
        elif dealer < player:
            print("YOU WINN!")
            print(f"Your Score: {player}")
            print(f"Dealer's Score: {dealer}")    