from network.Link import Link
from network.Path import Path
from network.Demand import Demand
from network.Net import Net


class Input_Reader:
    def read_links(self, name_of_file):
        links = []
        demands = []
        with open(name_of_file, "r") as file:
            number_of_links = int(file.readline())
            for i in range(number_of_links):
                parameters = file.readline().strip().split(" ")
                link_id = i + 1
                start_node_id = int(parameters[0])
                end_node_id = int(parameters[1])
                number_of_fibers = int(parameters[2])
                fiber_cost = int(parameters[3])
                number_of_lambdas_in_fiber = int(parameters[4])
                link = Link(link_id, start_node_id, end_node_id, number_of_fibers, fiber_cost, number_of_lambdas_in_fiber)
                # adding new nodes, checking node is in array
                # link = Link (parameters)
                links.append(link)
                # print(link)
            minus_one = int(file.readline())
            if(minus_one != -1):
                print("Error during reading links")
            file.readline()
            number_of_demands = int(file.readline())
            file.readline()
            for i in range(number_of_demands):
                # path_list
                paths_list = []
                demand_id = i + 1
                parameters = file.readline().strip().split()
                start_node_id = int(parameters[0])
                end_node_id = int(parameters[1])
                demand_volume = int(parameters[2])
                number_of_paths = int(file.readline())
                for j in range(number_of_paths):
                    path_parameters = file.readline().strip().split()
                    path_id = int(path_parameters[0])
                    links_list = []

                    # print(path_parameters[1:])
                    for i in path_parameters[1:]:
                        path_link = links[int(i) - 1]
                        links_list.append(path_link)
                    path = Path(path_id, links_list)
                    paths_list.append(path)
                demand = Demand(demand_id, start_node=start_node_id, end_node=end_node_id, demand_volume=demand_volume)
                demand.demand_paths = paths_list
                demands.append(demand)
                # print(demand)
                file.readline()
        net = Net()
        net.links = links
        net.demands = demands
        return net


ir = Input_Reader()
net = ir.read_links("data/net4.txt")
print(net)
