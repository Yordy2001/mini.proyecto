from models.player import Player

class PlayerD:

    def  __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def getPlayers(self):
        self.cursor.execute('SELECT * FROM players')

        players = []

        for id, name, age, team_id in self.cursor.fetchall():
            players.append(Player(id, name, age, team_id))

        return players

    def addPlayers(self, players):

        for player in players:
            self.cursor.execute(
                'INSERT INTO players VALUES (?, ?, ?, ?)',
                (player.id, player.name, player.age, player.team_id)
            )

        self.conn.commit()
