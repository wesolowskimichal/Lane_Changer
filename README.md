"Visualizing neural network learning in an auto driving game"  
---  
  
## Abstract  
The purpose of this work is to present a program that visually demonstrates the learning process of artificial intelligence in the environment of a car moving on the road with other cars. The work will include a general description of the program, its structure and functioning. Everything was implemented without using additional libraries, except for "PyGame," which was used to draw objects in the window.  
  
### Keywords  
Neural networks, Genetic algorithm, Artificial intelligence, AI in the game  
  
# Introduction  
  
Artificial intelligence (AI) is a field of computer science that focuses on creating intelligent systems capable of performing tasks that typically require human intelligence. AI encompasses a wide range of technologies, algorithms, and methodologies aimed at enabling machines to perceive, understand, reason, and learn from data or experiences.  
  
Artificial intelligence (AI) has witnessed significant advancements in recent years, driven by the increasing digitalization, enhanced computing power, and the availability of vast amounts of data. This progress has led to the development of AI programs and systems capable of processing information and making decisions based on acquired knowledge. One prominent application of AI is in the field of autonomous driving, where intelligent systems learn to navigate roads, avoid obstacles, and ensure passenger safety.  
  
This work presents a program that visually demonstrates the learning process of artificial intelligence in a simulated driving environment. Specifically, the program focuses on a car moving on a road alongside other vehicles. The primary objective is for the artificial intelligence to learn how to drive on the road effectively, avoiding collisions with other cars and safely maneuvering through traffic.  
  
The learning process is facilitated by a machine learning algorithm that analyzes various factors, including the car's speed, direction of travel, and data from its sensors. Based on this information, the artificial intelligence makes decisions regarding the car's movement, simulating the decision-making process of a human driver.  
  
The program incorporates visualization elements to provide real-time feedback on the learning process. A visual board displays the car's trajectory, movement traces, and other relevant information, enabling users to observe and analyze the AI's decision-making and learning capabilities. To optimize learning outcomes, the program utilizes advanced techniques such as cost functions, neural network mutation, parallelization, and more.  
  
The implementation of this program does not rely on external libraries, except for PyGame, which is used to render objects and create an immersive graphical interface. By providing a practical example of AI in action, this project offers valuable insights into the workings of machine learning algorithms and the decision-making process of artificial intelligence in complex interactive environments.  
  
Moreover, this program serves as an educational tool for individuals interested in understanding the basics of machine learning and exploring its applications in autonomous driving. Researchers and enthusiasts can also leverage this project as a starting point for further investigation and experimentation in the field of AI and its intersection with autonomous systems.  
  
In the following sections, we will delve into the program's structure, functioning, and the techniques employed to facilitate the learning process of the artificial intelligence. Through this exploration, we aim to shed light on the capabilities and potential of AI in the domain of autonomous driving and inspire further advancements in the field.  
  
---  
# General description of the program  
  
The main goal of this project is to showcase the learning process of artificial intelligence in a visual way using a program that simulates a car driving on a road with other cars. The program was developed without the use of any additional libraries, except for PyGame which was used to draw objects in the window.  
  
The program simulates a driving scenario where the car must navigate through other cars on the road. The car is controlled by a neural network that is trained through a genetic algorithm and reinforcement learning. The neural network takes input from the car's sensors, which includes information such as the car's speed and distance from other cars on the road. Based on this input, the neural network generates output, which determines the car's movement and direction.  
  
The program is designed to show the learning process of the neural network in real-time, with the car's movements being displayed on the screen. The program structure consists of two main parts: the neural network and the game environment. The neural network is implemented using a simple structure consisting of two classes: "NeuralNetwork" and "NeuralNetworkLevel". The "NeuralNetwork" class contains the entire neural network, while the "NeuralNetworkLevel" class stores one neural network level. The neural network is designed with one input layer and one hidden layer, which are connected to each other and generate output data.  
  
The game environment consists of a road with other cars driving on it. The cars move randomly, changing lanes and accelerating or decelerating. The car controlled by the neural network must navigate through this environment while avoiding collisions with other cars. The car's position on the road and its distance from other cars are determined by its sensors, which feed data into the neural network.  
  
To train the neural network, a genetic algorithm is used. The algorithm generates a population of cars with random parameters, which are then evaluated based on their fitness scores. The fitness score is determined by how far the car has traveled and how many cars it has overtaken. The algorithm then selects the best-performing cars as parents for the next generation, which are used to generate new cars with mutated parameters. This process is repeated for multiple generations, gradually improving the performance of the cars.  
  
In addition to the genetic algorithm, reinforcement learning is also used to train the neural network. The car receives a reward for passing another car without a collision, and a penalty for failing to overtake a car for a certain period of time. This reward/punishment system is designed to encourage the car to make safe and efficient driving decisions.  
  
