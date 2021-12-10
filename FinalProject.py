#MAria Suarez
#CReate Window for settings in your game

import pygame, os,random,time

from pygame import color
os.system('cls')
pygame.init()

## LISTS FOR MENU MESSAGES

screenMessage=[ "800x800", "800x600", "600x600"]
settingMessages=["Screen Size", "Background colors", "Object Colors","Sounds On/Off"]
mainMenu=["Instructions", 'Settings', "Level 1", "Level 2", "ScoreBoard", "Exit"]
colors = {'black':(0,0,0), 'red':(255,0,0), 'green':(0,255,0), 'blue':(0,0,145), 'white':(255,255,255), 'purple':(150,0,150), 'orange':(255, 165, 0)}
BGcolors=['Red', 'Blue', 'Yellow']
#GLOBAL VARIABLES
WHITE=colors.get('white')
BLACK=colors.get('black')
ORANGE=colors.get('orange')
COLOR=WHITE
MAINMENU=True
SETTINGS=False
INSTRUCTIONS=False
BACKGROUND=False
SCREEN=False
LEVEL1=False
LEVEL2=False
SCOREBOARD=False
OBJECTCOLOR=False
SOUNDS=False
flag=False
ScreenSize=['Larger, Smaller']

# Screen and square definition
WIDTH=800
HEIGHT=800
wbox=30
hbox=30
x=70
y=150
xs=50
ys=200
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Setting screendow")
square=pygame.Rect(x,y, wbox,hbox)
screenSize=pygame.Rect(xs,ys,wbox*4, hbox*4)
screen.fill(WHITE)
squaresSize=[pygame.Rect(xs,ys,wbox*4, hbox*4), pygame.Rect(xs,ys,wbox*4, hbox*3), pygame.Rect(xs,ys,wbox*3, hbox*3)]
#Declare FONTS
TITLE_FONT=pygame.font.SysFont('comicsans', 60)
MENU_FONT=pygame.font.SysFont('comicsans', 40)
INSTRUCTIONS_FONT=pygame.font.SysFont('comicsans', 30)
text= TITLE_FONT.render('message',1,BLACK)
#New window title
#images
colors={'red':(150,0,0), 'green':(0,200,0), 'blue': (0,0,255), 'purple': (150,0,150), 'white': (255,255,255), 'black': (0,0,0), 'navy': (0,80,128), 'hot pink': (255,105,180), 'orange': (255,165,0), 'yellow': (255,240,31)}
myColor = colors.get('purple')
ColorList = ['red', 'green', 'blue', 'white','purple', 'white', 'black', 'navy', 'hot pink', 'orange']
randColor = random.choice(ColorList)
Red=colors.get('red')
Blue=colors.get('blue')
Yellow=colors.get('yellow')
BG1=pygame.image.load('Images\\realimagelevel1.jpg')
BG2=pygame.image.load('Images\\realLEVEL2.png')
BG2=pygame.transform.scale(BG2, (800,800))
clock = pygame.time.Clock()
run=True
guyx=20
guyy=530
speed=25
wbox=64
hbox=64
Left= False
Right= False
WalkCount=0
char=pygame.image.load('Images\pigdownreal1-removebg-preview10.png')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.blit(char, (guyx, guyy))
MousePosition=(0,0)
print(MousePosition)

walkRight=[pygame.image.load('Images\pigright1-removebg-preview.png'),pygame.image.load('Images\pigright2-removebg-preview.png'), pygame.image.load('Images\pigright3-removebg-preview.png')]
walkLeft=[pygame.image.load('Images\pigleftreal1-removebg-preview.png'), pygame.image.load('Images\pigleftreal2-removebg-preview!.png'), pygame.image.load('Images\pigleftreal3-removebg-preview!.png')]
applex=650
appley=490
point=(applex, appley)
apple=pygame.image.load('Images\\apple-removebg-preview.png')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
COUNT = 12
jumpCount = COUNT
Jump = False
Left = False
Right = False



