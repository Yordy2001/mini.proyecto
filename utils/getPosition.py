def position():
    
    position = -1
    while True:
        try:
            positions = int(input("position-> "))
            return position
        except Exception:
            print("revice la posicion!!")
