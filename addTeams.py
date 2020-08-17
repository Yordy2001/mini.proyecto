from teams import Team


def addTeam():

    all_team = Team()

    all_team.name.append(input("Ingrese el nombre del equipo "))

    while True:
        try:
            all_team.coronas.append(int(input("Ingrese  la canridad de coronas que ha gando ")))
            break
        except ValueError:
            print("Debe ingresar un numero entero")

    while True:
        try:
            all_team.series_mundiales.append(int(input("Ingrese  la cantidad de series mundiales que ha ganado "))) 
            break   
        except ValueError:
            print("Debe introducir un numero entero")    
        