def redrawGameWindow():
    global WalkCount
    screen.blit(BG1,(0,0))
    if WalkCount + 1 >= 9:
        WalkCount = 0

    if Left:
        screen.blit(walkLeft[WalkCount//3], (guyx,guyy))
        WalkCount += 1
    elif Right:
        screen.blit(walkRight[WalkCount//3], (guyx,guyy))
        WalkCount += 1
    else:
        screen.blit(char, (guyx,guyy))
    screen.blit(apple, (applex, appley))

    pygame.display.flip()
    pygame.time.delay(100)
    # screen.fill((0,0,0))
    
    # pygame.display.update()

#Function to print Titles to all screens
def display_Title(message,ym):
    pygame.time.delay(100)
    text= TITLE_FONT.render(message,1,BLACK)
    xm=WIDTH/2-text.get_width()/2
    screen.blit(text, (xm,ym))
    pygame.display.update()
    pygame.time.delay(100)

#Function to print all the menus 
def Menu_function(line):
    pygame.time.delay(100)
    ym=y
    square.y=y
    xm=x+wbox+10
    for i in range(0,len(line)):
        word=line[i]
        pygame.draw.rect(screen, 'hot pink', square)
        text=MENU_FONT.render(word,1,BLACK)
        screen.blit(text,(xm,ym))
        pygame.display.flip()
        pygame.time.delay(100)
        ym +=100
        square.y=ym
def Level1():
    screen.blit(BG1, (0,0))
    display_Title("Back", HEIGHT-100)

def Level2():
    screen.blit(BG2, (0,0))
    display_Title("Back", HEIGHT-100)

def MainMenuWin(xm,ym):
    global MAINMENU
    global INSTRUCTIONS
    global SETTINGS
    global LEVEL1
    global LEVEL2
    global SCOREBOARD
    if xm>=70 and xm<=95 and ym>=150 and ym<=175:
        screen.fill(WHITE)
        pygame.display.set_caption("Instructions")
        display_Title("Instructions", 70)
        display_Title("Back", HEIGHT-100)
        pygame.display.update()
        MAINMENU = False
        INSTRUCTIONS = True               
    if xm>=70 and xm<=95 and ym>=250 and ym<=275: #71, 193. 93,193. 93, 212. 71, 211
        screen.fill(COLOR)
        pygame.display.set_caption("Settings")
        display_Title("SETTINGS",  70)
        Menu_function(settingMessages)
        display_Title("BACK", HEIGHT-100)
        pygame.display.update()
        MAINMENU = False
        SETTINGS = True  
    if xm>=70 and  xm<=95 and ym>=350 and ym<=375: #71, 193. 93,193. 93, 212. 71, 211
        screen.fill(COLOR)
        pygame.display.set_caption("Level 1")
        display_Title("Level 1",  70)
        # display_Title("Back", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        LEVEL1 = True
    if xm>=70 and  xm<=95 and ym>=450 and ym<=475: #71, 193. 93,193. 93, 212. 71, 211
        screen.fill(COLOR)
        pygame.display.set_caption("Level 2")
        display_Title("Level 2",  70)
        display_Title("Back", HEIGHT-100)
        pygame.display.update()
        MAINMENU = False
        LEVEL2 = True
    if xm>=70 and  xm<=95 and ym>=550 and ym<=575: #71, 193. 93,193. 93, 212. 71, 211
        screen.fill(COLOR)
        pygame.display.set_caption("ScoreBoard")
        display_Title("Scoreboard",  70)
        display_Title("Back", HEIGHT-100)
        pygame.display.update()
        MAINMENU = False
        LEVEL2 = True
    if xm>=70 and  xm<=95 and ym>=650 and ym<=675: #71, 193. 93,193. 93, 212. 71, 211
        screen.fill(COLOR)
        display_Title("Exit",  70)
        display_Title("Back", HEIGHT-100)
        pygame.display.update()
        MAINMENU = False
        global run
        run=False
def SettingMenuWin(xm,ym):
    global SETTINGS
    global SCREEN
    global BACKGROUND
    global OBJECTCOLOR
   
    if xm>=70 and xm<=95 and ym>=150 and ym<=175:
        screen.fill(COLOR)
        display_Title("Screen Size", 70)
        display_Title("Back", 750)
        pygame.display.update()
        SETTINGS = False
        SCREEN = True  
                   
    if xm>=70 and xm<=95 and ym>=250 and ym<=275 and flag: #71, 193. 93,193. 93, 212. 71, 211
        screen.fill(COLOR)
        display_Title("BACKGROUND COLORS",  70)
        display_Title("BACK", HEIGHT-100)
        pygame.display.update()
        BACKGROUND = True
        SETTINGS = False             
    if xm>=70 and  xm<=95 and ym>=350 and ym<=375: #71, 193. 93,193. 93, 212. 71, 211
        screen.fill(COLOR)
        display_Title("OBJECT COLORS",  70)
        display_Title("Back", HEIGHT-100)
        pygame.display.update()
        SETTINGS = False
        OBJECTCOLOR = True
    if xm>=70 and  xm<=95 and ym>=450 and ym<=475: #71, 193. 93,193. 93, 212. 71, 211
        screen.fill(COLOR)
        display_Title("SOUNDS",  70)
        display_Title("Back", HEIGHT-100)
        pygame.display.update()
        SETTINGS = False
        OBJECTCOLOR = True
def Menu_Back():
    global xm
    global ym
    xm=0
    ym=0
    screen.fill(COLOR)
    display_Title("MAIN", 70)
    Menu_function(mainMenu)

    pygame.display.update()
def Setting_Back():
    screen.fill(COLOR)
    display_Title("SETTINGS", 70)
    Menu_function(settingMessages)
    display_Title("Back", HEIGHT-100)
    pygame.display.update()
def Screen_size():
    pygame.time.delay(100)
    ym=ys
    screenSize.x=xs
    xm=xs
    for i in range(0,len(squaresSize)):
        squary=squaresSize[i]
        squary.x=xm
        pygame.draw.rect(screen, ORANGE, squary)
        word= screenMessage[i]
        text=MENU_FONT.render(word,1,BLACK)
        screen.blit(text,(xm-10,ym-40))
        pygame.display.flip()
        pygame.time.delay(100)
        xm +=200
# def game_Level1():
#     win.blit(BG1, (0,0))
#     pygame.display.set_caption("My game 1")
#     pygame.display.flip()
#     #add your game logic here

# def Color_screen():
#     for key in colors:
#Start Program
screen.fill(WHITE)
display_Title("MENU", 30)
Menu_function(mainMenu)
run=True 
# C:\Users\suarezm\OneDrive - Greenhill School\Game Design\GameDesign2021_Fall_Ablock\cade.py  
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run=False
    mouse_pos=(0,0)
    if eve.type==pygame.MOUSEBUTTONDOWN:
        mouse_pressed=pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_pos=pygame.mouse.get_pos()
            # print(pygame.mouse.get_pos())
            xm=mouse_pos[0]
            ym=mouse_pos[1]
            if MAINMENU:
                MainMenuWin(xm,ym)
            if INSTRUCTIONS:
                myFile=open('instructions.txt', 'r')
                yi=150
                for line in myFile.readlines():
                    print(line)
                    text=INSTRUCTIONS_FONT.render(line, 1, BLACK)
                    screen.blit(text, (40,yi))
                    pygame.display.update()
                    pygame.time.delay(10)
                    yi+=50
                myFile.close()

                if xm >335 and xm<460 and ym>745 and ym<795:
                    Menu_Back()
                    MAINMENU = True
                    INSTRUCTIONS = False
            if SETTINGS:
                SettingMenuWin(xm,ym)
                flag=True
                if xm >335 and xm<460 and ym>HEIGHT-50 and ym<HEIGHT:
                    Menu_Back()
                    MAINMENU = True
                    SETTINGS = False
                    flag=False
            if SCREEN:
                Screen_size()
                display_Title("Back", HEIGHT-100)
                pygame.display.update()
                x=70
                y=190
                square.x=x
                square.y=y
                for i in range(0, len(ScreenSize)):
                    word= ScreenSize[i]
                    pygame.draw.rect(screen, 'hot pink', square)
                    text=MENU_FONT.render(word,10, BLACK)
                    screen.blit(text, (x+wbox+10, y))
                    pygame.display.flip()
                    pygame.time.delay(100)
                    y += 100
                    square.y=y
                    counter=1
                counter+=1
                
                
                # if xm>450 and xm <540 and ym>200 and ym<290: 
                #     WIDTH=600
                #     HEIGHT=600
                #     screen=pygame.display.set_mode((WIDTH,HEIGHT))
                #     screen.fill(COLOR)
                
                    
                if xm >335 and xm<460 and ym>HEIGHT-50 and ym<HEIGHT:
                    WIDTH=800
                    HEIGHT=600
                    screen=pygame.display.set_mode((WIDTH,HEIGHT))
                    screen.fill(COLOR)
                    Screen_size()
                    display_Title("Back", HEIGHT-100)
                    Setting_Back()
                    SETTINGS = True
                    SCREEN = False

                if xm >335 and xm<460 and ym>745 and ym<795:
                    WIDTH=800
                    HEIGHT=800
                    screen=pygame.display.set_mode((WIDTH,HEIGHT))
                    screen.fill(COLOR)
                    display_Title("Back", HEIGHT-100)
                    Setting_Back()
                    SETTINGS = True
                    SCREEN = False
            if BACKGROUND:
                Menu_function(BGcolors)
                if xm>=70 and xm<=95 and ym>=150 and ym<=175:
                    COLOR=Red
                if xm>=70 and xm<=95 and ym>=250 and ym<=275:
                    COLOR=Blue
                if xm>=70 and  xm<=95 and ym>=350 and ym<=375:
                    COLOR=Yellow
                screen.fill(COLOR)
                if xm >335 and xm<460 and ym>HEIGHT-50 and ym<HEIGHT:
                    Setting_Back()
                    SETTINGS = True
                    BACKGROUND = False
            if OBJECTCOLOR:
                if xm >335 and xm<460 and ym>745 and ym<795:
                    Setting_Back()
                    SETTINGS = True
                    OBJECTCOLOR = False
            if LEVEL1:
                Level1()
                #play game here
                check=True
                while check:
                    clock.tick(30)
                    for eve in pygame.event.get():
                        if eve.type ==pygame.QUIT:

                            check=False
                    pygame.display.set_caption("My Game")
                    

                    if eve.type==pygame.MOUSEBUTTONDOWN:
                        mouse_pressed=pygame.mouse.get_pressed()
                        if mouse_pressed[0]:
                            mouse_pos=pygame.mouse.get_pos()
                            print(pygame.mouse.get_pos())
                            xm=mouse_pos[0]
                            ym=mouse_pos[1]
                #the pig is able to move around
                    keyPressed= pygame.key.get_pressed()
                    if keyPressed[pygame.K_LEFT] and guyx > speed:
                        guyx -= speed
                        Left = True
                        Right = False
                        
                    elif keyPressed[pygame.K_RIGHT] and guyx < WIDTH- speed:
                        if guyx >270 and guyx <=445 and guyy>=458:
                            Left=False
                            print(guyx,guyy)
                            Right= True
                        else:
                            guyx += speed
                            Right = True
                            Left = False                        
                    else:
                        Right= False
                        Left = False
                        WalkCount= 0

                        
                    # screen.blit(char,(guyx, guyy))
                    # pygame.display.flip()

                    if not Jump:
                        if keyPressed[pygame.K_SPACE]:
                            Jump = True
                            Right = False
                            Left = False
                            WalkCount = 0
                            # print(guyx,guyy)
                    else:
                        if jumpCount>=-COUNT:
                            guyy-= jumpCount*abs(jumpCount)/2
                            jumpCount -=1
                            print(guyx, guyy)
                        if guyy>=400 and guyx<= 270 and guyx>= 170:
                            Jump=COUNT
                            Jump=False
                        if guyy>=309 and guyx<=390 and guyx>=270:
                            Jump=COUNT
                            Jump=False
                        if guyy>=330 and guyx<=520 and guyx>=646:
                            Jump=COUNT
                            Jump=False
                                

                    redrawGameWindow()
                    pygame.display.flip()
                    if xm >300 and xm<500 and ym>700 and ym<795:
                        xm=0
                        ym=0
                        check=False
                        MAINMENU = True
                        LEVEL1 = False
                        Menu_Back()
                        
                        
                    pygame.display.flip()
            if LEVEL2:
                Level2()
                check=True
                while check:
                    clock.tick(30)
                    for eve in pygame.event.get():
                        if eve.type ==pygame.QUIT:

                            check=False
                    screen.blit(BG2, (0,0))
                    screen.blit(char, (guyx, guyy))
                    pygame.display.flip()
                    pygame.display.set_caption("My Game")
                    

                    if eve.type==pygame.MOUSEBUTTONDOWN:
                        mouse_pressed=pygame.mouse.get_pressed()
                        if mouse_pressed[0]:
                            mouse_pos=pygame.mouse.get_pos()
                            # print(pygame.mouse.get_pos())
                            xm=mouse_pos[0]
                            ym=mouse_pos[1]
                #the pig is able to move around
                    keyPressed= pygame.key.get_pressed()
                    if keyPressed[pygame.K_LEFT] and guyx > speed:
                        guyx -= speed
                        Left = True
                        Right = False
                        
                    elif keyPressed[pygame.K_RIGHT] and guyx < WIDTH- speed:
                        if guyx >270 and guyx <=445 and guyy>=458:
                            Left=False
                            # print(guyx,guyy)
                            Right= True
                        else:
                            guyx += speed
                            Right = True
                            Left = False                        
                    else:
                        Right= False
                        Left = False
                        WalkCount= 0

                        
                    # screen.blit(char,(guyx, guyy))
                    # pygame.display.flip()

                    if not Jump:
                        if keyPressed[pygame.K_SPACE]:
                            Jump = True
                            Right = False
                            Left = False
                            WalkCount = 0
                            # print(guyx,guyy)
                    else:
                        if jumpCount>=-COUNT:
                            guyy-= jumpCount*abs(jumpCount)/2
                            jumpCount -=1
                            # print(guyx, guyy)


    # print(pygame.mouse.get_pos())