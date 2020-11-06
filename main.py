import sys
from database.playerD import PlayerD
from database.teamD import TeamD
from database.database import Database
from commands.help.help import help
from commands.add.add import add
from commands.print.print import Print
from commands.delete.delete import delete
from commands.edit.edit import edit

if len(sys.argv) <= 2:
    print("Introcuzca un comando y un sub-comando!")

elif sys.argv[1] == "help":
    help()

elif sys.argv[1] == "add":
    add(sys.argv[2])

elif sys.argv[1] == "print":
    Print(sys.argv[2])

elif sys.argv[1] == "delete":
    delete(sys.argv[2])

elif sys.argv[1] == "edit":
    edit(sys.argv[2])

else: 
    print(f"Error: parametro {sys.argv[1:]} no encontrado, puede introcir <<help>> y mirar los comandos!")
