import sys
from commands.delete.deletePlayer import deletePlayer 
from commands.delete.deleteTeam import deleteTeam

def delete():

    if sys.argv[2] == "player":
        deletePlayer()

    elif sys.argv[2] == "team":
        deleteTeam()

