def promptNumber(message):

    num = 0
    while True:
        try:
            num = int(input(message))
            return num
        except ValueError:
            print(" DEBE INTRODUCIR UN NUMERO ENTERO!! ")
