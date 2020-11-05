# system libraries
import sys
from os import system
from tabulate import tabulate
# database import
from database.playerD import PlayerD
from database.teamD import TeamD
from database.database import Database
# command import
from commands.help.help import help
from commands.add.add import addPlayer, addTeam
from commands.print.print import printPlayer, printTeam
from commands.delete.delete import deletePlayer, deleteTeam 
from commands.edit.edit import editPlayer, editTeam
# other import
from utils.tables import *

# Open the connection to the database
database = Database.connect('mlb.db')
# Get the list of players from the database
players = database.player.getPlayers()
# get the list of teams from the database
teams = database.team.getTeams()

if len(sys.argv) <= 2:
    print(f"Debe introducir por lo menos 1 parametro")

elif sys.argv[1] == "help":
    help()

elif sys.argv[1] == "add" and sys.argv[2] == "player":
    addPlayer(teams)

elif sys.argv[1] == "add" and sys.argv[2] == "team":
    addTeam(teams)
       
elif sys.argv[1] == "print" and  sys.argv[2] == "player":
    printPlayer(players)

elif sys.argv[1] == "print" and  sys.argv[2] == "team":
    printTeam(teams)

elif sys.argv[1] == "delete" and  sys.argv[2] == "player":
    deletePlayer(players)

elif sys.argv[1] == "delete" and  sys.argv[2] == "team":
    deleteTeam(teams)

elif sys.argv[1] == "edit" and  sys.argv[2] == "player":
    editPlayer(players)

elif sys.argv[1] == "edit" and  sys.argv[2] == "team":
    editTeam(teams)

elif len(sys.argv) == 2:
     print("Debe intoducir un sub-comando")

else: 
    print(f"Error: parametro {sys.argv[1:]} no encontrado, puede introcir <<help>> y mirar los comandos!")

# set the player and team in the data base
database.player.setPlayers(players)
database.team.setTeams(teams)

print(input("Presione cualquier tecla para continuar"))

# Close the connection to the database
database.close()
