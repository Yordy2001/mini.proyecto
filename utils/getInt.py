def getInt():

    num = 0
    while True:
        try:
            num = int(input(" "))
            return num
        except ValueError:
            print(" DEBE INTRODUCIR UN NUMERO ENTERO!! ")
