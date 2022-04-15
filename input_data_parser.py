from graph import Graph
from link import Link
from node import Node

class Input_Reader():
    def __init__(self, name_of_file):
        self.name_of_file = name_of_file
        with open(name_of_file, "r") as file:
            self.data = file.readlines()
        self.graph_data()

    def graph_data(self):
        range = int(self.data[0])
        for element in self.data[1:]:
            if(element == '-1\n'):
                return
            parameters = element.split()
            # print(element)
            start_node_id = parameters[0]
            end_node_id = parameters[1]
            number_of_fibers = parameters[2]
            fiber_cost = parameters[3]
            number_of_lambdas_in_fiber = parameters[4]
            link = Link(start_node_id, end_node_id, number_of_fibers, fiber_cost, number_of_lambdas_in_fiber)
            print(link)
            

Input_Reader("data/net4.txt")