Overall, this program provides a visual representation of the learning process of artificial intelligence in a driving scenario. It showcases the use of neural networks, genetic algorithms, and reinforcement learning in training an AI system to make intelligent driving decisions.  
  
---  
# Neural Networks  
Artificial intelligence (AI) is a field of computer science that focuses on creating programs and systems capable of processing information and making decisions based on previously acquired knowledge. In recent years, the development of AI has been rapidly accelerating due to the increasing digitization, the growing computing power of computers, and the availability of vast amounts of data, which has made it possible to create more advanced learning algorithms. AI has vast applications in many areas of life, including medicine, industry, logistics, and finance. It enables automation of production processes, optimization of transportation routes, and diagnosis of diseases based on data analysis, among other things.  
  
In our project, we utilize artificial intelligence to teach models how to play Lane Changer. Neural networks are one of the most popular tools in the field of machine learning, allowing automatic learning from data. They consist of a series of interconnected neurons that process input data and generate output data. We use deep neural networks (DNNs), which are capable of learning complex relationships between input and output data. In this case, the input is the state of the game, i.e., the data taken from the car's sensors, and the output is the decisions the model should make, i.e., what move it should make. The neural network's task is to learn which moves are beneficial in certain situations and which ones should be avoided. In the project, we use a simple structure for creating neural networks, consisting of two classes: "NeuralNetwork" and "NeuralNetworkLevel," where the first one contains the entire neural network, and the second one stores one neural network level.  
  
We create a simple model with one input layer and one hidden layer that are connected to each other and generate output data. We use a genetic algorithm to generate better and better models. Each model has a fitness score, and the results of the cars are sorted accordingly. Depending on the genetic algorithm, a given number of the best cars are taken as parents for the next generation. The project also uses reinforcement learning, which is a different approach to teaching artificial intelligence. With reinforcement learning, the model learns based on the rewards or punishments it receives for its decisions. Rewards are given when the model makes favorable decisions, and penalties are given when it makes unfavorable ones.  
  
In this project, we assign a reward for passing and overtaking a car without collision and a penalty for not overtaking a car for 30 seconds. The system of rewards and penalties is designed to make the cars avoid collisions as much as possible. The visualization of the learning process takes place on a board, where the car's movement traces and other information about the learning state are drawn in real-time. During the learning process, we use various techniques such as cost functions, neural network mutation, and parallelization to obtain the best possible results.  
  
---  
# Genetic Algorithm  
  
Genetic algorithms (GAs) are a type of optimization algorithm that mimic natural selection to solve complex problems. They are inspired by the principles of evolutionary biology, such as inheritance, mutation, and selection. These algorithms are widely used in many fields, including engineering, biology, finance, and computer science. Their ability to find optimal solutions to complex problems makes them a valuable tool for many scientists and engineers.  
  
In the context of the "Lane Changer" game, the genetic algorithm's main goal is to find the best set of parameters that will affect the behavior of cars in the game. The genetic algorithm will be run multiple times, and each run will use a population of random parameter sets. The algorithm's success depends on the quality of the parameter sets generated, and how well they enable the cars to navigate the game environment.  
  
Each generation of the genetic algorithm begins with a population of potential solutions, in this case, cars with specific parameter sets. The cars' performance is evaluated based on their fitness score, which is determined by a set of criteria, such as the number of cars a vehicle has overtaken, how far it has gone, and whether it has simply started following the car in front of it. The best cars with the highest fitness scores are then selected to pass their genetic material to the next generation.  
  
The selection process involves choosing the best solutions based on fitness scores. In the "Lane Changer" game, the fitness score consists of several components, such as the car's progress in the game, the number of cars overtaken, and whether the car has collided with any obstacles. The better a car performs, the higher its fitness score, and the more likely it is to be selected for the next generation.  
  
After selecting the best solutions, the crossover process takes place, where the selected solutions share genetic information to create new offspring with new parameter sets. This process mimics natural reproduction, where offspring inherit genetic material from both parents. The new solutions are then evaluated, and the best ones are selected to create the next generation population.  
  
The mutation process takes place to introduce diversity in the population. Mutation involves changing the parameter sets of selected solutions slightly. This introduces variation in the population, which increases the chances of finding better solutions that were not previously explored.  
  
The genetic algorithm runs through multiple generations, selecting the best solutions, creating offspring, and mutating their parameter sets. The algorithm continues until it reaches a satisfactory solution, or until it reaches a pre-set number of generations.  
  
## Types of Genetic Algorithms  
  
The application presents 3 genetic algorithms:  
  
- **Follow The King:** In this method, models mutate from the car with the highest fitness score. This is the method that best visualizes the mutation. You can see well how cars with similar neural networks make decisions slightly different from each other and constantly evolve to a better and better form. The mutation time of models to a very well-driving form is very dependent on generation 0, a generation generated completely at random.  
  
