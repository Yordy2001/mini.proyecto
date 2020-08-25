from tabulate import tabulate
from addTeams import equipos

def prinTeam():
    team_list = []
    position = -1
    for equipo in (equipos):
        position +=1
        team_list.append([position, equipo[0], equipo[1], equipo[2]])

    print(tabulate(team_list,headers=["position","nombre", "coronas", "series Mundiales"],tablefmt="grid"))

