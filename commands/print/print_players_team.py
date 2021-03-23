from tabulate import tabulate
from database.database import Database
from models.player import Player
from models.team import Team

# Open the connection to the database
database = Database.connect('mlb.db')

def PlayerTeam(name_team):

    players = database.player.getPLayersT(name_team)
    player_list = []

    count = -1
    for player in (players):
        count = +1
        player_list.append([count, *player])

    print(tabulate(player_list, headers=["position",
                                         "NAME", "AGE", "TEAM", "CHAMPIONSHIP", "WORD SERIES"], tablefmt="grid"))
