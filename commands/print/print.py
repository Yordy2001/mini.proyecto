import sys
from commands.print.printPlayer import printPlayer 
from commands.print.printTeam import printTeam

def Print():

    if sys.argv[2] == "player":
        printPlayer()

    elif sys.argv[2] == "team":
        printTeam()
