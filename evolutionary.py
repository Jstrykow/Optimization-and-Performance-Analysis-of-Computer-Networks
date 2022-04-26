# this file represents implemenation of elvolutionary algorythm
# it is heuristic : resionable solution in resionable time

from network.Net import Net
import random

"""
Program powinien umożliwiać:
• określenie liczności populacji startowej,
• określenie prawdopodobieństwa wystąpienia krzyżowania i mutacji,
• wybór kryterium stopu (wymagane są: zadany czas, zadana liczba generacji, zadana liczba 
mutacji, brak poprawy najlepszego znanego rozwiązania obserwowany w kolejnych N 
generacjach),
• zapis trajektorii procesu optymalizacji rozumianej jako sekwencja wartości najlepszych rozwiązań (chromosomów) w kolejnych generacjach,
• wskazanie ziarna dla generatora liczb losowych.
"""


class EvolutionaryAlgorithm:
    def __init__(self, seed: int, net: Net, number_of_chromosomes: int, max_generations: int, max_time: int, max_generation: int, max_mutation: int, max_no_progress_generation: int, procent_of_best_chromosomes: int, crossover_probability: float, mutation_probability: float):
        random.seed(seed)

        self.net = net
        self.number_of_chromosomes = number_of_chromosomes
        self.max_generations = max_generations
        self.max_time = max_time
        self.max_generation = max_generation
        self.max_mutation = max_mutation
        self.max_no_progress_generation = max_no_progress_generation
        self.procent_of_best_chromosomes = procent_of_best_chromosomes
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability

        self.generations = 0
        self.no_progress = 0
        self.mutation = 0

    def inicjialization_function():
        pass
        

    def mutate(seed = None):
        # there is adding radom element in proces of elvolution, it is to move from local optimum. 
        # seed is parametr of function for making possible replication of function
        pass

    def crossover():
        # exchange genes from two parents, and produce two offspring, better fitting offspring is taking
        pass

    def fitness():
        # funtion checking is solution good solution
        pass

    
    def best_trajectory():
        pass
