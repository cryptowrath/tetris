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
x = 30
y = 30
coordinates = [[x, y], [x + 30, y],
              [x + 30, y - 30] , [x + 60, y - 30],
              [x + 60, y] ,[x + 90, y],
              [x + 90, y + 30],[x, y + 30]]

coordinates_x = [coordinates[0][0],
                coordinates[1][0],
                coordinates[2][0],
                coordinates[3][0],
                coordinates[4][0],
                coordinates[5][0],
                coordinates[6][0],
                coordinates[7][0],]

coordinates_y = [coordinates[0][1],
                coordinates[1][1],
                coordinates[2][1],
                coordinates[3][1],
                coordinates[4][1],
                coordinates[5][1],
                coordinates[6][1],
                coordinates[7][1],]

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
        pg.time.delay(10)
        keys = pg.key.get_pressed()
        root.fill(BLUE)
        pg.draw.polygon(root, GREEN, coordinates)

        if keys[K_LEFT]:
            x -= 20
        elif keys[K_RIGHT]:
            for i in coordinates_x:
                i += 20
        elif keys[K_UP]:
            for i in coordinates_y:
                i -= 20
        elif keys[K_DOWN]:
            for i in coordinates_y:
                i += 20
        else:
            for i in coordinates_y:
                i += 20
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
