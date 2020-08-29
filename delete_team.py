from print_teams import *
    
def delete_team():

    # print the players so the user can choose which one to change
    prinTeam()

    positions = -1
    while True:

        try:
            positions = int(
                input("introduzca la posicion del jugador a eliminar "))
            break
        except Exception:
            print("debe introducir un numero de la posicion")

    delete = input("{} es el jugador que desea eliminar? ".format(equipos[positions][0]))

    if delete == "si":
        del equipos[positions]

    elif delete == "no":
        print("revise la posicion")
        delete_team()  # return de delete player function
        
    else:
        print("debe introducir SI o NO ")
        delete_team()  # return de delete player function
