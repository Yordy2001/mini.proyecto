class Team:

    def __init__(self, id, name, championships, world_series):
        self.id = id
        self.name = name
        self.championships = championships
        self.world_series = world_series

    def print(self):
        
        return [self.name.title() , str(self.championships), str(self.world_series)]
