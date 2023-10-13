import random

print("""
888                                                           
888                                                           
888                                                           
88888b.   8888b.  88888b.   .d88b.  88888b.d88b.   8888b.  88888b.  
888 "88b     "88 b888 "88b d88P"88b 888 "888 "88b     "88b 888 "88b 
888  888 .d88888 8888  888 888  888 888  888  888 .d888888 888  888 
888  888 888  88 8888  888 Y88b 888 888  888  888 888  888 888  888 
888  888 "Y88888 8888  888  "Y88888 888  888  888 "Y888888 888  888 
                              888                              
                         Y8b d88P                              
                          "Y88P"   """)


deadLVL0 = """
      _______
     |/      
     |     
     |     
     |       
     |     
     |
  ___|___
"""

deadLVL1 = """
      _______
     |/      |
     |      (_)
     |     
     |       
     |     
     |
  ___|___
"""

deadLVL2 = """
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |     
     |
  ___|___
"""

deadLVL3 = """
      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |     
     |
  ___|___
"""

deadLVL4 = """
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |     
     |
  ___|___
"""

deadLVL5 = """
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |     _/ 
     |
  ___|___
"""

deadLVL6 = """
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |     _/ \_
     |
  ___|___
"""

#Reach LVL 6 for Game Over
deadLVL = int(0)

def showDeath(deadLVL):
    if deadLVL == 0:
        print(deadLVL0)
    elif deadLVL == 1:
        print(deadLVL1)
    elif deadLVL == 2:
        print(deadLVL2)
    elif deadLVL == 3:
        print(deadLVL3)
    elif deadLVL == 4:
        print(deadLVL4)
    elif deadLVL == 5:
        print(deadLVL5)
    elif deadLVL == 6:
        print(deadLVL6)

#Word list
wordList = [
'abruptly', 
'absurd', 
'abyss', 
'affix', 
'askew', 
'avenue', 
'awkward', 
'axiom', 
'azure', 
'bagpipes', 
'bandwagon', 
'banjo', 
'bayou', 
'beekeeper', 
'bikini', 
'blitz', 
'blizzard', 
'boggle', 
'bookworm', 
'boxcar', 
'boxful', 
'buckaroo', 
'buffalo', 
'buffoon', 
'buxom', 
'buzzard', 
'buzzing', 
'buzzwords', 
'caliph', 
'cobweb', 
'cockiness', 
'croquet', 
'crypt', 
'curacao', 
'cycle', 
'daiquiri', 
'dirndl', 
'disavow', 
'dizzying', 
'duplex', 
'dwarves', 
'embezzle', 
'equip', 
'espionage', 
'euouae', 
'exodus', 
'faking', 
'fishhook', 
'fixable', 
'fjord', 
'flapjack', 
'flopping', 
'fluffiness', 
'flyby', 
'foxglove', 
'frazzled', 
'frizzled', 
'fuchsia', 
'funny', 
'gabby', 
'galaxy', 
'galvanize', 
'gazebo', 
'giaour', 
'gizmo', 
'glowworm', 
'glyph', 
'gnarly', 
'gnostic', 
'gossip', 
'grogginess', 
'haiku', 
'haphazard', 
'hyphen', 
'iatrogenic', 
'icebox', 
'injury', 
'ivory', 
'ivy', 
'jackpot', 
'jaundice', 
'jawbreaker', 
'jaywalk', 
'jazziest', 
'jazzy', 
'jelly', 
'jigsaw', 
'jinx', 
'jiujitsu', 
'jockey', 
'jogging', 
'joking', 
'jovial', 
'joyful', 
'juicy', 
'jukebox', 
'jumbo', 
'kayak', 
'kazoo', 
'keyhole', 
'khaki', 
'kilobyte', 
'kiosk', 
'kitsch', 
'kiwifruit', 
'klutz', 
'knapsack', 
'larynx', 
'lengths', 
'lucky', 
'luxury', 
'lymph', 
'marquis', 
'matrix', 
'megahertz', 
'microwave', 
'mnemonic', 
'mystify', 
'naphtha', 
'nightclub', 
'nowadays', 
'numbskull', 
'nymph', 
'onyx', 
'ovary', 
'oxidize', 
'oxygen', 
'pajama', 
'peekaboo', 
'phlegm', 
'pixel', 
'pizazz', 
'pneumonia', 
'polka', 
'pshaw', 
'psyche', 
'puppy', 
'puzzling', 
'quartz', 
'queue', 
'quips', 
'quixotic', 
'quiz', 
'quizzes', 
'quorum', 
'razzmatazz', 
'rhubarb', 
'rhythm', 
'rickshaw', 
'schnapps', 
'scratch', 
'shiv', 
'snazzy', 
'sphinx', 
'spritz', 
'squawk', 
'staff', 
'strength', 
'strengths', 
'stretch', 
'stronghold', 
'stymied', 
'subway', 
'swivel', 
'syndrome', 
'thriftless', 
'thumbscrew', 
'topaz', 
'transcript', 
'transgress', 
'transplant', 
'triphthong', 
'twelfth', 
'twelfths', 
'unknown', 
'unworthy', 
'unzip', 
'uptown', 
'vaporize', 
'vixen', 
'vodka', 
'voodoo', 
'vortex', 
'voyeurism', 
'walkway', 
'waltz', 
'wave', 
'wavy', 
'waxy', 
'wellspring', 
'wheezy', 
'whiskey', 
'whizzing', 
'whomever', 
'wimpy', 
'witchcraft', 
'wizard', 
'woozy', 
'wristwatch', 
'wyvern', 
'xylophone', 
'yachtsman', 
'yippee', 
'yoked', 
'youthful', 
'yummy', 
'zephyr', 
'zigzag', 
'zigzagging', 
'zilch', 
'zipper', 
'zodiac', 
'zombie', 
]

#Select random Word from Word List
chosenWord = random.choice(wordList)

#Create Blanks
blankWord = ["_"] * len(chosenWord)

while "_" in blankWord and deadLVL < 6:
    
    #User Guess letter
    guessLetter = str("")
    #Allow User to insert only one letter
    while len(guessLetter) == 0 or len(guessLetter) > 1:
        print()
        blankWordStr = "".join(blankWord)
        print(f"Word: {blankWordStr}")
        guessLetter = input("Guess a letter: ").lower()

    if guessLetter in chosenWord:
        for x in range(len(chosenWord)):
            if guessLetter == chosenWord[x]:
                blankWord[x] = guessLetter

        showDeath(deadLVL)
        print("RIGHT !!!")
        print()
    else:
        deadLVL += 1
        showDeath(deadLVL)
        print("WRONG YOU LOSE A LIFE !!!")
        print(f"DeathLVL: {deadLVL} / 6")

if "_" not in blankWord:
    print()
    print("_________________")
    print("_____YOU WON_____")
    print("_________________")
    print()
    print()
elif deadLVL == 6:
    print()
    print("___________________")
    print("_____GAME OVER_____")
    print("___________________")
    print(f"The chosen Word was: >>> {chosenWord} <<<")
    print()
    



