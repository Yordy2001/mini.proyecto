from os import system
from database import Database
from prinplayers import *


def editPlayer(players):

    # print the players so the user can choose which one to change
    prinPlayers(players)

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
        team = input("Edita el equipo {} ".format(player.team))

        if name != "":
            player.name = name

        if age != "":
            player.age = age

        if team != "":
            player.team = team

    elif ask == "no":
        system("cls")
        print("Revise bien la posición")
        return editPlayer(players)

    else:
        system("cls")
        print("Su respuesta debe ser SI o NO")
        return editPlayer(players)      