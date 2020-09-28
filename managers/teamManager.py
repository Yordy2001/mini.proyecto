from os import system
from tabulate import tabulate
from database.database import  Database
from utils.createId import createId
from database.team import Team
from utils.getInt import getInt
from utils.getPosition import position

class TeamManager:
    teams = None

    @staticmethod
    def init(teams):
      TeamManager.teams = teams

    @staticmethod
    def addTeam():

        id = createId()

        name = input("Ingrese el nombre del equipo ")

        print("Ingrese  la cantidad de coronas que ha ganado ")
        championships = getInt()

        print("Ingrese  la cantidad de series mundiales que ha ganado ")
        world_series = getInt()
        
        team = Team(id, name, championships, world_series)
        TeamManager.teams.append(team)# store the teams in the data base

    @staticmethod
    def printTeam():
        team_list = []
        position = -1
        for equipo in (TeamManager.teams):
            position +=1
            team_list.append([position,equipo.name, equipo.championships, equipo.world_series])

        print(tabulate(team_list, headers=["position","nombre", "coronas", "series Mundiales"], tablefmt="grid"))

    @staticmethod
    def delete_team():

        # print the players so the user can choose which one to change
        TeamManager.printTeam()

        print("introduzca la posicion del equipo a eliminar ")
        # get the position from the get position function
        positions = position()
        team = TeamManager.teams[positions]

        delete = input("{} es el equipo que desea eliminar? ".format(team.name))

        if delete == "si":
            del TeamManager.teams[positions]

        elif delete == "no":
            print("revise la posicion")
            delete_team()  # return de delete player function 
        else:
            print("debe introducir SI o NO ")
            delete_team()  # return de delete player function