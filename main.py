import sys
from argparse import ArgumentParser
from database.playerD import PlayerD
from database.teamD import TeamD
from database.database import Database
from commands.print.print_players_team import PlayerTeam
from commands.add.addPlayer import addPlayer
from commands.print.printPlayers import printPlayers
from commands.add.addTeam import addTeam
from commands.print.printTeams import printTeams
from commands.delete.deletePlayer import deletePlayer
from commands.delete.deleteTeam import deleteTeam

parser = ArgumentParser()
parser.add_argument('--add',
                    type=str,
                    choices=['player', 'team'],
                    help="agregar players or teams")

parser.add_argument('--print',
                    type=str,
                    choices=['players', 'teams'],
                    help="Iprimir players or teams")

parser.add_argument('--printPT',
                    choices=["tigueres del licey", "TL",
                             "aguilas cibaeñas", "AC",
                             "leones del escogido", "LE",
                             "estrellas orinetales", "EO",
                             "toros del este", "TE",
                             "gigantes del cibao", "GC"],
                    type=str,
                    nargs='+',
                    help="Iprime las 2 tablas en juntas")

parser.add_argument('--delete',   type=str,
                    choices=['player', 'team'],
                    help="Eliminar players or teams")

parser.add_argument('--update',
                    type=str,
                    choices=['player', 'team'],
                    help="actualiza players or teams")

args = parser.parse_args()

if args.add == "player":
    addPlayer()

elif args.add == "team":
    addPlayer()

elif args.print == "players":
    printPlayers()

elif args.print == "teams":
    printTeams()

elif args.delete == "player":
    deletePlayer()

elif args.delete == "team":
    deleteTeam()

elif args.printPT != None:
    PlayerTeam(args.printPT)
