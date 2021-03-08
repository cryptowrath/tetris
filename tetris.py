import pygame as pg
from pygame.locals import *
import sys

FPS = 60
WHITE = (255, 255, 255)
GREEN = (0, 200, 64)
WEIGHT = 600
HEIGHT = 600



def main():
    global root, x, y, a, b
    a = 50
    b = 50
    x = WEIGHT // 2 
    y = HEIGHT // 2
    pg.init()
    root = pg.display.set_mode((WEIGHT, HEIGHT))
    pg.display.set_caption('Tetris')
    pg.display.update()
    while 1:
            
        for i in pg.event.get():
            if i.type == QUIT:
                pg.quit()
                sys.exit()
            elif i.type == KEYDOWN:
                if i.key ==  K_LEFT:
                    x -= 20
                elif i.key == K_RIGHT:
                    x += 20
                elif i.key == K_UP:
                    y -= 20
                elif i.key == K_DOWN:
                    y += 20
        pg.display.update()
        root.fill(WHITE)
        pg.draw.rect(root, GREEN, (x, y, a, b))
        if y >= HEIGHT + b:
            y -= 20
        elif x >= WEIGHT + a:
            x = 0 - a
        pg.display.update()
    
        
        pg.time.delay(50)
main()
draw()

