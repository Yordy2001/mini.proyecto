
from os import system
from tabulate import tabulate

class Jugador:
    nombre = []
    edad = []
    equipo = []


lista = []
def MLB():

    system("cls")
    print("MAJOR LENGUAJE BASEBALL\n")

    count = 0
    while True:

        print("Seleccione una opcion:\n")
        print("1.AGREGAR JUGADOR\n2.IMPRIMIR JUGADORES\n3.CERRAR PROGRAMA\n ")
        elija = input("Seleccione la opción deseada: ")

        if elija == "agregar jugador":
            system("cls")
            jugador = Jugador()
            jugador.nombre.append(input("ingrese el nombre del jugador "))

            while True:

                try:
                    jugador.edad.append(int(input(f"ingrese la edad de {jugador.nombre[count]} ")))
                    break
                except ValueError:
                    print("debe ingresar un numero entero")
                    pass

            jugador.equipo.append(input(f"ingrese el equipo de {jugador.nombre[count]} "))
            count +=1
            
            print (input("presione enter tecla para continuar"))
            return MLB()

        if elija == "imprimir jugadores":
            system("cls")

            for i in range(len(Jugador.nombre)):
                lista.append([Jugador.nombre[i].capitalize(),Jugador.edad[i],Jugador.equipo[i].capitalize()])

            print(tabulate(lista,headers=["nombre","edad","equipo"],tablefmt="grid"))

            print(input("presione la tecla enter para continuar"))
            return MLB()

        if elija == "cerrar programa":
            system("cls")
            print("bye")
            break

        else:
            system("cls")
            print("!REVISE SU ESCRITURA!")
            return MLB()

MLB()






