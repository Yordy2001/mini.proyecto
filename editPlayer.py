from os import system
from database import Database
from prinplayers import *

def editPlayer(players):

    #print the players so the user can choose which one to change
    prinPlayers(players)
   
    position = int(input("Introduzca la posición del jugador a editar "))

    player = players[position]
    
    ask = input("{} Éste es el jugador que desea editar ? ".format(player.name))

    if ask == "si":

        name = input("edita el nombre {} ".format(player.name))
        age = input("edita la edad {} ".format(player.age))
        team = input("edita el equipo {} ".format(player.team))

        if name != "":
            player.name = name

        if age != "":
            player.age = age

        if team != "":
            player.team = team

    elif ask == "no":
        print("revise bien la posicion")
        
    else:
        print("su respuesta debe ser SI o NO")
