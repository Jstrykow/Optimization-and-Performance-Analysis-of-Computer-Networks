# class Graph
from network.Node import Node


class Graph():
    def __init__(self):
        self.nodes = []

    # adding nodes with links to graph
    def add_nodes(self, node: Node):
        self.nodes.append(node)
    
    def get_nodes(self):
        rsp = ""
        for nodes in self.nodes:
            rsp += str(nodes)
        return rsp 
