import pygame as pg
from random import randint, random
from Game.Constants import *
from Game.Car import Car
from Game.Road import Road
from Game.Obstacle import Obstacle
from NeuralNetwork import NeuralNetwork
from copy import copy, deepcopy
from Config import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.dt = 1
        self.running = True
        self.cars = self.get_cars(50)   # population
        self.road = Road(self.cars[0])
        self.obstacles = []
        self.genre = 0
        self.idx = START_IDX_MIX_GENRE
        self.generate_new_obstacles(self.obstacles, randint(1,4), (2, 0), 600, NUMBER_OF_LANES, self.road.lane_W, ROAD_PADDING, self.cars[0], 45)
        self.run()

    def run(self):
        pg.display.set_caption('Genre: ' + str(self.genre))
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            self.update()

    def update(self):
        self.screen.fill("gray")
        self.road.draw(self.screen)
        curr_car = 0
        for i in range(len(self.cars)):
            if self.cars[i].alive:
                curr_car = i
                break
        for i in range(len(self.cars)):
            self.cars[i].current = False
            if self.cars[i].alive and self.cars[curr_car].y > self.cars[i].y:
                curr_car = i
        self.cars[curr_car].current = True
        self.road.change_car(self.cars[curr_car])
        for obstacle in self.obstacles:
            obstacle.change_car(self.cars[curr_car])
            obstacle.update(self.screen, self.road.road_borders, self.cars)
        self.obstacles[:] = [obstacle for obstacle in self.obstacles if obstacle.active]
        for i in range(len(self.cars)):
            self.cars[i].update(self.screen, self.road.road_borders, self.obstacles, self.cars[curr_car], self.dt)
        self.cars[curr_car].check_active_obstacles(self.obstacles)
        if self.cars[curr_car].active_obstacles is False:
            self.generate_new_obstacles(self.obstacles, randint(1, 4), (2, 0), self.cars[curr_car].y - MIN_SPACE - random() * (MAX_SPACE - MIN_SPACE), NUMBER_OF_LANES, self.road.lane_W, ROAD_PADDING, self.cars[0], 45)
        pg.display.flip()
        self.dt = self.clock.tick(60)
        dead_cars = 0
        for car in self.cars:
            if car.alive is False:
                dead_cars += 1
        if dead_cars == len(self.cars):
            self.create_new_genre()

    def create_new_genre(self):
        print("NEW GENRE")
        self.genre += 1
        pg.display.set_caption('Genre: ' + str(self.genre))
        for car in self.cars:
            car.fitness_score -= car.y * 0.01
            car.fitness_score = car.fitness_score - car.score + car.score * 200 * AGGRESIVENESS
        self.cars.sort(key=lambda x: x.fitness_score, reverse=True)
        for car in self.cars:
            print(car.fitness_score)
        print(self.cars[0].fitness_score)
        if FOLLOW_THE_KING:
            print("FOLLOW THE KING GENRE")
            self.follow_the_king_genre()
        elif TOP_CARS_TO_PARENTS:
            print("TOP CARS TO PARENTS GENRE")
            self.top_fam_genre()
        elif KING_AS_A_PARENT:
            print("KING AS A PARENT GENRE")
            self.king_as_a_parent_genre()
        else:
            print("MIX GENRE", end=" -> ")
            self.idx %= GENRES
            if self.idx == 0:
                print("FOLLOW THE KING GENRE")
                self.follow_the_king_genre()
            elif self.idx == 1:
                print("TOP CARS TO PARENTS GENRE")
                self.top_fam_genre()
            elif self.idx == 2:
                print("KING AS A PARENT GENRE")
                self.king_as_a_parent_genre()
            self.idx += 1
        for i in range(len(self.cars)):
            self.cars[i].reset((250, int(HEIGHT*.65)), int(HEIGHT*.65))
        self.road = Road(self.cars[0])
        self.obstacles = []
        self.generate_new_obstacles(self.obstacles, randint(1,4), (2, 0), 600, NUMBER_OF_LANES, self.road.lane_W, ROAD_PADDING,
                                    self.cars[0], 36)

    @staticmethod
    def get_cars(n):
        cars = []
        for i in range(n):
            cars.append(Car((250, int(HEIGHT*.65)), int(HEIGHT*.65)))
        return cars

    @staticmethod
    def generate_new_obstacles(obstacles, n, speed, y, number_of_lanes, lane_W, lane_padding, car, carW):
        if n < number_of_lanes-1:
            lanes = [True] * number_of_lanes
            numb = randint(0, number_of_lanes-1)
            for i in range(n):
                while lanes[numb] is False:
                    numb = randint(0, number_of_lanes - 1)
                lanes[numb] = False
                obstacles.append(Obstacle((carW + lane_padding + numb * lane_W, y), car, speed[0] + random() * speed[1]))
        else:
            for i in range(n):
                obstacles.append(Obstacle((carW + lane_padding + i * lane_W, y), car, speed[0] + random() * speed[1]))

    def follow_the_king_genre(self):
        leader_nn = self.cars[0].get_nn()

        for i in range(1, len(self.cars)):
            if self.cars[0].get_nn() != leader_nn:
                leader_nn = self.cars[0].get_nn()
            self.cars[i].neural_network = deepcopy(leader_nn)
            NeuralNetwork.mutate(self.cars[i].neural_network, 0.1)

    def top_fam_genre(self):
        n1 = TOP_PERCENT * len(self.cars) // 100
        children = self.cars[:n1]
        n2 = (100 - TOP_PERCENT) * len(self.cars) // 100
        for i in range(n2):
            r = randint(0, n1 - 1)
            parent1 = copy(self.cars[r])
            r = randint(0, n1 - 1)
            parent2 = copy(self.cars[r])
            offspring = parent1.compose_gens(parent2)
            children.append(offspring)
        self.cars = children

    def king_as_a_parent_genre(self):
        n1 = TOP_PERCENT * len(self.cars) // 100
        children = self.cars[:n1]
        n2 = (100 - TOP_PERCENT) * len(self.cars) // 100
        for i in range(n2):
            parent1 = copy(self.cars[0])
            r = randint(0, n1 - 1)
            parent2 = copy(self.cars[r])
            offspring = parent1.compose_gens(parent2)
            children.append(offspring)
        self.cars = children
