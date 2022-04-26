# this file contain brute force algorithm 
from network.Net import Net
from input_data_parser import Input_Reader
# solution x - two dimensional array of path-flows
from network.Solution import Demand_flow, Path_flow





class BruteForce():
    def __init__(self, net: Net):
        self.net = net

    def solve(self):
       
        possible_solution = self.get_all_possible_flows()
        print(possible_solution)
        self.prepare_solution()

    def get_all_possible_flows(self):
        possible_flows = []
        for demand in self.net.demands:

            all_flows_for_demand = self.rec(demand.demand_id, 1, demand.number_of_paths, demand.demand_volume)
            print(all_flows_for_demand)
            
            for demand_flow in all_flows_for_demand:
                demand_flow.path_flows.reverse()
            
            possible_flows.append(all_flows_for_demand)
            
        return possible_flows

    def rec(self, curd: int, curp: int, len_paths: int, lefth: int):  # current demand, current path, lefth, x
        all_possible_combinations = []

        if curp == len_paths:
            demand_flow = Demand_flow(curd, len_paths)
            path_flow = Path_flow(curp, lefth)
            demand_flow.path_flows.append(path_flow)
            all_possible_combinations.append(demand_flow)
        else:
            for parth in range(lefth):
                one_combinataion = self.rec(curd, curp + 1, len_paths, lefth - parth)
                for demand_flow in one_combinataion:
                    path_flow = Path_flow(curp, parth)
                    demand_flow.path_flows.append(path_flow)
                    
                all_possible_combinations += one_combinataion

        return all_possible_combinations

    def prepare_solution(self):
        pass


ir = Input_Reader()
net = ir.read_links("data/net4.txt")

brute = BruteForce(net)
brute.solve()