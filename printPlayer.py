from tabulate import tabulate

def prinPlayers(players):
    count = -1
    table = []
    for jugador in (players):
        count +=1
        table.append([count,jugador.id, jugador.name.capitalize(),
                jugador.age, jugador.team_id])
       
    print(tabulate(table, headers=["position", "ID",
                "NAME", "AGE", "TEAM"], tablefmt="grid"))
                