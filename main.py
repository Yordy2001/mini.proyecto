from os import system
from tabulate import tabulate
from database import Database
from player import Player
from addPlayer import addPlayer
from printPlayer import *
from editPlayer import editPlayer
from delete_player import deletePlayer
from team import Team
from addTeams import addTeam
from print_teams import prinTeam
from delete_team import delete_team


# Open the connection to the database
Database.connect('mlb.db')

# Get the list of players from the database
players = Database.getPlayers()
# get the list of teams from the database
teams = Database.getTeams()
 
print("MAJOR LENGUAJE BASEBALL\n")

while True:
    system("cls")
    print("SELECCIONE UNA OPCION MARCANDO EL NUMERO DE SU POSICION :\n")
    print("1.AGREGAR JUGADOR\n2.IPRIMIR JUGADORES\n3.EDITAR JUGADOR\n4.ELIMINAR JUGADOR")
    print("5.AGREGAR EQUIPO\n6.IMPRIMIR EQUIPOS\n7.ELIMINAR EQUIPO\n8.CERRAR PROGRAMA\n ")

    select = input(str("Seleccione la opcion deseada: "))

    if select == "agregar jugador" or select == "1":
        system("cls")

        # call the add player function
        addPlayer(players, teams)

    elif select == "imprimir jugadores" or select == "2":
        system("cls")

        # call the print player function
        prinPlayers(players)

    elif select == "editar jugador" or select == "3":
        system("cls")

        # call edid player function
        editPlayer(players)

    elif select == "eliminar jugador" or select == "4":
        system("cls")

        # call delete player function
        deletePlayer(players)

    elif select == "agregar equipo" or select == "5":
        system("cls")

        # call add team function
        addTeam(teams)

    elif select == "imprimir equipos" or select == "6":
        system("cls")

        # call print team function
        prinTeam(teams)

    elif select == "eliminar equipo" or select == "7":
        system("cls")

        # call delete team fuction
        delete_team(teams)

    elif select == "salir del programa" or select == "8":
        system("cls")

        print("bye")
        break

    # avoid an error when entering the wrong data
    else:
        system("cls")
        print("!REVISE SU ESCRITURA!")

    # Store the player list in the database
    Database.setPlayers(players)
    Database.setTeams(teams)

    print(input("presione cualquier tecla para continuar"))

# Close the connection to the database
Database.close()
