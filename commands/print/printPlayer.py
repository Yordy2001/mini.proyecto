from tabulate import tabulate
from database.database import Database
from models.player import Player

# Open the connection to the database
database = Database.connect('mlb.db')

def printPlayer():
  
    players = database.player.getPlayers()

    count = -1
    table = []
    for jugador in (players):
        count += 1
        table.append([count, jugador.name.capitalize(),
                        jugador.age])

    print(tabulate(table, headers=["position",
                                    "NAME", "AGE"], tablefmt="grid"))
