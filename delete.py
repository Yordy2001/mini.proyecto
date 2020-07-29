from os import system
from prinplayers import *
from database import Database

def deletePlayer(players):

    #print the players so the user can choose which one to change
    prinPlayers(players)

    positions = int(input("introduzca la posicion del jugador a eliminar "))

    player = players[positions]

    delete = input("{} es el jugador que desea eliminar? ".format(player.name))

    if delete == "si":
        del players[positions]

    if delete == "no":
        print("revise la posicion")
        deletePlayer(players)

    else:
        print("debe introducir SI o NO ")
        deletePlayer(players)