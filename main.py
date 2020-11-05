# system libraries
import sys
from os import system
from tabulate import tabulate
# database import
from database.playerD import PlayerD
from database.teamD import TeamD
from database.database import Database
# command import
from commands.help.help import help
from commands.add.add import add
from commands.print.print import Print
from commands.delete.delete import delete
from commands.edit.edit import edit
# other import
from utils.tables import *

if len(sys.argv) <= 2:
    print("Introcuzca un comando y un sub-comando!")

elif sys.argv[1] == "help":
    help()

elif sys.argv[1] == "add":
    add(sys.argv)

elif sys.argv[1] == "print":
    Print()

elif sys.argv[1] == "delete":
    delete()

elif sys.argv[1] == "edit":
    edit()

else: 
    print(f"Error: parametro {sys.argv[1:]} no encontrado, puede introcir <<help>> y mirar los comandos!")
