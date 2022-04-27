"""
Path:
    - path id
    - link list [links_ids]
"""


class Path:
    def __init__(self, path_id: int, links_list):
        self.links_list = []
        self.path_id = path_id
        self.links_list = links_list

    def __str__(self):
        return f"path id: {self.path_id}, link list: {self.links_list}"
