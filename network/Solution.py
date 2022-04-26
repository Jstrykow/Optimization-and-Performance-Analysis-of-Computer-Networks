# class for solutions
from typing import List


class Link_load():
    def __init__(self, link_id: int, number_of_signals: int, number_of_fiber: int ):
        self.link_id = link_id
        self.number_of_signals = number_of_signals
        self.number_of_fibers = number_of_fiber

    def str(self):
        return f"'\n{self.link_id} {self.number_of_signals} {self.number_of_fibers}"


class Demand_flow():
    def __init__(self, demand_id: int, number_of_paths: int):
        self.demand_id = demand_id
        self.number_of_paths = number_of_paths
        self.path_flows = []

    def __str__(self):
        msg = ''
        msg += f"{self.demand_id} {self.number_of_paths}\n"
        msg += '\n'
        for path_flow in self.path_flows:
            msg += f"\n{str(path_flow)}"
        return msg

class Path_flow():
    def __init__(self, path_id: int, lefth: int):
        self.path_id = path_id
        self.lefth = lefth

    def __str__(self):
        return f"{self.path_id} {self.lefth}"


class Solution():
    def __init__(self, number_of_links: int, link_load_list: List[Link_load], number_of_demands: int, demand_flow_list: List[Demand_flow]):
        # <link part>
        self.number_of_links = number_of_links
        self.link_load_list = link_load_list
        # <demand part>
        self.number_of_demand = number_of_demands
        self.demand_flow_list = demand_flow_list

    def __str__(self):
        msg = ""
        msg += self.number_of_links + '\n'
        msg += '\n'
        # <link load part>
        for link_load in self.link_load_list:
            msg += str(link_load)
        # <demand part>
        #
        #NIE  TESTOWANE
        #
        #
        for demand in self.demand_flow_list
            msg += str(demand)