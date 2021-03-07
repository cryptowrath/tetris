import pygame as pg
from pygame.locals import *
import sys

FPS = 60
WHITE = (255, 255, 255)
GREEN = (0, 200, 64)
WIN_WEIGHT = 400
WIN_HEIGHT = 400



def main():
    global root, x, y, a, b
    a = 30
    b = 30
    x = 0 
    y = WIN_HEIGHT // 2
    pg.init()
    root = pg.display.set_mode((WIN_WEIGHT, WIN_HEIGHT))
    pg.display.set_caption('Cryptowrath')
    pg.display.update()
    while 1:
            
        for i in pg.event.get():
            if i.type == QUIT:
                pg.quit()
                sys.exit()
        pg.display.update()
        root.fill(WHITE)
        pg.draw.rect(root, GREEN, (x, y, a, b))
        pg.display.update()
    
        if x >= WIN_WEIGHT + a:
            x = 0 - a
        else:
            x += 2
        
        pg.time.delay(50)
main()
draw()

