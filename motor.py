class Motor:

  instancia = None

  @staticmethod
  def crearInstancia(name):

      if Motor.instancia is not None:
          return Motor.instancia
      else:
          Motor.instancia = Motor(name)
          return Motor.instancia

  def __init__(self, name):
      self.name = name