- **Top Family As Parents:** In this method, a given percentage of the best cars stay in the next generation. Parents are then randomly selected from this percentage and their networks mutate to form a new model. The specification of gene takeover in the project looks as follows: 46% for the first parent's gene, 5% for the new random gene, and 49% for the second parent's gene. Then begins the process of mutating the weights and levels of bias for additional network mutation. Animals work similarly to this algorithm, where the strongest individuals are paired with other best-functioning individuals to create the best possible family.  
  
- **King As Parent:** An algorithm that works in the same way as Top Family As Parents with the difference that one parent will always be the best car of the generation. This ensures that the genes of the best car are always likely to be passed on.  
  
As an additional feature of the program, a "MIX\_GENRE" mode has been introduced, where you can see how the process of learning the cars looks like where a different genetic algorithm is selected with each generation.  
  
# Implementation  
  
## Game  
  
The game consists of 5 base classes:  
  
---
### Game  
  
The `Game` is the main class that initializes the game and runs the main game loop. The `get_cars()` method creates a list of Car objects representing AI-controlled cars. The `generate_new_obstacles()` method generates a new set of obstacles randomly on the road.  
  
The `create_new_genre()` method is a genetic algorithm that creates a new generation of AI-controlled cars. It calculates each car's fitness score based on the distance traveled and the number of obstacles it avoids. It then sorts the cars according to their fitness score and selects those with the best scores as parents for the next generation. The new generation is created by applying crossover and mutation to the parents' neural networks.  
  
---
#### Algorithm: Game.create_new_genre  
  
**Input:** `self` - reference to the current object  
**Output:** None  
  
1. Update `self.genre`:  
```Python  
self.genre = self.genre + 1  
```  
  
2. Update display caption:  
```Python  
pg.display.set_caption('Genre: ' + str(self.genre))  
```  
  
3. Iterate over cars and update fitness score:  
```Python  
for car in self.cars:  
car.fitness_score = car.fitness_score - car.y * 0.01  
```  
  
4. Sort cars by fitness score:  
```Python  
self.cars.sort(key=lambda x: x.fitness_score, reverse=True)  
```  
  
5. Determine next steps based on conditions:  
- If `FOLLOW_THE_KING` is true, call `self.follow_the_king_genre()`.  
- If `TOP_CARS_TO_PARENTS` is true, call `self.top_fam_genre()`.  
- If `KING_AS_A_PARENT` is true, call `self.king_as_a_parent_genre()`.  
- Otherwise:  
```Python
self.idx = self.idx % GENRES  
if self.idx == 0:  
self.follow_the_king_genre()  
elif self.idx == 1:  
self.top_fam_genre()  
elif self.idx == 2:  
self.king_as_a_parent_genre()  
self.idx = self.idx + 1  
```  
  
6. Reset cars:  
```  Python
for i in range(len(self.cars)):  
self.cars[i].reset((250, int(HEIGHT * 0.65)), int(HEIGHT * 0.65))  
```  
  
7. Initialize `self.road` and `self.obstacles`:  
```Python
self.road = Road(self.cars[0])  
self.obstacles = []  
```  
  
8. Generate new obstacles:  
```Python
self.generate_new_obstacles(self.obstacles, randint(1,4),  
						    (2, 0), 600, NUMBER_OF_LANES,  
							self.road.lane_W, ROAD_PADDING,  
							self.cars[0], 36)  
```  
There are several possible species that the genetic algorithm follows. The `FOLLOW_THE_KING` species selects the best-performing car as the sole parent for the next generation. The `TOP_CARS_TO_PARENTS` species selects a fixed percentage of the best-performing cars as parents for the next generation. The `KING_AS_A_PARENT` species selects the car with the best performance as a single parent for all new descendants. Finally, the `MIX_GENRE` species randomly selects one of the above species for each new generation.  
  
---
### Car  
  
The `Car` class is defined to represent the car object in the game. After initialization, the class sets the position, speed and angle of the car to zero and loads the image of the car. It also creates an instance of the Sensors class, which is responsible for detecting obstacles on the road.  
  
This class has methods that reset the car, update its state and control its movement. The update method takes the screen, road boundaries, obstacles, the current car and the time delta as input parameters. It checks whether the car is alive and updates its state accordingly. The method also calls the `check_collision` method to determine if the car has collided with any obstacles. The draw method is used to render the car on the screen.  
  
The class also has methods to get controls for the car. The `get_controls` method takes keystrokes to control the car, while the `get_ai_controls` method takes the output of a neural network to control the car.  
  
Overall, the Car class represents the car object in the game and contains methods to control its movement and update its state.  

---
### Car.compose_gens
#### Parameters:

-   **self:** The current object or instance of the class.
-   **parent_car:** Another car object, likely serving as a parent in genetic operations.
-   **mutation_prob:** Probability of mutation. Default is set to 0.1.

