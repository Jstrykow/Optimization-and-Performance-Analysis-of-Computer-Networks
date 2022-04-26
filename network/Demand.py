from typing import Any, List
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
    def __init__(self, demand_id: int, start_node: int, end_node: int, demand_volume: int, paths_list: List[Any] = None):
        # demand id
        self.demand_id = int(demand_id)
        self.start_node = int(start_node)
        self.end_node = int(end_node)
        self.demand_volume = int(demand_volume)
        self.paths_list = []

    def __str__(self):
        resp = f"start node: {self.start_node}, end node: {self.end_node}, demand_volume: {self.demand_volume}, paths list: "
        for path in self.paths_list:
            resp += f" {path} "
        return resp

    def get_number_of_paths(self) -> int:
        return len(self.paths_list)
