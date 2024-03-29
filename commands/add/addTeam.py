from database.database import Database
from models.player import Player
from models.team import Team
from commands.print.printTeams import printTeams
from utils.createId import createId
from utils.promptNumber import promptNumber

# Open the connection to the database
database = Database.connect('mlb.db')

def addTeam():

    id = createId()

    name = input("Ingrese el nombre del equipo: ")

    championships = promptNumber(
        "Ingrese la cantidad de coronas que ha ganado: ")

    world_series = promptNumber(
        "Ingrese la cantidad  de series mundiales que ha ganado: ")
    print("  Equipo agregado exitosamente!")

    team = Team(id, name, championships, world_series)
    
    database.team.addTeam(team)
