# this file contain brute force algorithm 
from network.Net import Net
from input_data_parser import Input_Reader
# solution x - two dimensional array of path-flows
from network.Solution import Demand_flow, Demand_path_flow, Solution
import itertools


class BruteForce():
    def __init__(self, net: Net, max_top_solution=15):
        self.net = net
        self.all_solutions = []
        self.best_solution_DAP = None
        self.best_solution_DDAP = None
        self.max_top_solution = max_top_solution
        self.lastTopSolutionsDAP = []  # lists of top solutions
        self.lastTopSolutionsDDAP = []

    def solve(self):
        possible_solution = self.get_all_possible_flows()
        # print(possible_solution)
        self.choose_solution(possible_solution)
        

    def get_all_possible_flows(self):
        possible_flows = []
        for demand in self.net.demands:

            all_flows_for_demand = self.rec(demand.demand_id, 1, demand.get_number_of_paths(), demand.demand_volume)
            
            for demand_flow in all_flows_for_demand:
                demand_flow.path_flows.reverse()
            
            possible_flows.append(all_flows_for_demand)
            
        return possible_flows

    def rec(self, curd: int, curp: int, len_paths: int, lefth: int):  # current demand, current path, lefth, x
        all_possible_combinations = []

        if curp == len_paths:
            demand_flow = Demand_flow(curd, len_paths)
            path_flow = Demand_path_flow(curp, lefth)
            demand_flow.path_flows.append(path_flow)
            all_possible_combinations.append(demand_flow)
        else:
            for parth in range(lefth):
                one_combinataion = self.rec(curd, curp + 1, len_paths, lefth - parth)
                for demand_flow in one_combinataion:
                    path_flow = Demand_path_flow(curp, parth)
                    demand_flow.path_flows.append(path_flow)
                all_possible_combinations += one_combinataion

        return all_possible_combinations

    def choose_solution(self, possible_flows):
        solution_id = 0
        # print(self.net.get_number_of_links())
        for combinations_of_demands_flows in itertools.product(*possible_flows):
            solution_id += 1
            solution = Solution(solution_id=solution_id,
                                           number_of_links=self.net.get_number_of_links(),
                                           number_of_demands=self.net.get_number_of_demands())
            solution.demand_flow_list = list(combinations_of_demands_flows)
            solution.calulate_load_link(self.net.demands, self.net.links)
        
            solution.calculate_objactive_DAP()
            if len(self.lastTopSolutionsDAP) < self.max_top_solution or solution.objactive_DAP < self.lastTopSolutionsDAP[-1].objactive_DAP:
                self.lastTopSolutionsDAP.append(solution)
                self.lastTopSolutionsDAP.sort(key=lambda x: x.objactive_DAP)
                
                if len(self.lastTopSolutionsDAP) > self.max_top_solution:
                    self.lastTopSolutionsDAP.pop()

        
            solution.calculate_objactive_DDAP(self.net.links)
            if len(self.lastTopSolutionsDDAP) < self.max_top_solution or solution.objactive_DDAP < self.lastTopSolutionsDDAP[-1].objactive_DDAP:
                self.lastTopSolutionsDDAP.append(solution)
                self.lastTopSolutionsDDAP.sort(key=lambda x: x.objactive_DDAP)
                if len(self.lastTopSolutionsDDAP) > self.max_top_solution:
                    self.lastTopSolutionsDDAP.pop()

            self.all_solutions.append(solution)
        self.best_solution_DAP = self.lastTopSolutionsDAP[0]
        self.best_solution_DDAP = self.lastTopSolutionsDDAP[0]
        

ir = Input_Reader()
net = ir.read_links("data/net4.txt")

brute = BruteForce(net)
brute.solve()   