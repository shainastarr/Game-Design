#Shaina Starr
# guess = random (20)
#ask user guess the number
#10 chances
#useranswer==guess


import os, random
os.system('cls')


randy=random.randint(1,20)
print(randy)
for i in range(10):
    guess=input("give me an integer from 1-20")
    try:

        guess= int(guess)
        check=True

    except ValueError:
        check=False

    if (check):
        if (guess==randy):
            print("You guessed the number")
            print("you won in ", i+1)
            break
        else:

         print("You losed")
         print("Thank you for playing")
 