import random
from Config import SHOW_SPEC_INFO

class NeuralNetworkLevel:
    def __init__(self, input_size, output_size):
        self.input = [0.0] * input_size
        self.output = [0.0] * output_size
        self.bias = [0.0] * output_size
        self.weights = []
        for i in range(input_size):
            w = []
            for j in range(input_size):
                w.append(0)
            self.weights.append(w)
        self.randomize_network(self)

    @staticmethod
    def randomize_network(neural_network_level):
        for i in range(len(neural_network_level.input)):
            for j in range(len(neural_network_level.output)):
                neural_network_level.weights[i][j] = float(random.randint(-100, 100)) / 100.0
        for i in range(len(neural_network_level.bias)):
            neural_network_level.bias[i] = float(random.randint(-100, 100)) / 100.0

    @staticmethod
    def feed_forward(inputs, neural_network_level):
        if SHOW_SPEC_INFO:
            print("NNL f_f inputs: ", inputs)
        for i in range(len(neural_network_level.input)):
            neural_network_level.input[i] = inputs[i]
        for i in range(len(neural_network_level.output)):
            res = 0
            for j in range(len(neural_network_level.input)):
                res += neural_network_level.input[j] * neural_network_level.weights[j][i]
            neural_network_level.output[i] = 1 if res > neural_network_level.bias[i] else 0
        return neural_network_level.output
