from tabulate import tabulate

def prinTeam(teams):
    team_list = []
    position = -1
    for equipo in (teams):
        position +=1
        team_list.append([position, equipo.id, equipo.name, equipo.championships, equipo.world_series])

    print(tabulate(team_list,headers=["position", "ID", "nombre", "coronas", "series Mundiales"],tablefmt="grid"))

