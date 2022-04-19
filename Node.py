# class representing node
from link import Link


# start node = node_id ? depends on bidiretional of graph
class Node():
    def __init__(self, id):
        self._id = id
        self.links = []
        self.neighbours = []

    def get_id(self):
        return self._id

    def add_link(self, start_node_id: int, end_node_id: int, number_of_fibers: int, fiber_cost: int, number_of_lambdas_in_fiber: int):
        link = Link(start_node_id, end_node_id, number_of_fibers, fiber_cost, number_of_lambdas_in_fiber)
        self.add_neigbour(start_node_id, end_node_id)
        self.links.append(link)

    def add_link(self, link: Link):
        link = Link(link.get_start_node_id(), link.get_end_node_id(), link.get_number_of_fibers(), link.get_fiber_cost(), link.get_number_of_fibers())
        self.add_neigbour(link.get_start_node_id(), link.get_end_node_id())
        self.links.append(link)

    def get_list_of_links(self):
        return self.links

    def add_neigbour(self, start_node_id: int, end_node_id: int):
        if self.get_id() != end_node_id:
            self.neighbours.append(end_node_id)
        else:
            self.neighbours.append(start_node_id)
        
    def __str__(self):
        return f"Node ID:{self.get_id()}, neighbours {self.neighbours}\n"