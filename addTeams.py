from team import Team
from createId import createId
from database import Database

def addTeam(teams):

    id = createId()

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

    team = Team(id, name, championships, world_series)
    teams.append(team)# store the teams in the data base
