from .PuntoDeVenta import *

class Local(PuntoDeVenta):
    def __init__(self):
        self.id = 0
        self.nombre = ""

    def setId(self, id):
        self.id = id
    def getId(self):
        return self.id

    def setNombre(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre    