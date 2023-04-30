import math
import pygame as pg
from Game.Constants import *
from Sensors import Sensors
from NeuralNetwork import NeuralNetwork
from Config import SHOW_KEY_INFO, AGGRESIVENESS
import numpy as np
from random import random, randint


class Car:
    def __init__(self, pos, drawY):
        self.x = pos[0]
        self.y = pos[1]
        self.drawY = drawY
        self.offset = 0
        self.speed = 0
        self.angle = 0
        self.current = False
        self.alive = True
        self.active_obstacles = True
        self.img = pg.image.load(PATH + '\\Game\\red.png')
        self.w, self.h = self.img.get_size()
        self.sensors = Sensors(self, 20, 250)
        self.score = 0
        self.fitness_score = 0
        self.time_since_last_point = 0
        self.time_to_reach_point = 60000 // 2
        self.neural_network = NeuralNetwork([self.sensors.number_of_sensors, 20, 4])   # sensors | hidden layer | neurons (forward, backward, left, right)
        self.area = []
        # slalom
        self.curves_made = 0

    def reset(self, pos, drawY):
        self.x = pos[0]
        self.y = pos[1]
        self.drawY = drawY
        self.offset = 0
        self.speed = 0
        self.angle = 0
        self.current = False
        self.alive = True
        self.active_obstacles = True
        self.w, self.h = self.img.get_size()
        self.sensors = Sensors(self, 20, 250)
        self.score = 0
        self.fitness_score = 0
        self.time_since_last_point = 0
        self.time_to_reach_point = 60000
        self.area = []

    def update(self, screen, road_borders, obstacles, curr_car, dt):
        if self.alive and self.score == self.fitness_score:
            self.time_since_last_point += dt
        elif self.alive and self.score != self.fitness_score:
            self.time_since_last_point = 0
            self.fitness_score = self.score
        if self.alive and self.time_since_last_point > self.time_to_reach_point:
            self.fitness_score -= 100 * AGGRESIVENESS
            self.alive = False

        self.active_obstacles = True
        if self.alive:
            if self.current:
                self.img = pg.image.load(PATH + '\\Game\\red.png')
            else:
                self.img = pg.image.load(PATH + '\\Game\\red_not_current.png')
            self.sensors.update(screen, road_borders, obstacles)
            offsets = []    # to achieve lower values when object is far away and higher values if is close, very similar to flashlight
            for i in range(self.sensors.number_of_sensors):
                if i >= len(self.sensors.bds) or self.sensors.bds[i] is False:
                    offsets.append(0)
                else:
                    offsets.append(1 - self.sensors.bds[i][2])
            outputs = NeuralNetwork.feed_forward(offsets, self.neural_network)
            self.controls(outputs)
            self.draw(screen, curr_car)
            self.check_collision(road_borders, obstacles)
        else:
            self.img = pg.image.load(PATH + '\\Game\\dead_car.png')
            self.draw(screen, curr_car)

    def check_active_obstacles(self, obstacles):
        self.active_obstacles = False
        temp = 0
        for obstacle in obstacles:
            if obstacle.drawY < self.offset:
                self.active_obstacles = True
            else:
                temp += 1
        self.score = temp if self.score < temp else self.score

    def get_controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.angle -= 1
        if keys[pg.K_RIGHT]:
            self.angle += 1
        if keys[pg.K_UP]:
            self.speed += ACCELERATION
        if keys[pg.K_DOWN]:
            self.speed -= ACCELERATION

    def get_ai_controls(self, ouput):
        if SHOW_KEY_INFO:
            print("output: ", ouput)
        if ouput[0] == 1:
            self.angle -= 1
            self.curves_made += 1
        if ouput[1] == 1:
            self.angle += 1
            self.curves_made += 1
        if ouput[2] == 1:
            self.speed += ACCELERATION
        if ouput[3]:
            self.speed -= ACCELERATION

    def controls(self, output):
        #self.get_controls()
        self.get_ai_controls(output)

        if self.speed > MAX_SPEED:
            self.speed = MAX_SPEED
        if self.speed < -MAX_SPEED/2:
            self.speed = -MAX_SPEED/2

        if self.speed > 0:
            self.speed -= FRICTION
        if self.speed < 0:
            self.speed += FRICTION

        if abs(self.speed) < FRICTION:
            self.speed = 0

        self.x += self.speed * math.sin(self.deg_to_rad(self.angle))
        self.y -= self.speed * math.cos(self.deg_to_rad(self.angle))

    def draw(self, screen, curr_car):
        d = curr_car.offset + (self.y - curr_car.y)
        if self.current:
            d = self.drawY
        self.offset = d
        img_rect = self.img.get_rect(topleft=(self.x - self.w/2, d - self.h/2))
        ctp_off = pg.math.Vector2((self.x, d)) - img_rect.center
        rot_off = ctp_off.rotate(self.angle)
        rot_img_center = (self.x - rot_off.x, d - rot_off.y)
        rot_img = pg.transform.rotate(self.img, -self.angle)
        rot_img_rect = rot_img.get_rect(center=rot_img_center)
        screen.blit(rot_img, rot_img_rect)

        topleft = (rot_img_rect.topleft[0] + 5, rot_img_rect.topleft[1])
        bottomleft = (rot_img_rect.bottomleft[0] + 5, rot_img_rect.bottomleft[1])
        topright = (rot_img_rect.topright[0] - 5, rot_img_rect.topright[1])
        bottomright = (rot_img_rect.bottomright[0], rot_img_rect.bottomright[1])

        self.area = ((topleft, bottomleft), (topright, topleft), (bottomright, bottomleft))

    def check_collision(self, road_borders, obstacles):
        for border in road_borders:
            if Sensors.intersection(self.area[0][0], self.area[0][1], border[0], border[1]) is not None:
                self.alive = False
            if Sensors.intersection(self.area[1][0], self.area[1][1], border[0], border[1]) is not None:
                self.alive = False
        for obstacle in obstacles:
            for point in obstacle.area:
                if Sensors.intersection(self.area[0][0], self.area[0][1], point[0], point[1]) is not None:
                    self.alive = False
                if Sensors.intersection(self.area[1][0], self.area[1][1], point[0], point[1]) is not None:
                    self.alive = False
                if Sensors.intersection(self.area[2][0], self.area[2][1], point[0], point[1]) is not None:
                    self.alive = False
            if Sensors.intersection(self.area[1][0], self.area[1][1], obstacle.area[0][0], obstacle.area[0][1]) is not None:
                self.alive = False

    @staticmethod
    def deg_to_rad(angle):
        return float(angle) * math.pi / 180.0

    def get_nn(self):
        return self.neural_network

    def compose_gens(self, parent_car, mutation_prob=0.1):
        chromosome = NeuralNetwork([self.sensors.number_of_sensors, 10, 4])

        for l in range(len(chromosome.levels)):
            for i in range(len(chromosome.levels[l].bias)):
                r = np.random.rand()
                if r < 0.47:
                    chromosome.levels[l].bias[i] = parent_car.neural_network.levels[l].bias[i]
                elif r > 0.95:
                    continue
                else:
                    chromosome.levels[l].bias[i] = self.neural_network.levels[l].bias[i]
            for i in range(len(chromosome.levels[l].weights)):
                for j in range(len(chromosome.levels[l].weights[i])):
                    r = np.random.rand()
                    if r < 0.5:
                        chromosome.levels[l].weights[i][j] = parent_car.neural_network.levels[l].weights[i][j]
                    else:
                        chromosome.levels[l].weights[i][j] = self.neural_network.levels[l].weights[i][j]

        for l in range(len(chromosome.levels)):
            for i in range(len(chromosome.levels[l].bias)):
                r = np.random.rand()
                if r < mutation_prob:
                    chromosome.levels[l].bias[i] += np.random.normal(0, 0.1)
            for i in range(len(chromosome.levels[l].weights)):
                for j in range(len(chromosome.levels[l].weights[i])):
                    r = np.random.rand()
                    if r < mutation_prob:
                        chromosome.levels[l].weights[i][j] += np.random.normal(0, 0.1)

        new_car = self
        new_car.neural_network = chromosome
        new_car.reset((250, int(HEIGHT * .65)), int(HEIGHT * .65))
        return new_car
