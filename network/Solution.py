# class for solutions
import math
from traceback import print_tb

from typing import List
from network.Demand import Demand
from network.Link import Link

class Link_load():
    def __init__(self, link_id: int, volume: int, number_of_fiber: int):
        self.link_id = link_id
        self.volume = volume # volume
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

class Demand_path_flow():
    def __init__(self, path_id: int, lefth: int):
        self.path_id = path_id
        self.volume = lefth

    def __str__(self):
        return f"{self.path_id} {self.volume}"


class Solution():
    def __init__(self, solution_id: int, number_of_links: int,  number_of_demands: int): # demand_flow_list: List[Demand_flow], link_load_list: List[Link_load],):
        # <link part>
        self.solution_id = solution_id
        self.number_of_links = number_of_links
        self.link_load_list = []  # link_load_list
        # <demand part>
        self.number_of_demand = number_of_demands
        self.demand_flow_list = []  # demand_flow_list

        # bruteforce alg
        self.objactive_DAP = None
        self.objactive_DDAP = None
        # evolutionary algorthm
        self.objactive = None
    
    def calulate_load_link(self, demands: List[Demand], links: List[Link]):
        self.link_load_list.clear()

        # new empty load list
        for load_id in range(self.number_of_links):
            link_load = Link_load(load_id + 1, 0, 0)
            self.link_load_list.append(link_load)
        
        for (demand_id, demand_flow) in enumerate(self.demand_flow_list):
            for (path_id, path_flow) in enumerate(demand_flow.path_flows):
                for link_id in range(len(demands[demand_id].paths_list[path_id].links_list)):
                    self.link_load_list[link_id - 1].volume += int(path_flow.volume)
                    print(self.link_load_list[link_id - 1].volume)
        # for (link_id, link_load) in enumerate(self.link_load_list):
        #    link_load.number_of_fibers = math.ceil(link_load.number_of_signals / links[link_id].number_of_lambdas_in_fiber)

    def calculate_objactive_DAP(self):
        objective_value = 0
        for link_load in enumerate(self.link_load_list):
            obj = link_load.number_of_signals
            if obj > objective_value:
                objective_value = obj
        self.objactive_DAP = objective_value
        self.objactive = objective_value
        return self.objactive_DAP

    def calculate_objactive_DDAP(self, links: List[Link]):
        objective_value = 0
        for (link_id, link_load) in enumerate(self.link_load_list):
            link_cost = link_load.number_of_fibers * links[link_id].fiber_cost
            objective_value += link_cost
        self.objectiveDDAP = objective_value
        self.objective = objective_value
        return self.objectiveDDAP
    
    def __eq__(self, other):
        return self.objective == other.objective

    def __lt__(self, other):
        return self.objactive < other.objective
    
    def __gt__(self, other):
        return self.objactive > other.objective
    
    def __str__(self):
        msg = ""
        msg += str(self.number_of_links) + '\n'
        msg += '\n'
        # <link load part>
        for link_load in self.link_load_list:
            msg += str(link_load)
        # <demand part>
        #
        #NIE  TESTOWANE
        #
        #
        for demand in self.demand_flow_list:
            msg += str(demand)
        return msg