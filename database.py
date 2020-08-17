import sqlite3
from player import Player

class Database:

    conn = None
    cursor = None

    @staticmethod
    def connect(name):
        Database.conn = sqlite3.connect(name)
        Database.cursor = Database.conn.cursor()

    @staticmethod
    def getPlayers():

        Database.cursor.execute('SELECT * FROM players')
        players = []

        for name, age, team in Database.cursor.fetchall():
            players.append(Player(name, age, team))

        return players

    @staticmethod
    def setPlayers(players):

        Database.cursor.execute('DELETE FROM players')

        for player in players:
            Database.cursor.execute(
                'INSERT INTO players VALUES (?, ?, ?)',
                (player.name, player.age, player.team)
            )

        Database.conn.commit()

    @staticmethod
    def close():
        Database.cursor.close()
        Database.conn.close()
