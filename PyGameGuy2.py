#Shaina Starr
#11/14/21
#Game Design F-Block


import os, random
import pygame as py, time, sys

py.init()


clock = py.time.Clock()
width=700
height=600
walkRight = [py.image.load('Images\Pygame-Tutorials-master\Game\R1.png'), py.image.load('Images\Pygame-Tutorials-master\Game\R2.png'), py.image.load('Images\Pygame-Tutorials-master\Game\R3.png'), py.image.load('Images\Pygame-Tutorials-master\Game\R4.png'), py.image.load('Images\Pygame-Tutorials-master\Game\R5.png'), py.image.load('Images\Pygame-Tutorials-master\Game\R6.png'), py.image.load('Images\Pygame-Tutorials-master\Game\R7.png'), py.image.load('Images\Pygame-Tutorials-master\Game\R8.png'), py.image.load('Images\Pygame-Tutorials-master\Game\R9.png')]
walkLeft = [py.image.load('Images\Pygame-Tutorials-master\Game\L1.png'), py.image.load('Images\Pygame-Tutorials-master\Game\L2.png'), py.image.load('Images\Pygame-Tutorials-master\Game\L3.png'), py.image.load('Images\Pygame-Tutorials-master\Game\L4.png'), py.image.load('Images\Pygame-Tutorials-master\Game\L5.png'), py.image.load('Images\Pygame-Tutorials-master\Game\L6.png'), py.image.load('Images\Pygame-Tutorials-master\Game\L7.png'), py.image.load('Images\Pygame-Tutorials-master\Game\L8.png'), py.image.load('Images\Pygame-Tutorials-master\Game\L9.png')]
char=py.image.load("Images\Pygame-Tutorials-master\Game\standing.png")
bg=py.image.load('Images\\bgSmaller (1).jpg')


colors={'red':(150,0,0), 'green':(0,200,0), 'blue': (0,0,255), 'purple': (150,0,150), 'white': (255,255,255), 'black': (0,0,0), 'navy': (0,80,128), 'hot pink': (255,105,180), 'orange': (255,165,0), 'yellow': (255,240,31)}
screen = py.display.set_mode((width, height))
myColor = colors.get('purple')
ColorList = ['red', 'green', 'blue', 'white','purple', 'white', 'black', 'navy', 'hot pink', 'orange']
randColor = random.choice(ColorList)
screen=py.display.set_mode((width,height))
screen.blit(bg,(0,0))
py.display.flip()
guyx=200
guyy=300
screen.blit(char, (guyx, guyy))
py.display.flip()
myColor=colors.get('purple')
py.display.flip()
green=colors.get('green')
red=colors.get('red')
blue=colors.get('blue')
yellow=colors.get('yellow')


x=width/2
y=height-200
wbox=50
hbox=50
boldX=width-300
boldY=height-200
Left = False
Right = False
walkCount = 0

screen.fill(blue)
py.display.set_caption("Shaina's Window")
boulder=py.Rect(boldX,boldY,100,200)
COUNT = 10
jumpCount = COUNT
Jump = False 


def redrawGameWindow():
    global walkCount
    screen.blit(bg,(0,0))
    if walkCount + 1 >= 27:
        walkCount = 0

    if Left:
        screen.blit(walkLeft[walkCount//3], (guyx,guyy))
        walkCount += 1
    elif Right:
        screen.blit(walkRight[walkCount//3], (guyx,guyy))
        walkCount += 1
    else:
        screen.blit(char, (guyx,guyy))

    py.draw.rect(screen,yellow,boulder)
    py.display.flip()
    
    

run=True    
while run:
    clock.tick(27)
    for ev in py.event.get():
        if ev.type == py.QUIT:
            run=False
        speed = 10
        keyBoardkey = py.key.get_pressed()
    if keyBoardkey [py.K_LEFT]:
        if guyx<= width-210 and guyx>= width-220 and guyy>= height-250:     
            print(guyy)
            print(guyx)
            guyx += 5
            Left = True
            Right = False
        else:
            guyx-= speed

    elif keyBoardkey [py.K_RIGHT] and guyx < 800-wbox:
        if guyx > 80:
            then: guyx < 392

      # and guyx < boulder.x-45:
            print(guyy)
            print(guyx)
            guyx += speed
            Right = True
            Left = False

    else: 
        Right = False
        Left = False
        WalkCount = 0

    if keyBoardkey[py.K_UP]:
        guyy-= speed

    if keyBoardkey[py.K_DOWN] and guyy > 0 and guyy < 392 and (guyx < width-300 or guyx > width-200):
        guyy+=speed

    if not Jump:
        if keyBoardkey[py.K_SPACE]:
            Jump = True
            Right = False
            Left = False
            WalkCount = 0
    else:
        if jumpCount>=-COUNT:
            guyy-= jumpCount*abs(jumpCount)/2
            jumpCount -=1

        else:
            jumpCount=COUNT
            Jump=False

            #Setting Boundaries
        
        # if rect.y > height - hbox : rect.y = height - hbox
        # if guyy > height - hbox : guyy = height - hbox


    redrawGameWindow()

py.quit()
