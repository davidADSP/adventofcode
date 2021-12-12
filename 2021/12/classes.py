class Node():
    def __init__(self, id):
        self.id = id
        self.neighbours = []
        self.small = self.id.islower()
    def __repr__(self):
        return self.id


