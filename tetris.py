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
COLORS = [WHITE, GREEN, BLUE]
x = 40
y = 0
offset = 20

coordinates = [[x, y], [x + 30, y],
              [x + 30, y - 30] , [x + 60, y - 30],
              [x + 60, y] ,[x + 90, y],
              [x + 90, y + 30],[x, y + 30]]


class Tetramino:
    def __init__(self, coordinates, color, widget):
        self.coordinates = []
        self.color = ""
        self.widget = ""


def main():
    global root

    pg.init()

    root = pg.display.set_mode((WEIGHT, HEIGHT))
    screen_rect = root.get_rect()
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
        tetramino = pg.draw.polygon(root, COLORS[1], coordinates)

        if keys[K_LEFT]:
            for i in coordinates:
                i[0] -= offset
        elif keys[K_RIGHT]:
            for i in coordinates:
                i[0] += offset
        elif keys[K_UP]:
            for i in coordinates:
                i[1] -= offset
        elif keys[K_DOWN]:
            for i in coordinates:
                i[1] += offset
        else:
            for i in coordinates:
                i[1] += offset
        if keys[K_DOWN] and keys[K_LEFT]:
            for i in coordinates:
                i[1] += offset
                i[0] -= offset
        if keys[K_DOWN] and keys[K_RIGHT]:
            for i in coordinates:
                i[1] += offset
                i[0] += offset
        if coordinates[0][0] <= 0 - offset and coordinates[7][0] <= 0 - offset:
            for i in coordinates:
                i[0] += offset
        elif coordinates[6][1] >= HEIGHT + 15 and coordinates[7][1] >= HEIGHT + 15:
            for i in coordinates:
                i[1] -= offset
        pg.display.flip()

        pg.time.delay(50)
main()
