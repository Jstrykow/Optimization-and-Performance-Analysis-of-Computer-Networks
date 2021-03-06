import itertools 
from network.Link import Link
from network.Demand import Demand


# class for take all links, demands, nodes etc
class Net:
    def __init__(self):
        self.links = []
        self.demands = []

    def get_link(self, link_id) -> Link:
        return self.links[link_id - 1]

    def get_demand(self, demand_id) -> Demand:
        return self.demands[demand_id - 1]

    def get_all_demands_paths(self):
        demand_paths = [demand.demand_paths for demand in self.demands]
        return list(itertools.chain.from_iterable(demand_paths))

    def __str__(self):
        resp = ""
        for link in self.links:
            resp += str(link) + '\n'
        for demand in self.demands:
            resp += str(demand) + '\n'
        return resp

    def get_number_of_links(self) -> int:
        return len(self.links)

    def get_number_of_demands(self) -> int:
        return len(self.demands)

