from  os import system 
from tabulate import tabulate

class tabla:
    def __init__(self,Nombre,Edad,Equipo):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Equipo =Equipo
            
    def juntar(self):
        return [self.Nombre,self.Edad,self.Equipo]
                    
players = tabla("juan",23,"licey")
players2 = tabla("pedro",43,"toros")
union = [players.juntar(),
        players2.juntar()]
print(tabulate(union,headers=["**Nombre**","**Edad**","**Equipo**"],tablefmt="grid"))



add_jugadores = tabla
lista = []
def MLB(lista):
    system("cls")
    print("MAJOR LENGUAJE BASEBALL\n")
    print("Seleccione una opcion:\n")
    print("1.AGREGAR JUGADORES\n2.IMPRIMIR JUGADORES\n3.CERRAR PROGRAMA\n ")
    elija = input("Seleccione la opción deseada: ")
    add_player = 0
    while True:
        if elija == "imprimir jugadores":
                system("cls")
                return(tabla)
                print(input("presione cualquier tecla para regresar"))
                return MLB(lista)

        if elija == "agregar jugadores" or "1":
            system("cls")
            add_player = add_player + 1
            class jugadores:
                Nombre = str(input("Ingrese nombre del jugador: "))
                    
                # solucion a error de introducir letra en la casilla edad.
                while True:
                    try:
                        Edad = int(input("Ingrese edad  de {}: ".format(Nombre)))
                        break
                    except ValueError:
                        print("DEBE INGRESAR UN NUMERO ENTERO")
                Edad = str(Edad)
                Equipo = str(input(f"Ingrese el equipo de {Nombre}: "))

            pelota_invernal = jugadores()
            print(f"El nombre del jugador es {pelota_invernal.Nombre.capitalize()} tiene {pelota_invernal.Edad} años y juega con {pelota_invernal.Equipo.capitalize()}")
            add_player = pelota_invernal.Nombre
            lista.append(add_player)
            # pelota_invernal.edad.capitalize()
            print(input(" presione cualquier tecla para regresar"))
            return MLB(lista)


        if elija == "cerrar programa":
            system("cls")
            print("bye")
            break
        # si el usuario elige una opcion  que no este returnara la funcion.
        else:
            print("!REVISE SU ESCRITURA!")
            return MLB(lista)

print(MLB(lista))











