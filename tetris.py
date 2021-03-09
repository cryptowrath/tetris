import pygame as pg
from pygame.locals import *
import sys
from random import *

FPS = 60
WHITE = (255, 255, 255)
GREEN = (0, 200, 64)
BLUE = (0, 0, 255)
WEIGHT = 400
HEIGHT = 800

    
def main():
    global root, x, y, a, b
    a = 100
    b = 50
    x = WEIGHT // 2 
    y = 0 - b
    pg.init()
    root = pg.display.set_mode((WEIGHT, HEIGHT))
    pg.display.set_caption('Tetris')
    pg.display.update()
    while 1:
            
        for i in pg.event.get():
            if i.type == QUIT:
                pg.quit()
                sys.exit()
        
        pg.display.update()
        root.fill(BLUE)
        pg.draw.rect(root, GREEN, (x, y, a, b))
        keys = pg.key.get_pressed()
        if keys[K_LEFT]:
            x -= 20
        elif keys[K_RIGHT]:
            x += 20
        elif keys[K_UP]:
            y -= 20
        elif keys[K_DOWN]:
            y += 20
        else:
            y += 20
        if keys[K_DOWN] and keys[K_LEFT]:
            x -= 20
            y += 20
        if keys[K_DOWN] and keys[K_RIGHT]:
            y += 20
            x += 20
        if y >= HEIGHT + b:
            y = 0 - b
        elif x >= WEIGHT + a:
            x = 0 - a
        elif x <= 0 - a:
            x = WEIGHT + a
        elif y <= 0 - b:
            y = HEIGHT + b
        pg.display.update()
    
        
        pg.time.delay(50)
main()


