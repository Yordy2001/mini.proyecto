from os import system
from tabulate import tabulate
from database.database import Database
from managers.PlayerManager import PlayerManager
from managers.teamManager import TeamManager
from utils.tables import *

# Open the connection to the database
Database.connect('mlb.db')

# Get the list of players from the database
players = Database.getPlayers()
# get the list of teams from the database
teams = Database.getTeams()

PlayerManager.init(players)

TeamManager.init(teams)

while True:
    system("cls")

    # print the main table so the user can select 
    Table()

    select = input(str("Seleccione la opcion deseada: "))

    if select == "1":

        Table.TablePlayer()

        select_table_player = input("seleciona una opciin del menu de player: ")

        if select_table_player == "1":
            PlayerManager.addPlayer(teams)

        elif select_table_player == "2":
            PlayerManager.printPlayer()

        elif select_table_player == "3":
            PlayerManager.deletePlayer()

        elif select_table_player == "4":
            PlayerManager.editPlayer()

        else:
            print("Revise la escritura!!")
            PlayerManager(players)

    elif select == "2":

        Table.TableTeam()

        select_table_team = input(str("seleciona una opciin del menu de team: "))

        if select_table_team == "1":
            TeamManager.addTeam()

        elif select_table_team == "2":
            TeamManager.printTeam()

        elif select_table_team == "3":
            TeamManager.delete_team()

        else:
            print("revise la escritura")
            TeamManager(teams)

    elif select == "salir del programa" or select == "3":
        system("cls")

        print("Bye")
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
