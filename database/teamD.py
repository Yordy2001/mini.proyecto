from models.team import Team
import sqlite3

class TeamD:
 
    conn = None
    cursor = None
    
    @staticmethod
    def connect(name):
        TeamD.conn = sqlite3.connect(name)
        TeamD.cursor = TeamD.conn.cursor()

    @staticmethod
    def getTeams():

        TeamD.cursor.execute('SELECT * FROM teams')
        teams = []

        for id, name, championships, world_series in TeamD.cursor.fetchall():
            teams.append(Team(id, name, championships, world_series))    

        return teams

    @staticmethod
    def setTeams(teams):
        
        TeamD.cursor.execute('DELETE FROM teams')

        for team in teams:
            TeamD.cursor.execute(
                'INSERT INTO teams VALUES (?, ?, ?, ?)',
                (team.id, team.name, team.championships, team.world_series)
            )

        TeamD.conn.commit()
