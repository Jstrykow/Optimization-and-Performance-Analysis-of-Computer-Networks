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
    def __init__(self, start_node: int, end_node: int, demand_volume: int):
        self.start_node = start_node
        self.end_node = end_node
        self.demand_volume = demand_volume
    
    def __str__(self):
        return f"start node: {self.start_node}, end node: {self.end_node}, demand_volume: {self.demand_volume}"
