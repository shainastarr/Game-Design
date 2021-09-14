#Shaina Starr
#09/08/2021
import os

os.system('cls')
#We are going to learn how to ask the user for data
#We are going to learn how to loop
star= int(input("please enter number of stars ")) #allow to get values from the user
#print ("* * * *")
#loop
#variable to count lines
spc=0
line = star 
for lncounter in range(line):
    for counter in range(lncounter):
        print(" ", end=" ")
    for space in range(star):
        print ("*", end=" ") 
    for space in range (spc):
        print (" ", end=" ")

    for counter in range (star):
        print ("*", end=" ")
    print()
    star=star-1
    spc+=2
#star = star-1 => star -=1

print("Thank you")

