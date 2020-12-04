from models.team import Team
import sqlite3

class TeamD:

    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def tableT(self):
    
        self.cursor.execute('CREATE TABLE IF NOT EXISTS teams(id  INTEGER PRIMARY KEY, name TEXT, championships INTEGER, world_seriesINTEGER,)')

        self.conn.commit()

    def getTeams(self):
        self.cursor.execute('SELECT * FROM teams')
        teams = []

        for id, name, championships, world_series in self.cursor.fetchall():
            teams.append(Team(id, name, championships, world_series))    

        return teams

    def setTeams(self, teams):

        self.cursor.execute('DELETE FROM teams')

        for team in teams:
            self.cursor.execute(
                'INSERT INTO teams VALUES (?, ?, ?, ?)',
                (team.id, team.name, team.championships, team.world_series)
            )

        self.conn.commit()

    def addTeam(self, team):

        self.cursor.execute(
            'INSERT INTO teams VALUES (?, ?, ?, ?)',
                (team.id, team.name, team.championships, team.world_series)
            )

        self.conn.commit()

    def updateTeam(self, team):

        self.cursor.execute(
            'UPDATE teams SET name = ?, championships = ?, world_series = ? WHERE id = ?',
            (team.name, team.championships, team.world_series, team.id)
        )

        self.conn.commit()

    def deletePlayer(self, team):
    
        self.cursor.execute(
            'DELETE  FROM teams WHERE id = ?',
            ([team.id]) 
        )

        self.conn.commit()
