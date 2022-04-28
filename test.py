from evolutionary import EvolutionaryAlgorithm
from input_data_parser import Input_Reader


def main() -> object:
    ir = Input_Reader()
    net = ir.read_links("data/net4.txt")
    ea = EvolutionaryAlgorithm(
        prb="DDAP",
        net=net,
        seed=1,
        number_of_chromosomes=30,
        max_no_progress_generation=20,
        max_generations=100,
        max_mutation=1000000,
        max_time=300,
        procent_of_best_chromosomes=0.7,
        crossover_probability=0.6,
        mutation_probability=0.03
    )
    solution = ea.calculate()
    print(solution)


if __name__ == "__main__":
    main()
