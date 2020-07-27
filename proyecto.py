from os import system
from database import Database
from tabulate import tabulate
from player import Player

# Open the connection to the database
Database.connect('mlb.db');

# Get the list of players from the database
players = Database.getPlayers()


system("cls")
print("MAJOR LENGUAJE BASEBALL\n")

while True:

    print("Seleccione una opcion:\n")
    print("1.AGREGAR JUGADOR\n2.IMPRIMIR JUGADORES\n3.CERRAR PROGRAMA\n ")
    select = input("Seleccione la opción deseada: ")

    if select == "agregar jugador" or select == "1":
        system("cls")
    
        name = str(input("ingrese el nombre del jugador "))
        age = 0
        while True:

            try:
                age = int(input("ingrese la edad de jugador "))
                break
            except ValueError:
                print("DEBE INGRESAR UN NUMERO ENTERO")
                pass

        team = str(input("ingrese el equipo del jugador "))
        player = Player(name, age, team)
        players.append(player)# Almacena la lista de jugadores en la base de datos
                
        # Store the player list in the database
        Database.setPlayers(players)

        print(input("presione cualquier tecla para continuar"))

    elif select == "imprimir jugadores" or select == "2":
        system("cls")
        table = []
        for player in (players):
            table.append([player.name.capitalize(), player.age, player.team.capitalize()])

        print(tabulate(table, headers=[
              "nombre", "edad", "equipo"], tablefmt="grid"))
        
        print(input("presione cualquier tecla para regresar"))

    elif select == "cerrar programa" or select == "3":
        system("cls")
        print("bye")
        break

    else:
        system("cls")
        print("!REVISE SU ESCRITURA!")
        
# Store the player list in the database
Database.setPlayers(players)

# Close the connection to the database
Database.close();
