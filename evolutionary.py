# this file represents implemenation of elvolutionary algorythm
# it is heuristic : resionable solution in resionable time
import copy
import random
from itertools import product
from time import time
from typing import List

from network import Demand
from network.Chromosome import Chromosome
from network.Net import Net

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
    def __init__(self, seed: int, net: Net, prb: str, number_of_chromosomes: int, max_generations: int, max_time: int, max_generation: int, max_mutation: int, max_no_progress_generation: int, procent_of_best_chromosomes: int, crossover_probability: float, mutation_probability: float):
        random.seed(seed)

        self.net = net
        self.prb = prb
        self.number_of_chromosomes = number_of_chromosomes
        self.max_generations = max_generations
        self.max_time = max_time
        self.max_generation = max_generation
        self.max_mutation = max_mutation
        self.max_no_progress_generation = max_no_progress_generation
        self.procent_of_best_chromosomes = procent_of_best_chromosomes
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability

        self.initial_time = None
        self.generations = 0
        self.no_progress = 0
        self.results_history =[]
        self.mutation = 0

    def calculate(self) -> Chromosome:
        self.initial_time = time()
        population = self.get_init_population()
        solution = Chromosome({})

        while not self.ending():
            self.generations += 1
            best_chromosome = Chromosome({})

            # calculate cost function for current generation
            for chromosome in population:
                chromosome.calculate(self.net, self.prb)
                if chromosome.calculate_z(self.net, self.prb) < best_chromosome.z:
                    best_chromosome = copy.deepcopy(chromosome)

            self.results_history.append(best_chromosome)

            if best_chromosome.z < solution.z:
                solution = copy.deepcopy(best_chromosome)
                self.no_progress = 0
            else:
                self.no_progress += 1

            population = self.pick_fittest(population)

            # crossover
            crossed_population = []
            while len(population) > 1:
                parents = random.sample(population, 2)
                population.remove(parents[0])
                population.remove(parents[1])
                crossed_population += (self.crossover(parents) if self.crossover_happened() else parents)

            population += crossed_population

            # mutation
            for chromosome in population:
                if self.mutation_happened():  # chromosome mutation
                    for i in range(chromosome.number_of_genes):
                        if self.mutation_happened():  # gene mutation
                            chromosome.mutate_gene(i + 1)
                            self.mutation += 1

        for results in self.results_history:
            results.calculate_links(self.net)

        solution.calculate_links(self.net)

        return solution

    def mutate(seed = None):
        # there is adding radom element in proces of elvolution, it is to move from local optimum. 
        # seed is parametr of function for making possible replication of function
        pass

    def crossover(self, parents):
        father = parents[0]
        mother = parents[1]
        brother = Chromosome({})
        sister = Chromosome({})

        number_of_genes = father.number_of_genes

        for gene_number in range(number_of_genes):
            if random.random() > 0.5:
                brother.add_gene(father.get_gene(gene_number + 1))
                sister.add_gene(mother.get_gene(gene_number + 1))
            else:
                brother.add_gene(mother.get_gene(gene_number + 1))
                sister.add_gene(father.get_gene(gene_number + 1))

        return [brother, sister]

    def pick_fittest(self, population: List):
        population.sort(key=lambda x: x.z)
        best_chromosomes = population[:self.number_of_best_chromosomes]
        padding = [copy.deepcopy(best_chromosomes[i]) for i in range(self.population_padding)]
        return best_chromosomes + padding

    def crossover_happened(self) -> bool:
        return random.random() < self.crossover_probability

    def mutation_happened(self) -> bool:
        return random.random() < self.mutation_probability

    def get_init_population(self) -> List:
        all_genes_combinations = [self.get_all_possible_chromosomes_with_one_gene(demand) for demand in
                                  self.net.demands]
        chromosomes = []

        for i in range(self.number_of_chromosomes):
            chromosome = Chromosome({})
            for gene_combination in all_genes_combinations:
                gene = random.choice(gene_combination).allocation_pattern
                chromosome.add_gene(gene)
            chromosome.calculate_links_for_problem(self.net, problem=self.problem)
            chromosomes.append(chromosome)

        random.shuffle(chromosomes)
        return chromosomes

    def get_all_possible_chromosomes_with_one_gene(self, demand: Demand) -> List[Chromosome]:
        volume_split = range(demand.volume + 1)
        volume_split_for_each_path = [volume_split for _ in range(demand.get_number_of_paths())]

        volume_split_combinations = [combination for combination in product(*volume_split_for_each_path) if
                                     sum(combination) == demand.volume]

        solutions = [Chromosome(self.build_gene(combination, demand)) for combination in volume_split_combinations]
        return solutions

    def build_gene(combination: tuple, demand: Demand):
        allocation_vector = {}
        for demand_path in demand.demand_paths:
            path_id = demand_path.path_id
            flow_xdp = (demand.id, path_id)
            allocation_vector[flow_xdp] = combination[path_id - 1]
        return allocation_vector

    def ending(self) -> bool:
        time_exceeded = time() - self.start_time >= self.max_time
        if time_exceeded:
            print("Time limit reached.")
            return True

        generations_exceeded = self.generation >= self.max_generations
        if generations_exceeded:
            print("Generations limit reached.")
            return True

        mutations_exceeded = self.mutations >= self.max_mutations
        if mutations_exceeded:
            print("Mutations limit reached.")
            return True

        no_progress = self.no_progress >= self.max_no_progress_generations
        if no_progress:
            print("Iteration without progress limit reached.")
            return True

        return False
