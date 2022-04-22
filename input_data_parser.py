from link import Link
from node import Node

class Input_Reader:
    def read_links(self, name_of_file):
        with open(name_of_file, "r") as file:
            range_of_links = int(file.readline())
            for i in range(range_of_links):
                parameters = file.readline().split()
                start_node_id = parameters[0]
                end_node_id = parameters[1]
                number_of_fibers = parameters[2]
                fiber_cost = parameters[3]
                number_of_lambdas_in_fiber = parameters[4]
                link = Link(start_node_id, end_node_id, number_of_fibers, fiber_cost, number_of_lambdas_in_fiber)
                # adding new nodes, checking node is in array
                # print(link)
            minus_one = int(file.readline())
            if(minus_one != -1):
                print("Error during reading links")
            file.readline()


ir = Input_Reader()
ir.read_links("data/net4.txt")