import math
import pygame as pg
from Game.Constants import *


class Road:
    def __init__(self, car):
        self.car = car
        self.lane_W = (WIDTH - 2*ROAD_PADDING) / NUMBER_OF_LANES
        self.lane_borders = []
        self.road_borders = [
            [(ROAD_PADDING, 1000000), (ROAD_PADDING, -1000000)],
            [(WIDTH - ROAD_PADDING, 1000000), (WIDTH - ROAD_PADDING, -1000000)]
        ]

        self.start = self.car.y % LINE_SPACE
        for i in range(ROAD_PADDING + int(self.lane_W), WIDTH - ROAD_PADDING, int(self.lane_W)):
            self.lane_borders.append(i)
            #print(i)

    def draw(self, screen):
        pg.draw.line(screen, (255, 255, 255), (ROAD_PADDING, 0), (ROAD_PADDING, HEIGHT), 5)
        pg.draw.line(screen, (255, 255, 255), (WIDTH - ROAD_PADDING, 0), (WIDTH - ROAD_PADDING, HEIGHT), 5)
        for i in range(ROAD_PADDING + int(self.lane_W), WIDTH - ROAD_PADDING, int(self.lane_W)):
            for j in range(-int(self.start), int(HEIGHT), int(LINE_SPACE)):
                pg.draw.line(screen, (255, 255, 255), (i, j), (i, j + 20))
        self.start = int(self.car.y) % LINE_SPACE

    def change_car(self, car):
        self.car = car
