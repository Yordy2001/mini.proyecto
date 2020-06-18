from os import system
from tabulate import tabulate
from jugador import Jugador

jugadores = []

system("cls")
print("MAJOR LENGUAJE BASEBALL\n")

while True:

    print("Seleccione una opcion:\n")
    print("1.AGREGAR JUGADOR\n2.IMPRIMIR JUGADORES\n3.CERRAR PROGRAMA\n ")
    elija = input("Seleccione la opción deseada: ")

    if elija == "agregar jugador":
        system("cls")
        jugador = Jugador()
        jugador.nombre = input("ingrese el nombre del jugador ")

        while True:

            try:
                jugador.edad = int(input("ingrese la edad de jugador "))
                break
            except ValueError:
                print("DEBE INGRESAR UN NUMERO ENTERO")
                pass

        jugador.equipo = input("ingrese el equipo del jugador  ")
        jugadores.append(jugador)

    elif elija == "imprimir jugadores":
        system("cls")
        tabla = []
        for jugador in (jugadores):
            tabla.append(jugador.nombre)

        print(tabulate(tabla, headers=[
              "nombre", "edad", "equipo"], tablefmt="grid"))

    elif elija == "cerrar programa":
        system("cls")
        print("bye")
        break

    else:
        system("cls")
        print("!REVISE SU ESCRITURA!")
