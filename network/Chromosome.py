# chromosome is a feasible solution, it represents sequence of genes, gemes represents internal structure of a solution
import math
from network.Net import Net
from network.Path import Path


class Chromosome():
    def __init__(self, allocation_pattern: dict):
        self.allocation_pattern = allocation_pattern
        self.link_size = []
        self.link_loads = []
        self.number_of_genes = 0

    def link_load_calculation(self):
        # link load l(e,x) 
        pass

    
    def calculate(self, net: Net):
        links = net.links
        link_values = [0] * len(net.links)
        paths = net.get_all_demands_paths()
        for link_id, link in enumerate(links):
            volume_sum = 0
            for path in paths:
                if link_id + 1 in path.links:
                    volume = self.allocation_pattern.get((path.demand_id, path.path_id))
                    volume_sum += volume
            link_values[link_id] = volume_sum  # DAP
            # math.ceil(volume_sum / link.modeule) DDAP


                


