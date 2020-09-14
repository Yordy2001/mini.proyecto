from os import system
from tabulate import tabulate
from database.database import  Database
from utils.createId import createId
from managers import teamManager
from managers.teamManager import TeamManager
from database.player import Player
from database.team import Team

class PlayerManager:
    def __init__(self, players):
        players = Database.setPlayers()

    @staticmethod
    def addPlayer():

        players = []

        id = createId()

        name = str(input("Ingrese el nombre del jugador: "))
        age = 0
        while True:

            try:
                age = int(input("Ingrese la edad del jugador: "))
                break
            except ValueError:

                print("DEBE INGRESAR UN NUMERO ENTERO \n")            


        print("Ingrese la posicion del equipo al que quiere que pertenezca el jugador! \n")

        # call prin_teams function 
        TeamManager.printTeam()
        
        position = -1
        while True:
            try:
                positions = int(input("position-> "))
                team_id = TeamManager.addTeam[positions].id
                break
            except Exception:
                print("revice la posicion!!")

        player = PlayerManager.addPlayer(id, name, age, team_id)
        players.append(player)# Stores the list of players in the database

    @staticmethod
    def printPlayer(players):
        count = -1
        table = []
        for jugador in (players):
            count +=1
            table.append([count,jugador.id, jugador.name.capitalize(),
                    jugador.age, jugador.team_id])
        
        print(tabulate(table, headers=["position", "ID",
                    "NAME", "AGE", "TEAM"], tablefmt="grid"))
    
    @staticmethod
    def editPlayer(players):
            
        position = 0
        while True:
            try:
                position = int(
                    input("Introduzca la posición del jugador a editar "))
                player = players[position]
                break
            except Exception:
                print("Debe introducir una poscion")

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
            return editPlayer(players)

        else:
            system("cls")
            print("Su respuesta debe ser SI o NO")
            return editPlayer(players) 

    @staticmethod
    def deletePlayer(players):

        # print the players so the user can choose which one to change
        PlayerManager.printPlayer(players)

        positions = -1
        while True:

            try:
                positions = int(
                    input("introduzca la posicion del jugador a eliminar "))
                player = players[positions]
                break
            except Exception:
                print("debe introducir un numero de la posicion")

        delete = input("{} es el jugador que desea eliminar? ".format(player.name))

        if delete == "si":
            del players[positions]

        elif delete == "no":
            print("revise la posicion")
            PlayerManager.deletePlayer()  # return de delete player function

        else:
            print("debe introducir SI o NO ")
            PlayerManager.deletePlayer()  # return de delete player function
