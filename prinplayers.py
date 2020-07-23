from tabulate import tabulate
from os import system

table = []
def prinPlayers(players):
    system("cls")
    
    for jugador in (players):
        table.append([jugador.name.capitalize(),
                jugador.age, jugador.team.capitalize()])
       
    print(tabulate(table, headers=[
                                "NAME", "AGE", "TEAM"], tablefmt="grid"))



