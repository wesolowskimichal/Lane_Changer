import math
import pygame as pg


class Sensors:
    def __init__(self, car, number_of_sensors=3, sensor_length=100):
        self.car = car
        self.number_of_sensors = number_of_sensors
        self.sensor_length = sensor_length
        self.sensor_spread = 120
        self.sensors = []
        self.bds = []

    def update(self, screen, road_borders, obstacles):

        def get_bd(s, r_b):
            t = []
            for border in r_b:
                inter = self.intersection(s[0], s[1], border[0], border[1])
                if inter is not None:
                    t.append(inter)
            if len(t) == 0:
                return False
            offs = []
            for x, y, off in t:
                offs.append(off)
            min_off = min(offs)
            for x, y, off in t:
                if min_off == off:
                    return [x, y, off]

        self.bds = []
        for sensor in self.sensors:
            self.bds.append(get_bd(sensor, road_borders))
        for i in range(len(self.sensors)):
            for obstacle in obstacles:
                res = get_bd(self.sensors[i], obstacle.area)
                if res is not False:
                    if self.bds[i] is not False:
                        self.bds[i] = min(res, self.bds[i])
                    else:
                        self.bds[i] = res
        self.update_sensors(screen)


    @staticmethod
    def intersection(A, B, C, D):
        s1x = B[0] - A[0]
        s1y = B[1] - A[1]
        s2x = D[0] - C[0]
        s2y = D[1] - C[1]
        dz = -s2x * s1y + s1x * s2y
        if dz == 0:
            return None
        s = (-s1y * (A[0] - C[0]) + s1x * (A[1] - C[1])) / (-s2x * s1y + s1x * s2y)
        t = (s2x * (A[1] - C[1]) - s2y * (A[0] - C[0])) / (-s2x * s1y + s1x * s2y)
        if s >= 0 and s <= 1 and t >= 0 and t <= 1:
            p1, p2 = A[0] + (t * s1x), A[1] + (t * s1y)
            offset = math.sqrt((p1 - A[0]) ** 2 + (p2 - A[1]) ** 2) / math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)
            return p1, p2, offset
        return None

    def update_sensors(self, screen):
        self.sensors = []
        for i in range(self.number_of_sensors):
            if self.number_of_sensors == 1:
                angle = self.f_a(self.sensor_spread / 2, -self.sensor_spread / 2, .5) - self.car.angle
            else:
                angle = self.f_a(self.sensor_spread / 2, -self.sensor_spread / 2,
                                 i / (self.number_of_sensors - 1)) - self.car.angle
            start = (self.car.x, self.car.offset)
            end = (self.car.x - math.sin(self.car.deg_to_rad(angle)) * self.sensor_length,
                   self.car.offset - math.cos(self.car.deg_to_rad(angle)) * self.sensor_length)
            self.sensors.append([start, end])
        # for i in range(len(self.sensors)):
        #     pt = self.sensors[i][1]
        #     if i < len(self.bds) and self.bds[i] is not False:
        #         pt = self.bds[i][:2]
        #     pg.draw.line(screen, (122, 140, 150), self.sensors[i][0], pt)
        #     pg.draw.line(screen, (255, 0, 0), pt, self.sensors[i][1])

    @staticmethod
    def f_a(a, b, c):           # linear interpolation
        return a + (b - a) * c
