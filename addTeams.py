from team import Team

equipos = []
def addTeam():

    name_of_team = input("Ingrese el nombre del equipo ")

    while True:
        try:
            champions = int(input("Ingrese  la cantidad de coronas que ha ganado "))
            break
        except ValueError:
            print("Debe ingresar un numero entero")

    while True:
        try:
            mundial_series = int(input("Ingrese  la cantidad de series mundiales que ha ganado ")) 
            break   
        except ValueError:
            print("Debe introducir un numero entero")  

    all_team = Team(name_of_team, champions, mundial_series)
    equipos.append([all_team.name_of_team, all_team.champions, all_team.mundial_series])# store the teams in the list equipos