from database import Database
from print_teams import prinTeam


def delete_team(teams):

    # # print the players so the user can choose which one to change
    prinTeam(teams)

    positions = -1
    while True:

        try:
            positions = int(
                input("introduzca la posicion del equipo a eliminar "))
            team = teams[positions]
            break
        except Exception:
            print("debe introducir un numero de la posicion")

    delete = input("{} es el equipo que desea eliminar? ".format(team.name))

    if delete == "si":
        del teams[positions]

    elif delete == "no":
        print("revise la posicion")
        delete_team(teams)  # return de delete player function
        
    else:
        print("debe introducir SI o NO ")
        delete_team(teams)  # return de delete player function
