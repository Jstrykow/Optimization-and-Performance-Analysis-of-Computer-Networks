# this file contain brute force algorithm 
from network.Net import Net
from input_data_parser import Input_Reader
# solution x - two dimensional array of path-flows

class Demand_flow():
    def __init__(self, demand_id: int, number_of_paths: int):
        self.demand_id = id
        self.number_of_paths = number_of_paths
        self.path_flows = []


class Path_flow():
    def __init__(self, path_id: int, lefth: int):
        self.path_id = path_id
        self.lefth = lefth


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
            print(f"[{demand.demand_id}, 1, {demand.number_of_paths}, {demand.demand_volume}]")
            """
            [1, 1, 3, 3]
            [2, 1, 3, 4]
            [3, 1, 2, 5]
            [4, 1, 3, 2]
            [5, 1, 3, 3]
            [6, 1, 3, 4]
            """

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