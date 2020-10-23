from models.team import Team
import sqlite3

class TeamD:

    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

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
