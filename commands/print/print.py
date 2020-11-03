from tabulate import tabulate

def printPlayer(players):
    count = -1
    table = []
    for jugador in (players):
        count += 1
        table.append([count, jugador.name.capitalize(),
                        jugador.age])

    print(tabulate(table, headers=["position",
                                    "NAME", "AGE"], tablefmt="grid"))

def printTeam(teams):
        team_list = []
        position = -1
        for equipo in (teams):
            position +=1
            team_list.append([position,equipo.name, equipo.championships, equipo.world_series])

        print(tabulate(team_list, headers=["position","nombre", "coronas", "series Mundiales"], tablefmt="grid"))
