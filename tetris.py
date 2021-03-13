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
              [x + 90, y + 30],[30, y + 30]]


class Properties:
    def __init__(self, coordinates, color, widget):
        self.coordinates = []
        self.color = ""
        self.widget = ""


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
            for i in coordinates:
                i[0] -= 20
        elif keys[K_RIGHT]:
            for i in coordinates:
                i[0] += 20
        elif keys[K_UP]:
            for i in coordinates:
                i[1] -= 20
        elif keys[K_DOWN]:
            for i in coordinates:
                i[1] += 20
        else:
            for i in coordinates:
                i[1] += 20
        if keys[K_DOWN] and keys[K_LEFT]:
            for i in coordinates:
                i[1] += 20
                i[0] -= 20
        if keys[K_DOWN] and keys[K_RIGHT]:
            for i in coordinates:
                i[1] += 20
                i[0] += 20

        pg.display.update()

        pg.time.delay(50)
main()
