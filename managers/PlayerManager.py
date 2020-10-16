from os import system
from tabulate import tabulate
from database.database import  Database
from utils.createId import createId
from models.player import Player
from models.team import Team
from managers.teamManager import TeamManager
from utils.promptNumber import promptNumber

class PlayerManager:
    players = None

    @staticmethod
    def init(players):
        PlayerManager.players = players

    @staticmethod
    def addPlayer(teams):

        id = createId()

        name = str(input("Ingrese el nombre del jugador: "))

        age = promptNumber(message= "introduce la edad del jugador: ")

        # call prin_teams function 
        TeamManager.printTeam()

        positions = promptNumber(message= "Ingrese la posicion del equipo al que quiere que pertenezca el jugador: ")
        team_id = teams[positions].id

        player = Player(id, name, age, team_id)
        PlayerManager.players.append(player)# Stores the list of players in the database

    @staticmethod
    def printPlayer():
        count = -1
        table = []
        for jugador in (PlayerManager.players):
            count +=1
            table.append([count,jugador.name.capitalize(),
                    jugador.age])

        print(tabulate(table, headers=["position",
                    "NAME", "AGE"], tablefmt="grid"))

    @staticmethod
    def editPlayer():

        # print all players
        PlayerManager.printPlayer()

        positions = promptNumber(message= "Introduzca la posición del jugador a editar: ")
        player = PlayerManager.players[positions]

        ask = input(
            "{} Éste es el jugador que desea editar ? ".format(
                player.name))

        if ask == "si":

            name = input("Edita el nombre {} ".format(player.name))
            age = input("Edita la edad {} ".format(player.age))
            team_id = input("Edita el equipo {} ".format(player.team_id))

            if name != "":
                player.name = name

            if age != "":
                player.age = age

            if team_id != "":
                player.team_id = team_id

        elif ask == "no":
            system("cls")
            print("Revise bien la posición")
            return PlayerManager.editPlayer()

        else:
            system("cls")
            print("Su respuesta debe ser SI o NO")
            return PlayerManager.editPlayer() 

    @staticmethod
    def deletePlayer():

        # print the players so the user can choose which one to change
        PlayerManager.printPlayer()

        positions = promptNumber(message= "introduzca la posicion del jugador a eliminar: ")
        player = PlayerManager.players[positions]

        delete = input("{} es el jugador que desea eliminar? ".format(player.name.capitalize()))

        if delete == "si":
            del PlayerManager.players[positions]

        elif delete == "no":
            print("revise la posicion")
            PlayerManager.deletePlayer()  # return de delete player function

        else:
            print("debe introducir SI o NO ")
            PlayerManager.deletePlayer()  # return de delete player function
