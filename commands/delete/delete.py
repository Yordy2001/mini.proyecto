from commands.delete.deletePlayer import deletePlayer 
from commands.delete.deleteTeam import deleteTeam

def delete(arg):

    if  arg == "player":
        deletePlayer()

    elif arg == "team":
        deleteTeam()

    else:
        print("los comandos para esta funcion solo son: 'player' y 'team'")
