from database.database import Database
from commands.print.print import printPlayer
from utils.promptNumber import promptNumber

database = Database.connect('mlb.db')

def editPlayer():

    players = database.player.getPlayers()

    # print all players
    printPlayer()

    positions = promptNumber(
         "Introduzca la posición del jugador a editar: ")
    player = players[positions]

    ask = input(
        "{} Éste es el jugador que desea editar ? ".format(
        player.name))

    if ask == "si":

        name = input("Edita el nombre {} ".format(player.name))
        age = input("Edita la edad {} ".format(player.age))
        team_id = input("Edita el equipo {} ".format(player.team_id))

        if name != "":
            player.name = name

        if age != "":
            player.age = age

        if team_id != "":
            player.team_id = team_id

    elif ask == "no":
        print("Revise bien la posición")
        editPlayer()

    else:
        print("Su respuesta debe ser SI o NO")
        editPlayer()
        
    database.player.setPlayers(players)
