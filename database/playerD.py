import sqlite3
from models.player import Player

class PlayerD:
    
    conn = None
    cursor = None
    
    @staticmethod
    def connect(name):
        PlayerD.conn = sqlite3.connect(name)
        PlayerD.cursor = PlayerD.conn.cursor()

    @staticmethod
    def getPlayers():
        PlayerD.cursor.execute('SELECT * FROM players')
        players = []

        for id, name, age, team_id in PlayerD.cursor.fetchall():
            players.append(Player(id, name, age, team_id))

        return players

    @staticmethod
    def setPlayers(players):

        PlayerD.cursor.execute('DELETE FROM players')

        for player in players:
            PlayerD.cursor.execute(
                'INSERT INTO players VALUES (?, ?, ?, ?)',
                (player.id, player.name, player.age, player.team_id)
            )

        PlayerD.conn.commit()
