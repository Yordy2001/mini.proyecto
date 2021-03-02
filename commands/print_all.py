from commands.print.printPlayers import printPlayers
from commands.print.printTeams import printTeams

def Print(arg):

    if  arg == "players":
        printPlayers()

    elif arg == "teams":
        printTeams()
