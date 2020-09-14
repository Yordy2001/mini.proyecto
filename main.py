from os import system
from tabulate import tabulate
from database.database import Database
from managers.teamManager import TeamManager 
from managers.PlayerManager import PlayerManager
from utils.tables import *

# Open the connection to the database
Database.connect('mlb.db')

# Get the list of players from the database
players = Database.getPlayers()
# get the list of teams from the database
teams = Database.getTeams()

print("MAJOR LENGUAJE BASEBALL\n")

while True:
    system("cls")

    # print the main table so the user can select 
    Table()

    select = input(str("Seleccione la opcion deseada: "))
    
    if select == "1":
        Table.TablePlayer()

    elif select == "2":
        Table.TableTeam()

    else:
        print("")

    select_table = input(str("Seleccione la opcion deseada: "))
    
    if select_table == "1":
        
        select_player = input("selecione una opcion: ")

        if select_player == "1":
            PlayerManager.addPlayer()

        elif select_player == "2":
            PlayerManager.printPlayer()

        elif select_player == "3":
            PlayerManager.editPlayer()

        elif select_player == "4":
            PlayerManager.deletePlayer()
        
        else:
            print("Revise la escritura!!")
            PlayerManager(players)

    elif select_table == "2":
    
        print("selecione una opcion! ")
        select_team = input(' ')

        if select_team == "1":
            TeamManager.addTeam()

        elif select_team == "2":
            TeamManager.printTeam()

        elif select_team == "3":
            TeamManager.delete_team()

        else:
            print("revise la escritura")
            TeamManager(teams)

    elif select == "salir del programa" or select == "3":
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
