from database.database import Database
from models.player import Player
from models.team import Team
from commands.print.print import printTeam
from utils.createId import createId
from utils.promptNumber import promptNumber

# Open the connection to the database
database = Database.connect('mlb.db')

def addPlayer():   

    teams = database.team.getTeams()
    players = database.player.getPlayers()

    id = createId()

    name = str(input("Ingrese el nombre del jugador: "))

    age = promptNumber("Introduce la edad del jugador: ")

    # call prin_teams function
    printTeam()

    positions = promptNumber(
        "Ingrese la posicion del equipo al que quiere que pertenezca el jugador: ")
    team_id = teams[positions].id

    player = Player(id, name, age, team_id)

    # Stores the list of players in the database
    players.append(player)
    
    database.player.setPlayers(players)
