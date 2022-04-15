# class representing node
from link import Link


# start node = node_id ? depends on bidiretional of graph
class Node():
    def __init__(self, id):
        self._id = id
        self.links = []
        self.neighbours = []

    def get_if(self):
        return self._id

    def add_link(self, start_node_id: int, end_node_id: int, number_of_fibers: int, fiber_cost: int, number_of_lambdas_in_fiber: int):
        link = Link(start_node_id, end_node_id, number_of_fibers, fiber_cost, number_of_lambdas_in_fiber)
        self.neighbours.append(end_node_id)
        self.links.append(link)
  
    def get_list_of_links(self):
        return self.links
