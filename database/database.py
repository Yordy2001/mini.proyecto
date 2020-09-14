import sqlite3
from database.player import Player
from database.team import Team

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

        for id, name, age, team_id in Database.cursor.fetchall():
            players.append(Player(id, name, age, team_id))

        return players

    @staticmethod
    def getTeams():

        Database.cursor.execute('SELECT * FROM teams')
        teams = []

        for id, name, championships, world_series in Database.cursor.fetchall():
            teams.append(Team(id, name, championships, world_series))    

        return teams; 

    @staticmethod
    def setPlayers(players):

        Database.cursor.execute('DELETE FROM players')

        for player in players:
            Database.cursor.execute(
                'INSERT INTO players VALUES (?, ?, ?, ?)',
                (player.id, player.name, player.age, player.team_id)
            )

        Database.conn.commit()

    @staticmethod
    def setTeams(teams):

        Database.cursor.execute('DELETE FROM teams')

        for team in teams:
            Database.cursor.execute(
                'INSERT INTO teams VALUES (?, ?, ?, ?)',
                (team.id, team.name, team.championships, team.world_series)
            )

        Database.conn.commit()

    @staticmethod
    def close():
        Database.cursor.close()
        Database.conn.close()
