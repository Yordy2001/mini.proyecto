from database.database import Database
from utils.promptNumber import promptNumber
from commands.print.print import printTeam

# Open the connection to the database
database = Database.connect('mlb.db')

def deleteTeam():

    teams = database.team.getTeams()

    # print the players so the user can choose which one to change
    printTeam()

    # get the position from the get position function
    positions = promptNumber("introduzca la posicion del equipo a eliminar: ")

    team = teams[positions]

    delete = input("{}, es el equipo que desea eliminar? ".format(team.name))

    if delete == "si":
        del teams[positions]

    elif delete == "no":
        print("Revise la posicion")
        deleteTeam()  # return de delete player function

    else:
        print("Debe introducir SI o NO ")
        deleteTeam()  # return de delete player function

    database.player.setPlayers()
