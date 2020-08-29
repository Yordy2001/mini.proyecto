from os import system
from tabulate import tabulate
from database import Database
from player import Player
from addPlayer import addPlayer
from prinplayers import *
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
 
print("MAJOR LENGUAJE BASEBALL\n")

while True:
    system("cls")
    print("""
    x------------------------------------------------------------x
    |  "SELECCIONE UNA OPCION MARCANDO EL NUMERO DE SU POSICION: |
    |                                                            |     
    |   1.AGREGAR JUGADOR                                        |
    |   2.IPRIMIR JUGADORES                                      |
    |   3.EDITAR JUGADOR                                         |
    |   4.ELIMINAR JUGADOR                                       |
    |   5.AGREGAR EQUIPO                                         |
    |   6.IMPRIMIR EQUIPOS                                       |
    |   7.ELIMINAR EQUIPO                                        |
    |   8.CERRAR PROGRAMA                                        |
    x------------------------------------------------------------x""")
   
    select = input(str("Seleccione la opcion deseada: "))

    if select == "agregar jugador" or select == "1":
        system("cls")

        # call the add player function
        addPlayer(players)

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
        addTeam()

    elif select == "imprimir equipos" or select == "6":
        system("cls")

        # call print team function
        prinTeam()

    elif select == "eliminar equipo" or select == "7":
        system("cls")

        # call delete team fuction
        delete_team()

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

    print(input("presione cualquier tecla para continuar"))

# Close the connection to the database
Database.close()
