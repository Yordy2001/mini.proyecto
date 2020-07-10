from os import system
from database import Database
from tabulate import tabulate
from player import Player

# Open the connection to the database
Database.connect('mlb.db');

# Get the list of players from the database
players = Database.getPlayers()


print("MAJOR LENGUAJE BASEBALL\n")

while True:
    system("cls")
    print("SELECCIONE UNA OPCION MARCANDO EL NUMERO DE SU POSICION :\n")
    print("""1.AGREGAR JUGADOR\n2.PRIMIR JUGADORES\n3.CERRAR PROGRAMA\n""")

    select = input(str("Seleccione la opcion deseada: "))

    if select == "agregar jugador" or select == "1":
        system("cls")
        
        name = input("ingrese el nombre del jugador")
        age = 0
        while True:

            try:
                age = int(input("ingrese la edad de jugador"))
                break
            except ValueError:
                print("DEBE INGRESAR UN NUMERO ENTERO")
                pass

        team=input("ingrese el equipo del jugador ")
        player=Player(name, age, team)
        players.append(player)

        # Store the player list in the database
        Database.setPlayers(players)

        print(input("presione cualquier tecla para continuar"))

    elif select == "imprimir jugadores" or select == "2":
        system("cls")
        table=[]
        for jugador in (players):
            table.append([jugador.name.capitalize(),
                         jugador.age, jugador.team.capitalize()])

        print(tabulate(table, headers=[
              "NAME", "AGE", "TEAM"], tablefmt="grid"))

        print(input("presione cualquier tecla para regresar"))

    elif select =="salir del programa" or select == "3":
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
