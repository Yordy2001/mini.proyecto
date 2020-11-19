from database.database import Database
from commands.print.print import printPlayer
from commands.print.print import printTeam
from utils.promptNumber import promptNumber

database = Database.connect('mlb.db')

def editTeam():

    teams = database.team.getTeams()

    # print all players
    printTeam()

    positions = promptNumber("Introduzca la posición del equipo a editar: ")

    team = teams[positions]

    ask = input(
        "{} Éste es el equipo que desea editar ? ".format(
            team.name))

    if ask == "si":

        name = input("Edita el nombre {} ".format(team.name))

        championships = input("Edita la cantidad de coronas de {} ".format(team.name))

        world_series = input("Edita la cantidad de series mudiales de {} ".format(team.name))

        if name != "":
            team.name = name

        if championships != "":
            team.championships = championships

        if world_series != "":
            team.world_series = world_series

    elif ask == "no":
            print("Revise bien la posición")
            editTeam()

    else:
        print("Su respuesta debe ser SI o NO")
        editTeam()

    database.team.updateTeam(team)