#### Method Implementation:

1.  **Initialize a new chromosome (neural network):**
    
    ```Python
    chromosome = NeuralNetwork([self.sensors.number_of_sensors, 10, 4])` 
    ```
    -   This line creates a new neural network (`chromosome`) with a specific architecture `[self.sensors.number_of_sensors, 10, 4]`. It seems to have three levels with 10 neurons in the second level and 4 neurons in the third level.
2.  **Genetic Crossover:**
    
```Python
    `for l in range(len(chromosome.levels)):
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
                    chromosome.levels[l].weights[i][j] = self.neural_network.levels[l].weights[i][j]` 
```
    -   This section performs genetic crossover (combination of genetic information) by iterating through each level, bias, and weight of the neural network.
    -   The bias and weight values are chosen from either the parent or the current object's neural network based on random probabilities (`r` values).
3.  **Mutation:**
    
```Python
    `for l in range(len(chromosome.levels)):
        for i in range(len(chromosome.levels[l].bias)):
            r = np.random.rand()
            if r < mutation_prob:
                chromosome.levels[l].bias[i] += np.random.normal(0, 0.1)
        for i in range(len(chromosome.levels[l].weights)):
            for j in range(len(chromosome.levels[l].weights[i])):
                r = np.random.rand()
                if r < mutation_prob:
                    chromosome.levels[l].weights[i][j] + np.random.normal(0, 0.1)` 
```
    -   This section introduces mutation by iterating through each level, bias, and weight of the neural network.
    -   If a random value (`r`) is less than the specified mutation probability (`mutation_prob`), a small random value from a normal distribution is added to the corresponding bias or weight.
4.  **Create a new car with the modified neural network:**
    
```Python
    new_car = self
    new_car.neural_network = chromosome
    new_car.reset((250, int(HEIGHT * .65)), int(HEIGHT * .65))
    return new_car
```
    
    -   A new car object is created as a copy of the current car (`self`).
    -   The neural network of the new car is set to the modified neural network (`chromosome`).
    -   The car is then reset to a specified position.

  
---
### Sensors  
  
The `Sensors` class is responsible for detecting obstacles by the car in the game simulation. This class has helper functions for detecting the intersection points between the line running from the car's sensor and the road borders or obstacles.  
  
The `update(self, screen, road_borders, obstacles)` method is responsible for updating the state of the sensors and detecting obstacles on the road. This function creates a list of borders for each sensor based on the road borders and obstacles, and then draws lines from the car to the border points.  
  
The `intersection(A, B, C, D)` method is a helper function that determines the intersection point between two sections.  
  
---
### Algorithm: Sensor.intersection  
  
**Input:** \(A, B, C, D\) - Points defining the line segments  
**Output:** Intersection point coordinates \((p_1, p_2)\) and offset  
  
1. Calculate the coordinates of the directional vectors of line segments AB and CD  
```Python  
s1x = B[0] - A[0]  
s1y = B[1] - A[1]  
s2x = D[0] - C[0]  
s2y = D[1] - C[1]  
```  
  
2. Calculate determinant of the two directional vectors  
```Python  
dz = -s2x * s1y + s1x * s2y  
```  
  
3. Determine if two vectors are parallel  
- `If (dz == 0)`, **return** `None`  
  
4. Calculate the parameters of the line equations for the line segments  
```Python  
s = (-s1y * (A[0] - C[0]) + s1x * (A[1] - C[1])) / (-s2x * s1y + s1x * s2y)  
t = ( s2x * (A[1] - C[1]) - s2y * (A[0] - C[0])) / (-s2x * s1y + s1x * s2y)  
```  
5. Determine if both s and t are within the range [0, 1], it means the intersection point is within both line segments  
  
- If s >= 0 **and** s <= 1 **and** t >= 0 **and** t <= 1:
 $$ p1, p2 = A[0] + (t \cdot s1x), A[1] + (t \cdot s1y) $$
 $$ offset = {\sqrt{p1 - A[0])^2 + (p2 - A[1])^2} \over\sqrt{(B[0] - A[0])^2 + (B[1] - A[1])^2}} $$
 **return** `p1, p2, offset`
 - Else, **return** `None`
  
---
### Constants  
  
The `Constants` file contains definitions of several constants and a list of textures for the game. These constants include window dimensions, car properties, number of road lanes, distance between lines on the road, and obstacle dimensions. The texture list contains paths to the graphics files that will be used in the game as textures for obstacles
  
---
### Road  
  
The `Road` class is responsible for drawing and updating the road on the screen, along with the lines separating the lanes. This class takes a `Car` object, which is used to determine the position and movement on the road. In the constructor, a road is created along with lanes and separating lines. The lane width is calculated based on constants defined in the `Constants` file. Next, the road’s borders are created, consisting of two vertical lines at the edges of the screen. The lane boundaries are stored in the `lane_borders` list. The `draw` method draws the road and lane borders, as well as the lines separating the lanes. These lines are drawn in loops, and their position is calculated based on the position of the car on the road. In the `change_car` method, the position of the car on the road is updated, which is necessary for the correct drawing of the lines separating the lanes on the screen.

---
### Summary
The main objective of the game is to drive on the highway and evade the cars on it. New obstacles appear every given period of time. Basic laws of physics such as acceleration have been implemented in the game.

  ---
## Neural Networks  
  
In this system, each car has its own neural network that acts as its "brain." To create the network, a list of neurons is passed, which is derived from the number of sensors, the size of hidden layers and the number of possible driving directions. In this case, the number of directions is 4: `right`, `left`, `up` and `down`. The neural network then creates a series of levels, where each level is represented by a `NeuralNetworkLevel` object. Each level is responsible for accepting inputs from the previous level and generating outputs for the next level. The input size for each level is based on the number of neurons in the previous level, while the output size is based on the number of neurons in the current level. Each level creates a layer of `inputs`, `outputs`, `biases` and `weights`. The weights and biases are initially set to random values between -1 and 1. When the car drives, it uses its `sensors` to gather information about the environment. Specifically, it uses the offset from each sensor and subtracts it from 1. This is done so that readings are lower when objects are far away, which more closely simulates human reactions. For example, when something suddenly appears in front of our car, we instinctively hit the brakes hard. The AI will do the same because of this scaling. Finally, the `feed forward` function is used to calculate the output of the neural network based on the input data collected from the sensors. This output is then used to determine the car’s actions, such as accelerating, braking or turning. Below is a description of the function: The algorithm is divided into 2 algorithms located in other classes:
  
---
### NeuralNetworkLevel.feed_forward  
  
Function yakes two arguments: 
`inputs` - a list of input values to be passed to the neural network, and
 `neural_network_level` - an instance of the `NeuralNetworkLevel` class that represents a single layer of the neural network. 
 This function implements the feedforward algorithm for the neural network, which computes the output values of the network given a set of input values. The function first initializes the input values of the neural network layer with the input values passed as an argument. It then loops over each output node in the layer and computes its output value by taking the dot product of the input values and their corresponding weights, adding the bias, and applying a step function to the result to obtain a binary output (either 0 or 1). The step function used here is a threshold function that outputs 1 if the input value is greater than the bias and 0 otherwise. The function returns the output values of the neural network layer, which can be used as input values for the next layer of the network or as the final output values of the network.
 
**Input:** `inputs`- list of input values, `neural_network_level` - neural network level
**Output:** neural network level output
1. Iterate over neural network level inputs and assign each input value to the corresponding neuron in the neural network's input layer
```Python
for i in range(len(neural_network_level.input)):
	neural_network_level[i] = inputs[i]
