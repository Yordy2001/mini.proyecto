from os import system
from database import Database
from tabulate import tabulate
from player import Player
from addPlayer import addPlayer
from prinplayers import *
from editPlayer import editPlayer


# Open the connection to the database
Database.connect('mlb.db');

# Get the list of players from the database
players = Database.getPlayers()


print("MAJOR LENGUAJE BASEBALL\n")

while True:
    system("cls")
    print("SELECCIONE UNA OPCION MARCANDO EL NUMERO DE SU POSICION :\n")
    print("""1.AGREGAR JUGADOR\n2.IPRIMIR JUGADORES\n3.EDITAR JUGADOR\n4.CERRAR PROGRAMA\n""")

    select = input(str("Seleccione la opcion deseada: "))

    if select == "agregar jugador" or select == "1":
        system("cls")
        
        # llama la  funcion de agregar jugador
        addPlayer(players)
        
        print(input("presione cualquier tecla para continuar"))
    
    elif select == "imprimir jugadores" or select == "2":
        system("cls")
        
        # llama la funcion de imprimir jugadores
        prinPlayers(players)
        
        print(input("presione cualquier tecla para continuar"))
    
    elif select == "editar jugador" or select == "3":
        system("cls")
        
        # llama la funcion de editar jugador
        editPlayer(players)
        
        print(input("presione cualquier tecla para continuar"))
    
    elif select =="salir del programa" or select == "4":
        system("cls")
        
        print("bye")
        break

    # avoid an error when entering the wrong data
    else:
        system("cls")
        print("!REVISE SU ESCRITURA!")
        


# Store the player list in the database
Database.setPlayers(players)

# Close the connection to the database
Database.close();
