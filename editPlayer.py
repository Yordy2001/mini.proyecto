from os import system
from database import Database
from prinplayers import *


def editPlayer(players):
    system("cls")

    # imprime los jugadores para que el usario elija cual cambiar
    prinPlayers(players)

    position = int(input("Introduzca la posicion del jugador a editar "))

    print(table[position])

    ask = input("Este es el jugador que desea editar ? ")

    if ask == "si":

        a = input("Que dato desea editar ? ")
        e = input("Introduzca el nuevo dato ")

        if a == "nombre":
            table[position][0] = e

        elif a == "edad":
            table[position][1] = e

        elif a == "apellido":
            table[position][2] = e

    elif ask == "no":
         print("revise bien la posicion")
    
    else:
        print("su respuesta debe ser SI o NO")
        
    

