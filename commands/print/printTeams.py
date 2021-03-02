from tabulate import tabulate
from database.database import Database
from models.player import Player
from models.team import Team

# Open the connection to the database
database = Database.connect('mlb.db')

def printTeams():

    teams = database.team.getTeams()
    
    team_list = []
    position = -1
    for equipo in (teams):
        position +=1
        team_list.append([position, *equipo.print()])

    print(tabulate(team_list, headers=["position","name", "championships", "world series"], tablefmt="grid"))
