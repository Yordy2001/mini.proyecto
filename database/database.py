import sqlite3
from database.playerD import PlayerD
from database.teamD import TeamD
from models.player import Player
from models.team import Team

class Database:

    conn = None
    cursor = None
    instancia = None
    player = PlayerD
    team = TeamD
    
    @staticmethod
    def connect(name):
        Database.conn = sqlite3.connect(name)
        Database.cursor = Database.conn.cursor()

    @staticmethod
    def crearInstancia(name):

        if Database.instancia is not None:
            return Database.instancia
        else:
            Database.instancia = Database(name)
            return Database.instancia

    def __init__(self, name):
        self.name = name

    def close(self):
        Database.cursor.close()
        Database.conn.close()