```  
2.1. Iterate over each neuron in the outpu layer and initialize res to 0
```Python
for i in range(len(neural_network_level.output)):
	res = 0
...
```  
2.2   For each neuron in the output layer, calculate the weighted sum of inputs and multiply each input value by the corresponding weight and sum them up
```Python
...
	for j in range(len(neural_network_level.input)):
		res += neural_network_level.input[j] * neural_network_level.weights[j][i]
...
```
2.3 If the calculated sum plus the neuron's bias is greater than the threshold, set the output to 1, otherwise, set it to 0
```Python
...
	if res > neural_network_level.bias[i]: 
		neural_network_level.output[i] = 1
	else:
		neural_network_level.output[i] = 0
```
3. **return** `neural_network_level.output`

---
### NeuralNetwork.feed_forward  
  
This method is responsible for performing the forward propagation through the neural network. It takes two arguments: 
`inputs`- which is a list of input values
  `neural_network` -  which is an instance of the NeuralNetwork class.
  The function begins by calling the `feed_forward` function of the `NeuralNetworkLevel` class with the `inputs` and the first level of the neural network. The `output` from this call is then assigned to the `output` variable. Then, a loop is started that iterates over the remaining `levels` in the neural network. Inside the loop, the `feed_forward` function of the `NeuralNetworkLevel` class is called again, this time passing in the output from the previous level and the current level of the neural network. The resulting output is assigned to the output variable. If the `SHOW_SPEC_INFO` flag is set to `True`, the function prints the output of each level of the neural network to the console. 
  Finally, the function returns the `output` from the last level of the neural network, which represents the predictions made by the neural network based on the input values

**Input:** `inputs`- list of input values, `neural_network` - neural network
**Output:** output
1. Initialize the output variable `output` by applying the `NeuralNetworkLevel.feed_forward` operation to the input values using the first neural network level (`𝑛𝑒𝑢𝑟𝑎𝑙_𝑛𝑒𝑡𝑤𝑜𝑟𝑘.𝑙𝑒𝑣𝑒𝑙𝑠[0]`).
```Python
output = NeuralNetworkLevel.feed_forward( inputs, neural_network.levels[0])
```
  2. Iterate over the remaining layers of the neural network. For each layer, update the output by applying the `NeuralNetworkLevel.feed_forward` operation to the current output and the neural network level.
 ```Python
 for i in range(1, len(neural_network.levels)):
	 output = NeuralNetworkLevel.feed_forward( output, neural_network.levels[i])
 ```
 **return**  `output`
 
 ---
 Two more important functions used in the neruon network
 ---
### NeuralNetworkLevel.randomize_network  
  
This method is used to randomly set the `weights` and `bias` for each layer of the neural network. On input, it takes one argument, which is an object of class `NeuralNetworkLevel`. At first, the function looks through each input-output pair of weights to randomly assign a value from the interval `[-1,1]` using the function `random.randint(-100, 100)` and dividing the result by `100.0`. Then the function randomizes the bias value from the interval `[-1,1]` for each neuron in the layer and assigns the value to the "bias" array. The function does not return a value, as it directly modifies the object of the `NeuralNetworkLevel` class.

#### Input:

-   **𝑛𝑒𝑢𝑟𝑎𝑙_𝑛𝑒𝑡𝑤𝑜𝑟𝑘_𝑙𝑒𝑣𝑒𝑙:** The neural network level to be randomized.

1.  Iterate over each input neuron in the neural network level:
    
    -   Iterate over each output neuron in the neural network level.
    ```Python
    for i in range(len(neural_network_level.input)):
	    ...
    ```
2.  For each weight in the neural network level:
    
    -   Assign a random floating-point value between -1 and 1 using `float(random.randint(−100, 100))/100.0`.
    ```Python
	    ...
	    for j in range(len(neural_network_level.output)):
		    neural_network_level.wieghts[i][j] = float(random.randint(-100, 100)) / 100.0
	...
    ```
3.  Iterate over each output neuron in the neural network level:
    
    -   Assign a random floating-point value between -1 and 1 to the bias using `float(random.randint(−100, 100))/100.0`.
    ```Python
    ...
    for i in range(len(neural_network_level.bias)):
	    neural_network_level.biast[i] = float(random.randint(-100, 100)) / 100.0
    ```
  
### NeuralNetwork.mutate  
  
This method takes a `neural_network` as input, and randomly mutates the `bias` and `weights` of each level in the network based on a mutation probability (per). The mutation operation is performed on each level of the network separately. For each bias in a level, the function calls the `f_a` function defined in the `Sensors` class with the `bias` value, a random number between -1 and 1, and the mutation probability as inputs. The `f_a` function applies a mutation based on the mutation probability, which results in a new value for the bias. Similarly, for each weight in a level, the function applies the `f_a` function with the `weight` value, a random number between -1 and 1, and the mutation probability as inputs, resulting in a new value for the `weight`.
Overall, the `mutate` function randomizes the `weights` and `biases` of the neural network to introduce variation and encourage the network to adapt to different scenarios over time.

---
#### Sensors.f_a
**Input:** `a, b, c`- input values
**Output:** result - linear interpolation
```Python
return a + (b - a) * c
```
---
#### Input:
-   **𝑛𝑒𝑢𝑟𝑎𝑙_𝑛𝑒𝑡𝑤𝑜𝑟𝑘:** The neural network to be mutated.
-   **𝑝𝑒𝑟:** The mutation percentage, determining the extent of the random changes.

1.  Iterate over each neural network level (𝑙𝑒𝑣𝑒𝑙) in the neural network.
    ```Python
    for level in neural_neutwork.levels:
	    ...
    ```
2.  For each bias (𝑏𝑖𝑎𝑠) in the current neural network level:
    -   Apply a mutation to the bias using the function `Sensors.f_a`.
    -   `Sensors.f_a` takes the current bias value, a random value between -1 and 1, and the mutation percentage.
    ```Python
	    ...
	    for i in range(len(level.bias)):
		    level.bias[i] = Sensors.f_a(level.bias[i], random() * 2 - 1, per)
		...
    ```
3.  For each weight (𝑤𝑒𝑖𝑔ℎ𝑡𝑠) in the current neural network level:
    
    -   Iterate over each element in the weight matrix.
    -   Apply a mutation to each weight using the function `Sensors.f_a`.
    -   `Sensors.f_a` takes the current weight value, a random value between -1 and 1, and the mutation percentage.
    ```Python
	    ...
	    for i in range(lenght(level.weights)):
		    for j in range(lenght(level.weights[i])):
			    level.weights[i][j] = Sensors.f_a(level.weights[i][j], random() * 2 - 1, per)
    ```

## Genetic algorithm
The main goal of the algorithm is to evolve a population of cars that can successfully complete the race. The `fitness score` of each car is calculated based on the distance traveled, the number of overtakings, and the time elapsed without overtaking any other car. The genetic algorithm consists of several steps. First, a new generation of cars is created when all the cars in the current generation have crashed. The list of cars is then sorted in a non-increasing order based on their `fitness score`. Depending on the selected algorithm, a new generation of cars is created from the top-performing individuals. There are three different algorithms available in this implementation. The first one, called `Follow the King`, involves copying the neural network of the topperforming car and using it to create the next generation of cars. The top-performing car is referred to as the "King" in this algorithm, and its neural network is used as a template for the other cars in the generation. The genetic algorithm then applies a small mutation to each of the copied neural networks to introduce some variability in the population. The second algorithm, called `Top Cars to Parents`, involves selecting the top-performing cars from the current generation and using them as parents for the next generation. A certain percentage of the remaining cars in the current generation is then bred using the genetic composition of the selected parents to create new offspring. The third algorithm, called `King as a Parent`, is similar to the second one but with a slight modification. Instead of selecting the top-performing cars as parents, the algorithm uses the top-performing car as one of the parents for each offspring created. The other parent is chosen randomly from the top-performing individuals in the current generation. Once a new generation of cars is created using one of the three algorithms, the cars are reset to their starting position, and a new race begins. The cars are spawned on a road that contains randomly generated obstacles, and their performance is evaluated based on their `fitness score`. The process of creating new generations of cars continues until a car successfully completes the race or until the maximum number of generations is reached. Overall, the genetic algorithm is a powerful tool for evolving populations of cars that can successfully complete a racing game. The algorithm is flexible enough to allow for different selection strategies and can be adapted to a wide range of other applications.

---
### Follow The King
#### Input/Requirements:

-   **self:** Reference to the current object 

#### Algorithm Steps:

1.  **Initialize leader neural network:**
    
    -   Set `leader_nn` to the neural network of the first car in the list (`self.cars[0].get_nn()`).
    ```Python
    leader_nn = self.cars[0].get_nn()
    ...
    ```
2.  **Update neural networks of follower cars:**
    
    -   Iterate over the cars starting from the second one (index 1).
    -   Check if the neural network of the leader (`self.cars[0].get_nn()`) is not equal to the previously stored leader neural network (`leader_nn`).
    -   If not equal, update `leader_nn` to the neural network of the leader car.
    ```Python
    ...
    for i in range(1, len(self.cars)):
	    if self.cars[i].get_nn() != leader_nn:
		    leader_nn = self.cars[i].get_nn()
		...
    ```
3.  **Copy leader's neural network to followers:**
    
    -   For each follower car, deep copy the leader's neural network (`deepcopy(𝑙𝑒𝑎𝑑𝑒𝑟_𝑛𝑛)`).
    -   Mutate the copied neural network of each follower using the `NeuralNetwork.mutate` method with a mutation percentage of 0.1.
```Python
	...
	self.cars[i].neural_network = deepcopy(leader_nn)
	NeuralNetwork.mutate(self.cars[i].neural_network, 0.1)
