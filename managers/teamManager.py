from tabulate import tabulate
from database.database import Database
from utils.createId import createId
from database.team import Team

class TeamManager:
    def __init__(self, teams):
        self.teams = Database.getTeams()
        

    @staticmethod
    def addTeam():
        
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
    
    @staticmethod
    def printTeam():
        team_list = []
        position = -1
        for equipo in (teams):
            position +=1
            team_list.append([position, equipo.id, equipo.name, equipo.championships, equipo.world_series])

        print(tabulate(team_list, headers=["position", "ID", "nombre", "coronas", "series Mundiales"], tablefmt="grid"))


    @staticmethod
    def delete_team():

        # print the players so the user can choose which one to change
        TeamManager.printTeam()

        positions = -1
        while True:

            try:
                positions = int(
                    input("introduzca la posicion del equipo a eliminar "))
                team = teams[positions]
                break
            except Exception:
                print("debe introducir un numero de la posicion")

        delete = input("{} es el equipo que desea eliminar? ".format(team.name))

        if delete == "si":
            del teams[positions]

        elif delete == "no":
            print("revise la posicion")
            delete_team()  # return de delete player function
            
        else:
            print("debe introducir SI o NO ")
            delete_team()  # return de delete player function
