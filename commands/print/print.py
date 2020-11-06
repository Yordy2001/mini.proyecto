from commands.print.printPlayer import printPlayer 
from commands.print.printTeam import printTeam

def Print(arg):

    if  arg == "player":
        printPlayer()

    elif arg == "team":
        printTeam()
