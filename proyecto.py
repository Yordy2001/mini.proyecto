lista = []
def MLB(lista):
    print("IMPRIMIR JUGADORES,  AGREGAR JUGADORES")
    elija = input("seleccione la opcion deseada: ")
    if elija == "imprimir jugadores":
            return lista
    if elija == "agregar jugadores":
        class jugadores:
            nombre = input("ingrese nombre del jugador: ")
            edad = int(input("ingrese edad  del jugador: "))
            equipo = input("ingrese el equipo del jugador: ")

        pelota_invernal = jugadores()
        print(f"el nombre del jugador es {pelota_invernal.nombre} tiene {pelota_invernal.edad} años y juega con {pelota_invernal.equipo}")
        lista.append(pelota_invernal)    
    else:
            print("debe elegir una opcion progrmada")
            return MLB(lista)
print(MLB(lista))











