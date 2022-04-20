from cgi import print_arguments
from operator import truediv
from graph import Graph
from link import Link
from node import Node

class Input_Reader():
    def __init__(self, name_of_file):
        self.name_of_file = name_of_file
        with open(name_of_file, "r") as file:
            self.data = file.readlines()
        self.links = []
        self.read_links()

    def read_links(self):
        # not used, maybe fo rerror detection self.range = int(self.data[0]) 
        for element in self.data[1:]:
            if(element == '-1\n'):
                for link in self.links: print(link)
                return
            parameters = element.split()
            start_node_id = parameters[0]
            end_node_id = parameters[1]
            number_of_fibers = parameters[2]
            fiber_cost = parameters[3]
            number_of_lambdas_in_fiber = parameters[4]
            link = Link(start_node_id, end_node_id, number_of_fibers, fiber_cost, number_of_lambdas_in_fiber)
            # adding new nodes, checking node is in array
            self.links.append(link)
    
            

Input_Reader("data/net4.txt")