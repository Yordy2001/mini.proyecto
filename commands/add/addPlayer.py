from commands.print.printTeams import printTeams
from database.database import Database
from models.player import Player
from models.team import Team
from utils.createId import createId
from utils.promptNumber import promptNumber

# Open the connection to the database
database = Database.connect('mlb.db')

def addPlayer():   

    teams = database.team.getTeams()

    id = createId()

    name = str(input("Ingrese el nombre del jugador: "))

    age = promptNumber("Introduce la edad del jugador: ")

    # call prin_teams function
    printTeams()

    positions = promptNumber(
        "Ingrese la posicion del equipo al que quiere que pertenezca el jugador: ")
    team_id = teams[positions].id
    print("    Jugador agregado Exitosamente!  ")

    player = Player(id, name, age, team_id)

    # Stores the list of players in the database
    database.player.addPlayer(player)
