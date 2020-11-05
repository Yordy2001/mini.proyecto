from database.database import Database
from models.player import Player
from models.team import Team
from commands.print.print import printTeam
from utils.createId import createId
from utils.promptNumber import promptNumber

database = Database.connect('mlb.db')

def addPlayer(teams):   

    players = database.player.getPlayers()

    id = createId()

    name = str(input("Ingrese el nombre del jugador: "))

    age = promptNumber("Introduce la edad del jugador: ")

    # call prin_teams function
    printTeam(teams)

    positions = promptNumber(
        "Ingrese la posicion del equipo al que quiere que pertenezca el jugador: ")
    team_id = teams[positions].id

    player = Player(id, name, age, team_id)

    # Stores the list of players in the database
    players.append(player)

def addTeam(teams):

    id = createId()

    name = input("Ingrese el nombre del equipo ")

    championships = promptNumber(
        "ingrese la cantidad de coronas que ha ganado: ")

    world_series = promptNumber(
        "ingrese la cantidad  de series mundiales que ha ganado: ")

    team = Team(id, name, championships, world_series)
    teams.append(team)  # store the teams in the data base
