# chromosome is a feasible solution, it represents sequence of genes, gemes represents internal structure of a solution

from network.Net import Net
from network.Path import Path
import math
import random
from pprint import pformat


class Chromosome:
    def __init__(self, allocation_pattern: dict):
        self.allocation_pattern = allocation_pattern
        self.link_size = []
        self.link_loads = []
        self.number_of_genes = 0
        self.z = float('inf')

    def calculate(self, net: Net, prb: str):
        links = net.links
        link_values = [0] * len(net.links)
        paths = net.get_all_demands_paths()
        for link_id, link in enumerate(links):
            volume_sum = 0
            for path in paths:
                if link_id + 1 in path.links:
                    volume = self.allocation_pattern.get((path.demand_id, path.path_id))
                    volume_sum += volume
            link_values[link_id] = math.ceil(volume_sum / link.module) if prb == "DDAP" else volume_sum
        if prb == "DDAP":
            self.link_size = link_values
        else:
            self.link_loads = link_values

    def add_flow(self, mapping: dict):
        self.allocation_pattern = {**self.allocation_pattern, **mapping}

    def add_gene(self, gene: dict):
        self.add_flow(gene)
        self.number_of_genes += 1

    def get_gene(self, demandID):
        return {key: value for key, value in self.allocation_pattern.items() if key[0] == demandID}

    def mutate(self, gene_number):
        gene = self.get_gene(gene_number)
        if len(gene) > 1:
            flows = random.sample(list(gene), 2)
            if self.allocation_pattern[flows[0]] > 0:
                self.allocation_pattern[flows[0]] -= 1
                self.allocation_pattern[flows[1]] += 1

    def calculate_z(self, net: Net, prob: str):
        if prob == "DDAP":
            z = 0
            for link_id, link_size in enumerate(self.link_size):
                z += net.links[link_id].cost * link_size
            self.z = z
        else:
            z = float('-inf')
            for i, link_load in enumerate(self.link_loads):
                _z = link_load - net.links[i].number_of_modules * net.links[i].module
                if _z > z:
                    z = _z
                self.z = z
        return z

    def calculate_links(self, net: Net):
        self.calculate(net, "DDAP")
        self.calculate(net, "DAP")

    def __str__(self):
        text = "Flows for (demand, path):\n" + pformat(self.allocation_pattern)

        if self.link_size:
            text += f"\nLink sizes: {self.link_size}"
        if self.link_loads:
            text += f"\nLink loads: {self.link_loads}"
        text += f"\nz = {self.z}"
        return text




