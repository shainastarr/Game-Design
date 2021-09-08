#Shaina Starr
#09/08/2021

#We are going to learn how to ask the user for data
#We are going to leanr how to loop
star= int(input("please enter number of stars ")) #allow to get values from the user
print ("* * * *")
#loop
#variable to count lines
line = star 
for incounter in range(line):
    for counter in range (star):
        print ("*", end=" ") 
    print ()
print ("Thank you")
for incounter in range(line):
    for counter in range (star):
        print ("*", end=" ") 
    print ()
    star -=1
print ("Thank you")
