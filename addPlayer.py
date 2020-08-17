from player import Player
from database import Database
from print_teams import prinTeam


def addPlayer(players):
   
    name = str(input("Ingrese el nombre del jugador "))
    age = 0
    while True:

        try:
            age = int(input("Ingrese la edad de jugador "))
            break
        except ValueError:
            print("DEBE INGRESAR UN NUMERO ENTERO \n")
            
    # call prin_teams function 
    prinTeam()
    team = input("Escriba el nombre del equipo al que quiere que pertenezca el jugador ")
    
    player = Player(name, age, team)
    players.append(player)# Stores the list of players in the database
