#Shaina Starr
#10/24/21
#Learning diplay
#opening windows
#alerting size window
#basic game loop

import pygame, random
from pygame.draw import circle
#first thing to do is to intialize pygame
pygame.init()
check= True 
height=600
width=700
x = 200
y = 300
rad = 30
hbox, wbox =20,20
boldX= width-300
boldY= height-200
bolder= pygame.Rect(boldX, boldY, 100, 200)
rect = pygame.Rect(x, y, hbox, wbox)
colors={'red':(150,0,0), 'green':(0,200,0), 'blue': (0,0,255), 'purple': (150,0,150), 'white': (255,255,255), 'black': (0,0,0), 'navy': (0,80,128), 'hot pink': (255,105,180), 'orange': (255,165,0)}
screen=pygame.display.set_mode((width, height))
myColor=colors.get('purple')
ColorList= ['red', 'green', 'blue', 'white','purple', 'white', 'back', 'navy', 'hot pink', 'orange']
randColor=random.choice(ColorList)
PURPLE=(150,0,150)
while check:
    #height=input("height of the window: (100-1000)")
    #width=input("Width of your window: (100-1000)")
   
    try:
        height=int(height)
        width=int(width)
        check= False
    except ValueError:
        check= False
color= randColor
window=pygame.display.set_mode((width,height)) #set up color 
# window.fill(color)
pygame.display.flip() #refresh window with new color 
#change title of the window 
pygame.display.set_caption("Shaina's Game")
pygame.display.flip()
hbox=50
wbox=50
speed=5
xc=random.randint(25,500)
yc=random.randint(25,400)
radius=hbox/2
#ball=pygame.circle(x=width/2, y=width/2)
rect=pygame.Rect(width/2, height/2, wbox, hbox )
#pygame.draw.circle(window ,color.get('green'),rect)
pygame.draw.circle(window, colors.get('blue'), (xc,yc), radius)
jumpCount= 7
COUNT = 7
jump=False


pygame.display.flip()
run=True

#main loop for the game:
while run:
    pygame.time.delay(100)
    for case in pygame.event.get():
        if case.type == pygame.QUIT:
            run= False
    #how to get the position of the mouse
   # x,y=pygame.mouse.get_pos()
    #print("("+str(x)+","+str(y)+")")
    keyPressed= pygame.key.get_pressed()
    
   
    if keyPressed[pygame.K_LEFT]:
        rect.x -= speed
        if rect.x<1:
            rect.x=width-wbox/2

    if rect.colliderect(bolder):
        rect.x +=5
    else:
        rect.x-= speed


    if keyPressed[pygame.K_RIGHT]:
        if rect.colliderect(bolder):
            rect.x-=5
        else:
            rect.x += speed

    rect.x += speed
    if rect.x>width:
        rect.x=width-wbox/2

    if not jump:
        if keyPressed[pygame.K_UP]:
            rect.y -= speed
            if rect.y<0:
                rect.y=height
                
        if keyPressed[pygame.K_DOWN]:
            rect.y += speed
            if rect.y>height:
                rect.y=0
        if keyPressed[pygame.K_SPACE]:
            jump=True
        print(jump)
    else: 
        if jumpCount>=-10:
            rect.y-=jumpCount*abs(jumpCount)
            rect.y-= jumpCount**2/2
            jumpCount-=1
        else:
            jumpCount=COUNT
            Jump=False
    
    if keyPressed[pygame.K_w]:
        yc -= speed
        if yc<0:
            yc=wbox
    if keyPressed[pygame.K_s]:
        yc += speed
        if yc> height:
            yc=height-wbox
    if keyPressed[pygame.K_a]:
        xc -= speed
        if xc<1:
            xc=wbox/2
    if keyPressed[pygame.K_d]:
        xc += speed
        print("xc= ", xc)
        if xc>(width-wbox):
            xc=width

    window.fill(color)
    pygame.display.flip()
    pygame.draw.rect(window, 'green', rect)
    pygame.draw.circle(window, colors.get('green'), (xc,yc), radius)
    pygame.display.flip()

    point =(xc, yc)   
    collide=pygame.Rect.collidepoint(rect,point)
    #collide function
    if collide:
        radius += wbox/2
        rect.x=random.randrange(25,width)
        rect.y=random.randrange(25,height)
   
    pygame.draw.rect(window, colors.get('purple'), rect)
    pygame.draw.circle(window, colors.get('blue'), (point), radius)
    pygame.draw.rect(screen,PURPLE,bolder)
    pygame.display.update()
    pygame.time.delay(30)
    pygame.display.flip() 
    if radius >= height/3:
        run=False
        
pygame.quit()