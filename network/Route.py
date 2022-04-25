class Route:
    def __init__(self, list_of_paths: list, demand_id: int, path_id: int):
        self.demand_id = demand_id
        self.path_id = path_id
        self.links = [int(link_id) for link_id in list_of_paths]