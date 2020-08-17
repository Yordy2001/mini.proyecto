from tabulate import tabulate
from teams import Team


def prinTeam():
    lista = []
    position = -1
    for i in range(len(Team.name)):
        position +=1
        lista.append([position, Team.name[i], Team.coronas[i], Team.series_mundiales[i]])

    print(tabulate(lista,headers=["position","nombre", "coronas", "series Mundiales"],tablefmt="grid"))

