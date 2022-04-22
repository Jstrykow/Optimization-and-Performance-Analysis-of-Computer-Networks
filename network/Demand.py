from typing import Any, List
from network.Path import Path
"""
demands class
- number of demands
- Demands list
    Demand: 
    - start node
    - end node
    - demand volume
"""


class Demand:
    def __init__(self, start_node: int, end_node: int, demand_volume: int, paths_list: List[any] = None):
        self.start_node = start_node
        self.end_node = end_node
        self.demand_volume = demand_volume
        if paths_list is not None:
            new_paths_list = paths_list.copy()
            self.paths_list = new_paths_list
        else:
            self.paths_list = []

    def __str__(self):
        resp = f"start node: {self.start_node}, end node: {self.end_node}, demand_volume: {self.demand_volume}, paths list: "
        for path in self.paths_list:
            resp += f" {path} "
        return resp