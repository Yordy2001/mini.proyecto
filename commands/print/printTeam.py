from tabulate import tabulate
from database.database import Database
from models.player import Player

# Open the connection to the database
database = Database.connect('mlb.db')

def printTeam():

    teams = database.team.getTeams()

    team_list = []
    position = -1
    for equipo in (teams):
        position +=1
        team_list.append([position,equipo.name.title(), equipo.championships, equipo.world_series])

    print(tabulate(team_list, headers=["position","nombre", "coronas", "series Mundiales"], tablefmt="grid"))
