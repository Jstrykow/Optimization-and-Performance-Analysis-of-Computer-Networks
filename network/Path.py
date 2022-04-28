"""
Path:
    - path id
    - link list [links_ids]
"""
from typing import List
from network.Link import Link

class Path:
    def __init__(self, path_id: int, links_list: List[Link]):
        # self.links_list = []
        self.path_id = path_id
        self.links_list = links_list

    def __str__(self):
        msg = ""
        msg += f"\n path_id: {self.path_id}: links_list: " 
        for link in self.links_list:
            msg += " " + str(link.link_id)
        return msg
