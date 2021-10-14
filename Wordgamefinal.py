#Word Game
#Shaina Starr
# 09/29/2021
# We are creating a list of words
# randomly select a word from the list for the user to guess
# give the user some turns
# show the word to the user with the characters guessed  
# play as long as the user has turns or has guessed the word

import random, os
os.system('cls')
score=0
choice=0
maxScore=0
#for loops are used to loop through an iterable object performing the same actions for each entry
def updateWord(word, guesses, letCount):
    for letter in word:
        if letter in guesses:
            print(letter,end=" ")
            letCount+=1
        else:
            print('_', end=' ')
    return letCount
def Menu():
    print("########################################")
    print("Welcome to Hangman! You will be given 3 categorizes\n and will be asked to guess the word.\nGood Luck!")
    print("#                MENU                  #")
    print("#                                      #")
    print("#       1. Animals                     #")
    print("#       2. Computer PArts              #")
    print("#       3. Fruits                      #")
    print("#       4. ScoreBoard                  #")
    print("#       5. Exit                        #")
    print("#    To play the game select 1-4       #")
    print("#       To exit select 5               #")
    print("########################################")
    print()
    #The try block tests a block of code for errors and the except block handles the error.
    while 1:
        sel=input("What would you like to do? ")
        try:
            sel = int(sel)
            break
        except ValueError:
            print("This is not an integer")

    sel=int(sel)
    return sel
def scoreBoard():
    #create our object file so we can open our text file
    myScore=open('score.txt', 'r')
    print(myScore.read())
    myScore.close()
    #myScore is a variable that I created where it is a memory location to store values.
    input("Are you ready to leave")
def ExitNow():
    print("I need to write in my file")
    print("Thank you for playing,", name)

def selWord(sel):
    if sel == 1:
        word= random.choice(animals)
    elif sel ==2:
        word= random.choice(compParts)
    elif sel ==3: 
        word= random.choice(fruits)
    
    return word
# create the function for the score board and comeback to main menu
# create the function to Exit, where you write to the file the max score and exit game
#These are the lists that I created which store multiple values in a single variable code
animals=["tiger", "elephant", "lion", "bear", "cat", "snake"]
fruits=["banana", "strawberries", "apple", "pear", "mango", "lemon"]
compParts=["keyboard", "Monitors","trackpad", "case","Operating System"]

name= input("What is your name? ")
maxScore=0 #to store highest Score
sel = Menu()
print(sel)
if sel ==4:
        scoreBoard()
        sel=Menu()
if sel ==5:
    ExitNow()
    os._exit
while sel<=3:
    print(name, " Good Luck! you have 5 chances to guess")
    
    word= selWord(sel)
    word = word.lower()
    wordCount=len(word)
    turns= wordCount+2  
    letCount=0  
    guesses=''
    score=0
    letCount=updateWord(word, guesses, letCount)
    #The IF statement evaluates whether an expression is true or false
    #The ELSE statement is used to conditionally control the statement
    while turns > 0 and letCount<wordCount:
        print()
        newguess=input (name + " Give me a letter ")
        newguess= newguess.lower()
        if newguess in word:
            guesses += newguess
            
            print("you guessed one letter ")
        else:
            turns -=1
            print("Sorry, you have ", turns, "turns left")
        letCount=0
        letCount= updateWord(word, guesses, letCount)
    os.system('cls')
    score=3*wordCount+5*turns
    if score > maxScore:
        maxScore=score
    print(maxScore)
    sel=Menu()
    anotherFile = open("score.txt", "a")
    anotherFile.write("\n" + name +"  highest score: \t" + str(maxScore))
    anotherFile.close()
#anotherFile is a variable I created to store my score after each round is played 
