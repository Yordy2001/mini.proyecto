class Table:
    def __init__(self):

        table = print("""
        x------------------------------------------------------------x
        |           "MAJOR LENGUAJE BASEBALL"                        | 
        |                                                            |
        |   "SELECCIONE UNA OPCION MARCANDO EL NUMERO DE SU POSICION:|
        |                                                            |     
        |   1.PLAYER                2.TEAM              3.SALIR      |
        |                                                            |
        |                                                            |
        x------------------------------------------------------------x""")

    @staticmethod
    def TablePlayer():

        print("""
        x------------------------------------------------------------x
        |  "SELECCIONE UNA OPCION MARCANDO EL NUMERO DE SU POSICION: |
        |                                                            |     
        |   1.Add Player                                             |
        |   2.Print Player                                           |
        |   3.Delete Player                                          |  
        |   4.Edit Player                                            |
        x------------------------------------------------------------x""")

    @staticmethod
    def  TableTeam():
        print("""
        x------------------------------------------------------------x
        |  "SELECCIONE UNA OPCION MARCANDO EL NUMERO DE SU POSICION: |
        |                                                            |     
        |   1.Add Team                                               |
        |   2.Print Team                                             |
        |   3.Delete Team                                            |  
        |                                                            |
        x------------------------------------------------------------x""")
 