```

---
### Top Cars To Parents
#### Input:

-   **self:** Reference to the current object

#### Algorithm Steps:

1.  **Calculate the number of top-performing cars to be selected as parents:**
    
    -   Set 𝑛1 to the product of `TOP_PERCENT`, the length of `self.cars`, and the division result of 100.
    -   This defines the number of top-performing cars that will be selected as parents.
```Python
n1 = TOP_PERCENT * len(self.cars) / 100
...
```
2.  **Select top cars as parents:**
    
    -   Extract the first 𝑛1 cars from the list (`self.cars[: 𝑛1]`) and assign them to 𝑐ℎ𝑖𝑙𝑑𝑟𝑒𝑛.
```Python
...
children = self.cars[:n1]
...
```
3.  **Calculate the number of offspring to be generated:**
    
    -   Set 𝑛2 to the product of (100 - TOP_PERCENT), the length of `self.cars`, and the division result of 100.
    -   This defines the number of offspring cars to be generated.
```Python
...
n2 = (100 - TOP_PERCENT) * len(self.cars) / 100
...
```
4.  **Generate offspring:**
    
    -   Iterate 𝑛2 times to generate offspring.
    -   Randomly select two parents from the top-performing cars.
    -   Create copies of the selected parents (`𝑝𝑎𝑟𝑒𝑛𝑡1` and `𝑝𝑎𝑟𝑒𝑛𝑡2`) using `copy`.
    -   Combine the genetic information of the parents using the method `parent1.compose_gens`.
    -   Append the resulting offspring to 𝑐ℎ𝑖𝑙𝑑𝑟𝑒𝑛.
```Python
...
for i in range(n2):
	r = randint(0, n1 - 1)
	parent1 = copy(self.cars[r])
	r = randint(0, n1 - 1)
	parent2 = copy(self.cars[r])
	offspring = parent1.compose_gens(parent2)
	children.append(offspring)
