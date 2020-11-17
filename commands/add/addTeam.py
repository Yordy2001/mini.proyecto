from database.database import Database
from models.player import Player
from models.team import Team
from commands.print.print import printTeam
from utils.createId import createId
from utils.promptNumber import promptNumber

# Open the connection to the database
database = Database.connect('mlb.db')

def addTeam():

    id = createId()

    name = input("Ingrese el nombre del equipo ")

    championships = promptNumber(
        "ingrese la cantidad de coronas que ha ganado: ")

    world_series = promptNumber(
        "ingrese la cantidad  de series mundiales que ha ganado: ")

    team = Team(id, name, championships, world_series)
    
    database.team.addTeam(team)
