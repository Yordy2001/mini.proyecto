from motor import Motor

class Player:
    def __init__(self, id, name, age, team_id):
        motor = Motor.crearInstancia('motor 4');
        print(motor.name);
        self.id = id
        self.name = name
        self.age = age
        self.team_id = team_id