```
5.  **Replace current cars with offspring:**
    
    -   Update `self.cars` with the newly generated offspring (`self.cars ← children`).
```Python
self.cars = children
```

---
### King As Parent
#### Input:

-   **self:** Reference to the current object.

#### Algorithm Steps:

1.  **Calculate the number of top-performing cars to be selected as parents:**
    
    -   Set 𝑛1 to the product of `TOP_PERCENT`, the length of `self.cars`, and the division result of 100.
```Python
n1 = TOP_PERCENT * len(self.cars) / 100
...
```
2.  **Select top cars as parents:**
    
    -   Extract the first 𝑛1 cars from the list (`self.cars[: 𝑛1]`) and assign them to 𝑐ℎ𝑖𝑙𝑑𝑟𝑒𝑛.
```Python
...
children = self.cars[:n1]
...
```
3.  **Calculate the number of offspring to be generated:**
    
    -   Set 𝑛2 to the product of (100 - TOP_PERCENT), the length of `self.cars`, and the division result of 100.
```Python
...
n2 = (100 - TOP_PERCENT) * len(self.cars) / 100
...
```
4.  **Generate offspring:**
    
    -   Iterate 𝑛2 times to generate offspring.
    -   Create a copy of the first car in the list (`𝑝𝑎𝑟𝑒𝑛𝑡1 ← copy(𝑠𝑒𝑙𝑓.𝑐𝑎𝑟𝑠[0])`).
    -   Randomly select a second parent from the top-performing cars (`𝑟 ← randint(0, 𝑛1 − 1)`).
    -   Create a copy of the selected parent (`𝑝𝑎𝑟𝑒𝑛𝑡2 ← copy(𝑠𝑒𝑙𝑓.𝑐𝑎𝑟𝑠[𝑟])`).
    -   Combine the genetic information of the parents using the method `parent1.compose_gens`.
    -   Append the resulting offspring to 𝑐ℎ𝑖𝑙𝑑𝑟𝑒𝑛.
```Python
...
for i in range(n2):
	parent1 = copy(self.cars[0])
	r = randint(0, n1 - 1)
	parent2 = copy(self.cars[r])
	offspring = parent1.compose_gens(parent2)
	children.append(offspring)
