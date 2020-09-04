from player import Player
from database import Database
from print_teams import prinTeam
from createId import createId

def addPlayer(players, teams):
   
    id = createId()

    name = str(input("Ingrese el nombre del jugador: "))
    age = 0
    while True:

        try:
            age = int(input("Ingrese la edad del jugador: "))
            break
        except ValueError:
            print("DEBE INGRESAR UN NUMERO ENTERO \n")            

    print("Ingrese la posicion del equipo al que quiere que pertenezca el jugador! \n")
    
    # call prin_teams function 
    prinTeam(teams)

    position = -1
    while True:
        try:
            positions = int(input("position-> "))
            team_id = teams[positions].id
            break
        except Exception:
            print("revice la posicion!!")

    player = Player(id, name, age, team_id)
    players.append(player)# Stores the list of players in the database
