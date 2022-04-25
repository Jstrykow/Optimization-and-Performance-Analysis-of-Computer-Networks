import itertools 
from Link import Link
from Demand import Demand


# class for take all links, demands, nodes etc
class Net:
    def __init__(self):
        self.link = []
        self.demands = []

    def get_link(self, link_id) -> Link:
        return self.links[link_id - 1]
    
    def get_demand(self, demand_id) -> Demand:
        return self.demands[demand_id - 1]
    
    def get_all_demands_paths(self):
        demand_paths = [demand.demand_paths for demand in self.demands]
        return list(itertools.chain.from_iterable(demand_paths))