# chromosome is a feasible solution, it represents sequence of genes, gemes represents internal structure of a solution

INITIAL_COST = float('inf')

class Chromesome(object):
    def __init__(self, allocation_pattern: dict):
        self.allocation_pattern = allocation_pattern
        self.link_size = []
        self.link_loads = []
        self.number_of_genes = 0
        self.z = INITIAL_COST
    
    