from utils.promptNumber import promptNumber
from commands.print.print import printPlayer
from commands.print.print import printTeam

def deletePlayer(players):

    # print the players so the user can choose which one to change
    printPlayer(players)

    positions = promptNumber(
            "Introduzca la posicion del jugador a eliminar: ")

    player = players[positions]

    delete = input("{}, es el jugador que desea eliminar? ".format(
        player.name.capitalize()))

    if delete == "si":
        del players[positions]

    elif delete == "no":
            print("Revise la posicion")
            deletePlayer(players)  # return de delete player function

    else:
        print("Debe introducir SI o NO ")
        deletePlayer(players)  # return de delete player function

def deleteTeam(teams):

        # print the players so the user can choose which one to change
        printTeam(teams)

        # get the position from the get position function
        positions = promptNumber("introduzca la posicion del equipo a eliminar: ")

        team = teams[positions]

        delete = input("{}, es el equipo que desea eliminar? ".format(team.name))

        if delete == "si":
            del teams[positions]

        elif delete == "no":
            print("Revise la posicion")
            deleteTeam(teams)  # return de delete player function

        else:
            print("Debe introducir SI o NO ")
            deleteTeam(teams)  # return de delete player function

