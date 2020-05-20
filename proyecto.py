from os import system 
from database import Database
from player import Player

# Abre la conexion con la base de datos
Database.connect('mlb.db');

# Obtiene la lista de jugadores desde la base de datos
players = Database.getPlayers()

# Imprime la lista de jugadores
for player in players:
   print(player.name+ ', ' +str(player.age)+ ', ' +player.team)

lista = []
def MLB(lista):
    print("IMPRIMIR JUGADORES,  AGREGAR JUGADORES,CERRA PROGRAMA")
    elija = input("seleccione la opcion deseada: ")
    count = 0
    while True:
        
        if elija == "imprimir jugadores":
                return lista
                print("presione cualquier tecla para regresar")
                return MLB(lista)
            
        system("cls")
        
        if elija == "agregar jugadores":
            count = count + 1
            class jugadores:
                nombre = str(input("Ingrese nombre del jugador: "))
                edad = int(input(f"Ingrese edad  del {nombre}: "))
                equipo = str(input(f"Ingrese el equipo del {nombre}: "))

            pelota_invernal = jugadores()
            print(f"el nombre del jugador es {pelota_invernal.nombre} tiene {pelota_invernal.edad} años y juega con {pelota_invernal.equipo}")
            count = pelota_invernal.nombre
            lista.append(count)
            print("preciones cualquier tecla para continuar")
            return MLB(lista)
            system("cls")
        
        if elija == "cerrar programa":
            print("bye")
            break
        # si el usuario elige una opcion  que no este returnara la funcion.
        else:
            print("DEBE ELGIR UNA OPCION DE LA LISTA!")
            return MLB(lista)
            system("cls")
print(MLB(lista))

# Almacena la lista de jugadores en la base de datos
Database.setPlayers(players)

# Cierra la conexion con la base de datos
Database.close();
