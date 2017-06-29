class Bebida(object):

    def __init__(self, marca, nombre, contenido):
        self.marca = marca
        self.nombre = nombre
        self.contenido = contenido

    def ser_consumida():
        print "glup"

    def ser_abierta():
        print "tsssss"

    def ser_cerrada():
        print "*silence*"

class Refresco(Bebida):

        def __init__(self, sabor):
        self.sabor = sabor

    def perder_gas():
        print "ssssss"

    def explotar():
        print "pum"

class Bebida_Alcoholica(Bebida):

        def __init__():

    def emborrachar():
        print "XX"

class Cerveza(Bebida):
    
    def quemarse():
        print "bowchibowow"