...
```
5.  **Replace current cars with offspring:**
    
    -   Update `self.cars` with the newly generated offspring (`self.cars ← children`).
```Python
self.cars = children
```

---
# Results
From my observations, artificial intelligence learns fastest using the `Top Family As Parents` method, because this method provides the largest cross-section of genes. The `King As a Parent` method is added only as a curiosity and is based entirely on zero-generation randomness; if a car is "born" with a good neural network, it will pass it on to everyone, but note that this works both ways - by creating a faulty network, other cars will also inherit it. The `King As a Parent` method works almost as well as `Top Family As Parents`, but doesn’t give as good results. I’ve been able to get very good results with cars using the `Top Family As Parents` method as early as the 26th generation, but I note that the design relies on a lot of randomness, and cars like to choose a safe driving style, despite the large penalty. The `Top Family As Parents` method is based on selecting the best neural networks from the previous generation of cars, which are then used as parents to create the next generation. This makes it possible to learn quickly and pass on good genes to achieve faster results. The `King As a Parent` method is based on a completely different approach, where randomness plays a bigger role. In this method, each car has a chance to become a "king" (King) with the best neural network, but this approach can lead to different results and faulty neural networks. It is important to understand that each method has its own advantages and disadvantages, and the choice of one depends on the specific application and performance expectations. Therefore, it is important to experiment and adapt the method to individual needs and goals. However, based on the observations, the `Top Family As Parents` method seems to be more effective in machine learning for the car game.

---
## Average fitness score in each algorithm 
Fitness score was calculated this way:
```Python
fitness_score = -car.y * 0.01 + overtaken_obstacles
if alive:
	fitness_score -= 10 
```
| Generation | Follow The King | Top Family As Parents | King As Parent | Mix Genre | 
|--|--|--|--|--|
| 1|12.98559296174006  | -7.808195494281016 |-6.924033910972822  |10.379026294401912  |
| 3| -3.3052884221014924 | -4.14103949994384 |-2.97331677029527  | 11.5580597163735 |
| 5|5.15214906222836  |-3.559338431188315  |-11.40538175404779  | 21.993954491650882 |
| 7| 6.246051073366174 | 1.284096953323152 | -2.877347691507002|   7.226481800294589|
|10|-8.694551304109911  | 4.743076811319067 | 26.678059567683494| 12.623682066421734 |
|13|  -9.440997341453917 |18.137469461837625  |6.879047690467651  | 24.399372053295775 |
|15| -3.082444493759183 |30.98968531352831  |15.108799506261816  | 12.492459327392492 |

