from os import system
from commands.print.print import printPlayer
from commands.print.print import printTeam
from utils.promptNumber import promptNumber

def editPlayer(players):
    
        # print all players
        printPlayer(players)

        positions = promptNumber("Introduzca la posición del jugador a editar: ")
        player = players[positions]

        ask = input(
            "{} Éste es el jugador que desea editar ? ".format(
                player.name))

        if ask == "si":

            name = input("Edita el nombre {} ".format(player.name))
            age = input("Edita la edad {} ".format(player.age))
            team_id = input("Edita el equipo {} ".format(player.team_id))

            if name != "":
                player.name = name

            if age != "":
                player.age = age

            if team_id != "":
                player.team_id = team_id

        elif ask == "no":
            system("cls")
            print("Revise bien la posición")
            editPlayer(players)

        else:
            system("cls")
            print("Su respuesta debe ser SI o NO")
            editPlayer(players)
            
def editTeam(teams):
    
        # print all players
        printTeam(teams)

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
            system("cls")
            print("Revise bien la posición")
            editPlayer(team)

        else:
            system("cls")
            print("Su respuesta debe ser SI o NO")
            editTeam(teams)
