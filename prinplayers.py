from tabulate import tabulate
from os import system

def prinPlayers(players):
    count = -1
    table = []
    for jugador in (players):
        count +=1
        table.append([count,jugador.name.capitalize(),
                jugador.age, jugador.team.capitalize()])
       
    print(tabulate(table, headers=["position",
                "NAME", "AGE", "TEAM"], tablefmt="grid"))
