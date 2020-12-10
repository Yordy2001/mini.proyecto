from models.player import Player

class PlayerD:

    def  __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def createTable(self):

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id TEXT,
                name TEXT,
                age INTEGER,
                team_id TEXT
                )
            ''')

        self.conn.commit()

    def getPlayers(self):
        self.cursor.execute('SELECT * FROM players')

        players = []

        for id, name, age, team_id in self.cursor.fetchall():
            players.append(Player(id, name, age, team_id))

        return players

    def setPlayers(self, players):

        self.cursor.execute('DELETE FROM players')

        for player in players:
            self.cursor.execute(
                'INSERT INTO players VALUES (?, ?, ?, ?)',
                (player.id, player.name, player.age, player.team_id)
            )
        self.conn.commit()

    def addPlayer(self, player):

        self.cursor.execute(
            'INSERT INTO players VALUES (?, ?, ?, ?)',
            (player.id, player.name, player.age, player.team_id)
        )

        self.conn.commit()

    def updatePlayer(self, player):

        self.cursor.execute(
            'UPDATE players SET name = ?, age = ?, team_id = ? WHERE id = ?',
            (player.name, player.age, player.team_id, player.id)
        )

        self.conn.commit()

    def deletePlayer(self, player):

        self.cursor.execute(
            'DELETE FROM players WHERE id = ?',
            ([player.id]) 
        )

        self.conn.commit()
