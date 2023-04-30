from NeuralNetworkLevel import NeuralNetworkLevel
from Config import SHOW_SPEC_INFO
from random import random, gauss
from Sensors import Sensors


class NeuralNetwork:
    def __init__(self, neurons):
        self.levels = []
        for i in range(len(neurons)-1):
            self.levels.append(NeuralNetworkLevel(neurons[i], neurons[i+1]))
            if SHOW_SPEC_INFO:
                print("lev ", i, "=> in: ", self.levels[i].input, "\t out: ", self.levels[i].output)

    @staticmethod
    def feed_forward(inputs, neural_network):
        output = NeuralNetworkLevel.feed_forward(inputs, neural_network.levels[0])
        if SHOW_SPEC_INFO:
            print("NN f_f output 0: ", output)
        for i in range(1, len(neural_network.levels)):
            output = NeuralNetworkLevel.feed_forward(output, neural_network.levels[i])
            if SHOW_SPEC_INFO:
                print("NN f_f output ", i, " : ", output)
        return output

    @staticmethod
    def mutate(neural_network, per=1):
        for level in neural_network.levels:
            for i in range(len(level.bias)):
                level.bias[i] = Sensors.f_a(level.bias[i], random() * 2 -1, per)
            for i in range(len(level.weights)):
                for j in range(len(level.weights[i])):
                    level.weights[i][j] = Sensors.f_a(level.weights[i][j], random() * 2 -1, per)
