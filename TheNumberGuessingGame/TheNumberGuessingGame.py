import random

print("""
___________                        _________                      __  .__    .__                 
\__    ___/__.__.______   ____    /   _____/ ____   _____   _____/  |_|  |__ |__| ____    ____   
  |    | <   |  |\____ \_/ __ \   \_____  \ /  _ \ /     \_/ __ \   __\  |  \|  |/    \  / ___\  
  |    |  \___  ||  |_> >  ___/   /        (  <_> )  Y Y  \  ___/|  | |   Y  \  |   |  \/ /_/  > 
  |____|  / ____||   __/ \___  > /_______  /\____/|__|_|  /\___  >__| |___|  /__|___|  /\___  /  
          \/     |__|        \/          \/             \/     \/          \/        \//_____/  
""")

#This Variable changes when the user wants to play again or not
again = "y"

#Check if the user does not want to play again
while again == "y":
    print("\n\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100\n")

    #User choose easy or hard game
    while True:
        try:
            degree = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
            if degree == "easy" or degree == "hard":
                break
            else:
                print("Invalid input. Please choose 'easy' or 'hard'.")
        except ValueError:
            print("Invalid input. Please choose 'easy' or 'hard'.")

    #Easy game = 10 attempts or Hard game = 5 attempts
    if degree == "hard":
        attempt = 5
    else:
        attempt = 10

    print(f"You have {attempt} attempts remaining to guess the number.\n")

    #Set number to guess
    guessNumber = random.randint(1, 100)

    #Function that limited the user to make an int-input
    def userInput():
        while True:
            try:
               userGuess = int(input("Make a guess: "))
               if userGuess == int(userGuess) and 1 <= int(userGuess) <= 100:
                   break
               else:
                   print("Invalid input. Please choose a number between 1 and 100.")
            except ValueError:
                print("Invalid input. Please choose a number between 1 and 100.")
        return userGuess

    #User has to find the guessNumber
    for n in range(0, attempt):
        userGuess = userInput()
        if userGuess < guessNumber:
            if n + 1 == attempt:
                print("\n\nYOU LOSE! :(\n")
                break
            print("Too low.\nGuess again.\n")
        elif userGuess > guessNumber:
            if n + 1 == attempt:
                print("\n\nYOU LOSE! :(\n")
                break
            print("Too High.\nGuess again.\n")
        elif userGuess == guessNumber:
            print("\n\n!!!_____!!!You WINN!!!_____!!!")
            break

    #Ask if the user wants to play again 
    while True:
        try:
            again = input("\n\nIf you want to play again type 'y' or 'n': ").lower()
            if again == "y" or again == "n":
                break
            else:
                print("Invalid input. Please choose 'y' or 'n'.")
        except ValueError:
            print("Invalid input. Please choose 'y' or 'n'.")
    



        