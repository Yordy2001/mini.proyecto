from os import system
from database import Database
from tabulate import tabulate
from player import Player

# Abre la conexion con la base de datos
Database.connect('mlb.db');

# Obtiene la lista de jugadores desde la base de datos
jugadores = Database.getPlayers()


system("cls")
print("MAJOR LENGUAJE BASEBALL\n")

while True:

    print("Seleccione una opcion:\n")
    print("1.AGREGAR JUGADOR\n2.IMPRIMIR JUGADORES\n3.CERRAR PROGRAMA\n ")
    elija = input("Seleccione la opción deseada: ")

    if elija == "agregar jugador":
        system("cls")
    
        nombre = str(input("ingrese el nombre del jugador "))
        edad = 0
        while True:

            try:
                edad = int(input("ingrese la edad de jugador "))
                break
            except ValueError:
                print("DEBE INGRESAR UN NUMERO ENTERO")
                pass

        equipo = str(input("ingrese el equipo del jugador "))
        jugador = Player(nombre, edad, equipo)
        jugadores.append(jugador)
                
        # Almacena la lista de jugadores en la base de datos
        Database.setPlayers(jugadores)

        print(input("presione cualquier tecla para continuar"))

    elif elija == "imprimir jugadores":
        system("cls")
        tabla = []
        for jugador in (jugadores):
            tabla.append([jugador.name.capitalize(), jugador.age, jugador.team.capitalize()])

        print(tabulate(tabla, headers=[
              "nombre", "edad", "equipo"], tablefmt="grid"))
        
        print(input("presione cualquier tecla para regresar"))

    elif elija == "cerrar programa":
        system("cls")
        print("bye")
        break

    else:
        system("cls")
        print("!REVISE SU ESCRITURA!")
        
# Almacena la lista de jugadores en la base de datos
Database.setPlayers(jugadores)

# Cierra la conexion con la base de datos
Database.close();
