import sys
from commands.edit.editTeam import editTeam 
from commands.edit.editPlayer import editPlayer

def edit():

    if sys.argv[2] == "player":
        editPlayer()

    elif sys.argv[2] == "team":
        editTeam()
        
    else:
        print("este comado es incoreccto")