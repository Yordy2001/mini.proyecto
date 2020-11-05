from database.database import Database
from utils.promptNumber import promptNumber
from commands.print.print import printPlayer

database = Database.connect('mlb.db')

def deletePlayer():

    players = database.player.getPlayers()
    # print the players so the user can choose which one to change
    printPlayer()

    positions = promptNumber(
            "Introduzca la posicion del jugador a eliminar: ")

    player = players[positions]

    delete = input("{}, es el jugador que desea eliminar? ".format(
        player.name.capitalize()))

    if delete == "si":
        del players[positions]

    elif delete == "no":
        print("Revise la posicion")
        deletePlayer()  # return de delete player function

    else:
        print("Debe introducir SI o NO ")
        deletePlayer()  # return de delete player function
    database.player.setPlayers(players)
