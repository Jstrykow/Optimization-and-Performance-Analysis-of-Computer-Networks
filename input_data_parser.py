from network.Link import Link
from network.Path import Path
from network.Demand import Demand

class Input_Reader:
    def read_links(self, name_of_file):
        with open(name_of_file, "r") as file:
            number_of_links = int(file.readline())
            for i in range(number_of_links):
                parameters = file.readline().strip().split(" ")
                link_id = i + 1
                start_node_id = parameters[0]
                end_node_id = parameters[1]
                number_of_fibers = parameters[2]
                fiber_cost = parameters[3]
                number_of_lambdas_in_fiber = parameters[4]
                link = Link(link_id, start_node_id, end_node_id, number_of_fibers, fiber_cost, number_of_lambdas_in_fiber)
                # adding new nodes, checking node is in array
                # link = Link (parameters)
                print(link)
            minus_one = int(file.readline())
            if(minus_one != -1):
                print("Error during reading links")
            file.readline()
            number_of_demands = int(file.readline())
            file.readline()
            for i in range(number_of_demands):
                # path_list
                paths_list = []
                parameters = file.readline().strip().split()
                start_node_id = parameters[0]
                end_node_id = parameters[1]
                demand_volume = parameters[2]
                number_of_paths = int(file.readline())
                for j in range(number_of_paths):
                    path_parameters = file.readline().strip().split()
                    path_id = path_parameters[0]
                    links_list = path_parameters[1:]
                    path = Path(path_id, links_list)
                    paths_list.append(path)
                demand = Demand(start_node=start_node_id, end_node=end_node_id, demand_volume=demand_volume, paths_list=paths_list)
                print(demand)
                file.readline()


ir = Input_Reader()
ir.read_links("data/net4.txt")
