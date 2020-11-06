from commands.edit.editTeam import editTeam 
from commands.edit.editPlayer import editPlayer


def edit(arg):

    if  arg== "player":
        editPlayer()

    elif arg == "team":
        editTeam()

    else:
        print("los comandos para esta funcion solo son: 'player' y 'team'")
