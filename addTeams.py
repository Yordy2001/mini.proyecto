from team import Team
from idCreator import idCreator
from database import Database

def addTeam(teams):

    id = idCreator()

    name = input("Ingrese el nombre del equipo ")

    while True:
        try:
            championships = int(input("Ingrese  la cantidad de coronas que ha ganado "))
            break
        except ValueError:
            print("Debe ingresar un numero entero")

    while True:
        try:
            world_series = int(input("Ingrese  la cantidad de series mundiales que ha ganado ")) 
            break   
        except ValueError:
            print("Debe introducir un numero entero")  

    all_team = Team(id, name, championships, world_series)
    teams.append(all_team)# store the teams in the list equipos
    