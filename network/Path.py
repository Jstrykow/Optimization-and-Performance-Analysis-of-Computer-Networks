"""
Path:
    - path id
    - link list [links_ids]
"""
from network.Link import Link 


class Path:
    def __init__(self, path_id: int, links_list):
        self.links_list = []
        self._path_id = path_id

    def get_path_id(self):
        return self._path_id
    
    def add_link(self, link: Link):
        self.add_link.append(link)
