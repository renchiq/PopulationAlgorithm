from random import randint, random
import random
import numpy as np


class BatAlgorithm():
    def __init__(self,
                 d_dimension,
                 population_size,
                 iterations,
                 a_loudness,
                 r_pulse,
                 f_min,
                 f_max,
                 lower_bound,
                 upper_bound,
                 function):
        self.d_dimension = d_dimension  # dimension
        self.population_size = population_size  # population size
        self.iterations = iterations  # generations
        self.a_loudness = a_loudness  # loudness
        self.r_pulse = r_pulse  # pulse rate
        self.f_min = f_min  # frequency min
        self.f_max = f_max  # frequency max
        self.lower_bound = lower_bound  # lower bound
        self.upper_bound = upper_bound  # upper bound

        self.f_min = 0.0  # minimum fitness

        self.lower_bound_dimension = [0] * self.d_dimension  # lower bound
        self.upper_bound_dimension = [0] * self.d_dimension  # upper bound
        self.frequency_population = [0] * self.population_size  # frequency

        self.velocity = [[0 for i in range(self.d_dimension)] for j in range(self.population_size)]  # velocity
        self.Sol = [[0 for i in range(self.d_dimension)] for j in range(self.population_size)]  # population of solutions
        self.fitness_values = [0] * self.population_size  # fitness
        self.best_values = [0] * self.d_dimension  # best solution
        self.fitness_function = function

    def best_bat(self):
        j = 0
        for i in range(self.population_size):
            if self.fitness_values[i] < self.fitness_values[j]:
                j = i
        for i in range(self.d_dimension):
            self.best_values[i] = self.Sol[j][i]
        self.f_min = self.fitness_values[j]

    def init_bat(self):
        for i in range(self.d_dimension):
            self.lower_bound_dimension[i] = self.lower_bound
            self.upper_bound_dimension[i] = self.upper_bound

        for i in range(self.population_size):
            self.frequency_population[i] = 0
            for j in range(self.d_dimension):
                rnd = np.random.uniform(0, 1)
                self.velocity[i][j] = 0.0
                self.Sol[i][j] = self.lower_bound_dimension[j] + (self.upper_bound_dimension[j] - self.lower_bound_dimension[j]) * rnd
            self.fitness_values[i] = self.fitness_function(self.d_dimension, self.Sol[i])
        self.best_bat()

    def simplebounds(self, val, lower, upper):
        if val < lower:
            val = lower
        if val > upper:
            val = upper
        return val

    def move_bat(self):
        S = [[0.0 for i in range(self.d_dimension)] for j in range(self.population_size)]

        self.init_bat()

        for t in range(self.iterations):
            for i in range(self.population_size):
                rnd = np.random.uniform(0, 1)
                self.frequency_population[i] = self.f_min + (self.f_max - self.f_min) * rnd
                for j in range(self.d_dimension):
                    self.velocity[i][j] = self.velocity[i][j] + (self.Sol[i][j] -
                                                                 self.best_values[j]) * self.frequency_population[i]
                    S[i][j] = self.Sol[i][j] + self.velocity[i][j]

                    S[i][j] = self.simplebounds(S[i][j], self.lower_bound_dimension[j],
                                                self.upper_bound_dimension[j])

                rnd = np.random.random_sample()

                if rnd > self.r_pulse:
                    for j in range(self.d_dimension):
                        S[i][j] = self.best_values[j] + 0.001 * random.gauss(0, 1)
                        S[i][j] = self.simplebounds(S[i][j], self.lower_bound_dimension[j],
                                                    self.upper_bound_dimension[j])

                f_new = self.fitness_function(self.d_dimension, S[i])

                rnd = np.random.random_sample()

                if (f_new <= self.fitness_values[i]) and (rnd < self.a_loudness):
                    for j in range(self.d_dimension):
                        self.Sol[i][j] = S[i][j]
                    self.fitness_values[i] = f_new

                if f_new <= self.f_min:
                    for j in range(self.d_dimension):
                        self.best_values[j] = S[i][j]
                    self.f_min = f_new

        print(self.f_min)
        print(self.best_values)


class Bat:
    def __init__(self):
        self.f_frequency = random() * 10
        self.x_position = random() * 15
        self.v_velocity = random() * 15
        self.a_loudness = random()
        self.r_pulse = random()

    def __str__(self):
        return f'f Frequency = {self.f_frequency}\n' \
               f'x Position = {self.x_position}\n' \
               f'v Velocity = {self.v_velocity}\n' \
               f'a Loudness = {self.a_loudness}\n' \
               f'r Pulse = {self.r_pulse}'


def Fun(D, sol):
    val = float(0)
    for i in range(D):
        val = val + sol[i] * sol[i]
    return val


algorithm = BatAlgorithm(
                 d_dimension=10,
                 population_size=40,
                 iterations=1000,
                 a_loudness=0.5,
                 r_pulse=0.5,
                 f_min=0,
                 f_max=2,
                 lower_bound=-10,
                 upper_bound=10,
                 function=Fun)
algorithm.move_bat()
