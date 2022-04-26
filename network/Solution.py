# class for solutions
from typing import List

class link_load():
    def __init__(self, link_id: int, number_of_signals:int, number_of_fiber: int):
        self.link_id = link_id
        self.number_of_signals = number_of_signals
        self.number_of_fibers = number_of_fiber



class Solution():
    def __init__(self, number_of_links: int, link_load_list: List[link_load] ):
        # <link part>
        self.number_of_links = number_of_links
        self.link_load_list = link_load_list
        # <demand part>



        # <demand part>