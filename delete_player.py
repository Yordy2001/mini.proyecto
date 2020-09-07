from os import system
from printPlayer import prinPlayers
from database import Database


def deletePlayer(players):

    # print the players so the user can choose which one to change
    prinPlayers(players)

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
        deletePlayer(players)  # return de delete player function
    else:
        print("debe introducir SI o NO ")
        deletePlayer(players)  # return de delete player function
