from commands.add.addPlayer import addPlayer
from commands.add.addTeam import addTeam

def add (arg):

    if arg == "player":
        addPlayer()

    elif arg == "team":
        addTeam()

    else:
        print("Los comandos para esta funcion solo son: 'player' y 'team'")
