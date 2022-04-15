# class representing node


class Node():
    def __init__(self, id):
        self._id = id
        self.links = []

    def get_if(self):
        return self._id
