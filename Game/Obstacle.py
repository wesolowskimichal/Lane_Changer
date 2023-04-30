import math
import pygame as pg
from Game.Constants import *
from Sensors import Sensors
from random import randint


class Obstacle:
    def __init__(self, pos, car, max_speed):
        self.x = pos[0]
        self.y = pos[1]
        self.drawY = self.y
        self.speed = 0
        self.angle = 0
        self.img = pg.image.load(OBSTACLE_TEXTURES[randint(0, len(OBSTACLE_TEXTURES)-1)])
        self.w, self.h = self.img.get_size()
        self.area = []
        self.max_speed = max_speed
        self.car = car
        self.active = True

    def update(self, screen, road_borders, cars):
        self.controls()
        self.draw(screen)
        self.check_if_active(cars)
        self.check_collision(road_borders)

    def check_if_active(self, cars):
        self.active = False
        for car in cars:
            distance = abs(self.y - car.y)
            if distance <= MAX_SPACE:
                self.active = True

    def change_car(self, car):
        self.car = car

    def controls(self):

        self.speed += ACCELERATION

        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < -self.max_speed/2:
            self.speed = -self.max_speed/2

        if self.speed > 0:
            self.speed -= FRICTION
        if self.speed < 0:
            self.speed += FRICTION

        if abs(self.speed) < FRICTION:
            self.speed = 0

        self.x += self.speed * math.sin(self.deg_to_rad(self.angle))
        self.y -= self.speed * math.cos(self.deg_to_rad(self.angle))
        self.drawY = self.y - self.car.y
        #print(self.car.y , self.y, self.drawY)

    def draw(self, screen):
        img_rect = self.img.get_rect(topleft=(self.x - self.w / 2, self.drawY - self.h / 2))
        ctp_off = pg.math.Vector2((self.x, self.drawY)) - img_rect.center
        rot_off = ctp_off.rotate(self.angle)
        rot_img_center = (self.x - rot_off.x, self.drawY - rot_off.y)
        rot_img = pg.transform.rotate(self.img, -self.angle)
        rot_img_rect = rot_img.get_rect(center=rot_img_center)
        screen.blit(rot_img, rot_img_rect)

        topleft = (rot_img_rect.topleft[0] + 5, rot_img_rect.topleft[1])
        bottomleft = (rot_img_rect.bottomleft[0] + 5, rot_img_rect.bottomleft[1])
        topright = (rot_img_rect.topright[0] - 5, rot_img_rect.topright[1])
        bottomright = (rot_img_rect.bottomright[0], rot_img_rect.bottomright[1])


        self.area = ((topleft, bottomleft), (topright, topleft), (topright, bottomright),  (bottomright, bottomleft))
        # pg.draw.rect(screen, (255, 0, 0), (rot_img_rect.topleft, rot_img.get_size()), 1)

    def check_collision(self, road_borders):
        for border in road_borders:
            if Sensors.intersection(self.area[0][0], self.area[0][1], border[0], border[1]) is not None:
                print("LOSE")
            if Sensors.intersection(self.area[1][0], self.area[1][1], border[0], border[1]) is not None:
                print("LOSE")

    @staticmethod
    def deg_to_rad(angle):
        return float(angle) * math.pi / 180.0
