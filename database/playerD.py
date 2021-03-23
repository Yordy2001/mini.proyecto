from models.player import Player


class PlayerD:

    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def createTable(self):

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id TEXT,
                name TEXT,
                age INTEGER,
                team_id TEXT,
                avg INTEGER
                )
            ''')

        self.conn.commit()

    def getPlayers(self):
        self.cursor.execute('SELECT * FROM players')

        players = []

        for id, name, age, team_id, avg in self.cursor.fetchall():
            players.append(Player(id, name, age, team_id, avg))

        return players

    def setPlayers(self, players):

        self.cursor.execute('DELETE FROM players')

        for player in players:
            self.cursor.execute(
                'INSERT INTO players VALUES (?, ?, ?, ?, ?)',
                (player.id, player.name, player.age, player.team_id, player.avg)
            )
        self.conn.commit()

    def getPLayersT(self, team_name):

        self.cursor.execute(
            '''
            SELECT
                players.name,
                players.age,
                teams.name AS teamName,
                teams.championships,
                teams.world_series
            FROM players
            INNER JOIN teams ON players.team_id = teams.id
            WHERE teams.name = ?
            ''',
            (str(team_name[0]),)
        )

        playersT = []

        for name, age, teamName, championships, world_series in self.cursor.fetchall():
            playersT.append(
                (name.title(), age, teamName.title(), championships, world_series))

        return playersT

    def addPlayer(self, player):

        self.cursor.execute(
            'INSERT INTO players VALUES (?, ?, ?, ?, ?)',
            (player.id, player.name, player.age, player.team_id, player.avg)
        )

        self.conn.commit()

    def updatePlayer(self, player):

        self.cursor.execute(
            'UPDATE players SET name = ?, age = ?, team_id = ?, avg WHERE id = ?',
            (player.name, player.age, player.team_id, player.avg, player.id)
        )

        self.conn.commit()

    def deletePlayer(self, player):

        self.cursor.execute(
            'DELETE FROM players WHERE id = ?',
            ([player.id])
        )

        self.conn.commit()
