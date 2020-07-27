from player import Player
from database import Database

def addPlayer(players):
   
    name = str(input("ingrese el nombre del jugador "))
    age = 0
    while True:

        try:
            age = int(input("ingrese la edad de jugador "))
            break
        except ValueError:
            print("DEBE INGRESAR UN NUMERO ENTERO")
            pass

    team = str(input("ingrese el equipo del jugador "))
    player = Player(name, age, team)
    players.append(player)# Stores the list of players in the database


   

