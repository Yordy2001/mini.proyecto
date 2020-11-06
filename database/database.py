import sqlite3
from database.playerD import PlayerD
from database.teamD import TeamD
from models.player import Player
from models.team import Team

class Database:

    instance = None

    @staticmethod
    def connect(name):

        if Database.instance is not None:
            return Database.instance
        else:
            Database.instance = Database(name)
            return Database.instance

    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect(name)
        self.cursor = self.conn.cursor()
        self.player = PlayerD(self.conn, self.cursor)
        self.team = TeamD(self.conn, self.cursor)

    def close(self):
        self.cursor.close()
        self.conn.close()
