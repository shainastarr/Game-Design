#Shaina Starr
#10/27/21
#We will create a window for settings where the user has options to set:
#Screen size
#Background color
#Object colors
#Sounds on/off

import pygame as py, os, random, time
os.system ('cls')

py.init()
black = (0, 0, 0)
white = (255, 255, 255)
width = 800
height = 800

window = py.display.set_mode((width, height))
py.display.set_caption("settings")


title_font = py.font.SysFont("comic sands", 80)
subtitle_font = py.font.SysFont("comic sands", 50, italic = True)
def display_title(message):
    py.time.delay(100)
    text = title_font.render(message, 1, white)
    window.blit(text, (width/2 - text.get_width()/2, 70))
    py.display.flip()
    py.time.delay(100)
def display_subtitle(message, x, y):
    py.time.delay(100)
    text = subtitle_font.render(message, 1, white)
    window.blit(text, (x, y))
    py.display.flip()
    py.time.delay(100)

run = True
while run:
    for eve in py.event.get():
        if eve.type == py.QUIT:
            run = False
            py.quit()
    display_title("Settings")
    py.time.delay(300)
    
    display_subtitle("Window size",80, 150)
    py.time.delay(300)
    display_subtitle("Background color", 80, 250)
    py.time.delay(300)
    display_subtitle("Object colors", 80, 350)
    py.time.delay(300)
    display_subtitle("Sound (on/off)", 80, 450)
    py.time.delay(300)
py.quit()