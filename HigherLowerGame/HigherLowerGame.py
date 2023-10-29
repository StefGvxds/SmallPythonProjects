from data import data
from art import logo
from art import vs
import random

#Print Logo
print(logo)

#User score
score = 0

while True:
    
    #Chose from data list 
    while True:
        compareA = random.randint(0, len(data) - 1)
        compareB = random.randint(0, len(data) - 1)
        # We can't chose the same comparison
        if compareA != compareB:
            break
    
    print(f"\nCompare A: {data[compareA]['name']}, a {data[compareA]['description']}, from {data[compareA]['country']}.")
    print(vs)
    print(f"\nCompare B: {data[compareB]['name']}, a {data[compareB]['description']}, from {data[compareB]['country']}.")

    #Save Followernumber
    followerA = int(data[compareA]['follower_count'])
    followerB = int(data[compareB]['follower_count'])
    print(f"A = {followerA}, B = {followerB}")

    #User imput to make a choice
    while True:
        try:
            select = input("\nWho has more followers? Type 'A' or 'B': ").lower()
            if select == "a" or select == "b":
                break
            else:
                print("Invalid input. Please choose 'a' or 'b'.")
        except ValueError:
            print("Invalid input. Please choose 'a' or 'b'.")

    #Choice A
    if select == "a":
        if followerA > followerB:
            score += 1
            print(f"\nYou're right! Current score: {score}")
        else:
            print(f"\nSorry that's wrong. Final score: {score}")
            #Finish the game
            break
    #Choice B
    else:
        if followerB > followerA:
            score += 1
            print(f"\nYou're right! Current score: {score}")
        else:
            print(f"\nSorry that's wrong. Final score: {score}")
            #Finish the game
            break

