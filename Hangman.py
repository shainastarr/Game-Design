#Word Game
# Shaina Starr
#10/06/2021
# We are creating a list of words
# randomly select a word from the list for the user to guess
# give the user some turns
# show the word to the user with the characters guessed  
# play as long as the user has turns or has guessed the word

import random, os

os.system('cls')
#function to update dashes and letters
def updateWord(word, guesses, letcount):
    for letter in word:
        if letter in guesses:
            print(letter,end=" ")
            letCount+=1
        else:
            print('_', end=' ')
def Menu() :
    print("##############################################")
    print("Select the number which you would like to play")
    print("#                  MENU                      #")
    print("#                                            #")
    print("#      1. Animals                            #")
    print("#      2. Computer Parts                     #")
    print("#      3. Fruits                             #")
    print("#      4. Exit                               #")
    print("# To play the game select 1-3 to exit select 4")
    print("##############################################")

    while 1:
        sel=input("What would you like to do? ")
        try:
            sel = int(sel)
            break
        except ValueError:
            print("This is not an integer")
    
    return sel

def selWord(sel) :
    if sel ==1 : 
        word= random.choice(animals)
    elif sel==2:
        word=random.choice(compParts)
    else:
        word=random.choice(fruit)
    return word
letCount=0
animals=["tiger", "elephant"]
fruit=["banana", "strawberries"]
compParts=["keyboard", "Monitors", "computer","storage", "case","Operating System"]
name= input("What is your name? ")
score=0
counter=0
sel=Menu()
print(sel)
while sel <=3 :

    print(name, " Good Luck! you have 5 chances to guess")
    turns=5
    counter +=1
    word= selWord(sel)
    word = word.lower()
    wordCount=len(word)
    letCount=0
    print(word) # just for checking our code delete later
    guesses=''
    updateWord(word, guesses,letCount)
    while turns > 0 and letCount<=wordCount:
        print()
        newguess=input (name + " Give me a letter ")
        newguess= newguess.lower()
        if newguess in word:
            guesses += newguess
            letCount +=1
            print("you guessed one letter ")
        else:
            turns -=1
            print("Sorry, you have ", turns, "turns left")
        letCount=0
        updateWord(word, guesses,letCount)
    score= 3*len(word)+5*turns
    print(score)
    os.system('cls')
    sel=Menu()