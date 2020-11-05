import sys
from commands.add.addPlayer import addPlayer
from commands.add.addTeam import addTeam

def add (argv):

    if sys.argv[2] == "player":
        addPlayer()

    elif sys.argv[2] == "team":
        addTeam()
    else:
        print("los comandos para esta funcion solo son: 'player' y 'team'")
