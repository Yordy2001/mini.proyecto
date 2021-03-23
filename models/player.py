class Player:

    def __init__(self, id, name, age, team_id, avg):
        self.id = id
        self.name = name
        self.age = age
        self.team_id = team_id
        self.avg = avg

    def print(self):

        return [self.name.title(), self.age, self.avg]
