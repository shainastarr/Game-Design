#Shaina Starr
#create Window for setting in your game

import pygame, os, random, time


os.system('cls')
pygame.init()

#LISTS FOR MENU MESSAGES
setingMessages=["Screen Size", "Background colors", "Object colors", "Sounds On/Off", "BACK"]
# GLOBAL VARIABLES
MAINMENU=True
InstWin=False
SETTINGS=False
colors={'red':(150,0,0), 'green':(0,200,0), 'blue': (0,0,255), 'purple': (150,0,150), 'white': (255,255,255), 'black': (0,0,0), 'navy': (0,80,128), 'hot pink': (255,105,180), 'orange': (255,165,0)}
WHITE=colors.get('white')
BLACK=colors.get('black')
ORANGE=colors.get('orange')
COLOR=WHITE
MainMenu=["intructions", "level 1", "level 2", "Settings", "Scoreboard", "Exit"]

WIDTH=800
HEIGHT=800
wbox=30
hbox=30
x=70
y=150
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Setting Window")
square=pygame.Rect(x,y, wbox, hbox)

#Declare the FONTS
TITLE_FONT=pygame.font.SysFont('comicsans', 80)
SubTitle=pygame.font.SysFont('comicsans', 40, italic=True)
MENU_FONT=pygame.font.SysFont('comicsans', 40)
text=TITLE_FONT.render('Settings', 1, BLACK)
def create_NewWindow(winTitle):
    pygame.display.set_caption(winTitle)
    win.fill(COLOR)
    pygame.display.update()


def display_Title(message):
    win.fill(COLOR)
    pygame.time.delay(100)
    text=TITLE_FONT.render(message, 1, BLACK)
    xm=WIDTH/2-text.get_width()/2
    ym=40
    win.blit(text, (xm,ym))
    pygame.display.update()
    pygame.time.delay(100)

def Menu_function(message):
    pygame.time.delay(100)
    ym=y
    xm=x+wbox+10
    for i in range(0,len(message)):
        word=message[i]
        pygame.draw.rect(win, ORANGE, square)
        text=MENU_FONT.render(word, 1, BLACK)
        win.blit(text,(xm,ym))
        pygame.display.flip()
        pygame.time.delay(100)
        ym +=100
        square.y=ym


display_Title("Main Menu")
Menu_function(MainMenu)

run=True                

while run:
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            run=False
        if eve.type ==pygame.MOUSEBUTTONDOWN:
            mouse_presses=pygame.mouse.get_pressed()
            if mouse_presses[0]:
                mouse_pos =pygame.mouse.get_pos()
                print(mouse_pos)
                xp=mouse_pos[0]
                yp=mouse_pos[1]
                print(x,y)
                #if py.Rect.collidepoint(square,(mouse_pos)):
                if xp>x and xp<x+wbox and yp>y and yp<245 and MAINMENU: #MainBool:
                    win.fill(COLOR)
                    display_Title("INSTRUCTIONS")
                    MAINMENU=False
                    InstWin=True
                if xp>x and xp<x+wbox and yp>250 and yp<275 and MAINMENU: #MainBool:
                    win.fill(COLOR)
                    display_Title("LEVEL 1")
                if xp>x and xp<x+wbox and yp>350 and yp<375 and MAINMENU: #MainBool:
                    win.fill(COLOR)
                    display_Title("LEVEL 2")
                if xp>x and xp<x+wbox and yp>450 and yp<475 and MAINMENU: #MainBool:
                    win.fill(COLOR)
                    y=150
                    display_Title("SETTINGS")
                    Menu_function(setingMessages)
                    MAINMENU=False
                    SETTINGS=True

                    

                    

                 





# Menu_function(setingMessages)
#                     display_Title("SETTINGS")
#                     create_NewWindow("Screen Size")
#                     display_Title("SCREEN SIZE", 40)
#                     create_NewWindow("BACKGROUND COLORS")
#                     display_Title("background colors", 40)
#                     create_NewWindow("OBJECT COLORS")
#                     display_Title("object colors", 40)
#                     create_NewWindow("SOUND ON/OFF")
#                     display_Title("sound on/off", 40)
