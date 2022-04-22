# class for edges
"""
link
- number of fibers
- fiber cost
- number of lambdas in fiber
"""


class Link():
    # add link id
    def __init__(self, start_node_id: int, end_node_id: int, number_of_fibers: int, fiber_cost: int, number_of_lambdas_in_fiber: int):
        self.start_node_id = start_node_id
        self.end_node_id = end_node_id
        self.number_of_fibers = number_of_fibers
        self.fiber_cost = fiber_cost
        self.number_of_lambdas_in_fiber = number_of_lambdas_in_fiber

    def get_start_node_id(self):
        return self.start_node_id

    def get_end_node_id(self):
        return self.end_node_id

    def get_number_of_fibers(self):
        return self.number_of_fibers

    def get_fiber_cost(self):
        return self.fiber_cost

    def get_number_of_lambdas_in_fiber(self):
        return self.number_of_lambdas_in_fiber
    
    def __str__(self):
        return f"Link: start: {self.start_node_id}, end: {self.end_node_id}, number of fibers: {self.number_of_fibers}, fiber cost: {self.fiber_cost}, number of lambdas_in_fiber: {self.number_of_lambdas_in_fiber}"

