#Shaina Starr
#Learning how to use while loops
#create randy and ask player if they want to play
#while('y' in answer)


#Place instructions of your game
import os, random
print("Welcome to this game. Keep going to begin")

name=input("What is your name")
print("Hi", name)
answer=input("Would you like to play my game")
while('y' in answer):
    randy=random.randrange(1,100)
    print(randy)
    counter=0
    guess=input("please enter an integer")
    while(guess !=randy):
        try:
            guess=int(guess)
            check=True
        except ValueError:
            check=False
        if guess == randy:
            print("You guess correct. It took you")
            print(counter+1, end=" tries\n")
            break
        else: 
            counter +=1
            if guess > randy:
                print("Your guess was high") 
            else: 
                print("Your guess was low")
        guess=input("give me a new number")
    answer=input("Would you like to play again")

print("Thank you for playing ", name)
        
    

        