class Automovil(object):

    def __init__(self, marca, modelo, anio, Motor):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.Motor = Motor

    def arrancar():
        print "ruuuuuuuuuuuuuuum"

    def acelerar():
        print "trrrrrrrrrrrrrrrrrr"

    def frenar():
        print "crrrrrrrrrrrrrrrr"

class Motor (object):

        def __init__(self, potencia, numero, capacidad):
        self.potencia = potencia
        self.numero = numero
        self.capacidad = capacidad

    def encender():
        print "mmmmmmmmmmmmmmmmmm"

    def acelerar():
        print "rmmmmmmmmmmmmmmmmm"
