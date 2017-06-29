def salud():
    print("Hola, mi nombre es Maria Eugenia Hernandez..")

def saludar(quien, edad="algunos "):
    print("Hola %s de %s anios. Mi nombre es Maria Eugenia Hernandez.." % (quien, edad))

def pintar_linea (long, simbolo):
    line=""
    for s in range(long):
        line += simbolo
    print (line)

def pintar_linea2 (long, simbolo="*"):
    print (simbolo*long)
    

def crear_piramide(long, simbolo):
    for l in range(long):
        pintar_linea(l+1, simbolo)

def crear_piramidei(long, simbolo):
    for l in range(long, 0, -1):
        pintar_linea(l, simbolo)

def crear_piramidota(long, simbolo="+"):
    crear_piramide(long+1, simbolo)
    crear_piramidei(long, simbolo)



def piramide_top(long):
    for i in range(long):
        if i == 0:
            print ("?")
        elif i > 0 and i < long - 1:
            print ("+" * i + "?")
        elif i == long:
            print ("+" * i + "*")

def piramide_bottom(long):
    for i in range(long, 0 , -1):
        if i == 0:
            print ("?")
        elif i > 0 and i < long:
            print ("+" * i + "?")
        elif i == long:
            print ("+" * i + "*")


def piramide_decorada (long, datos):
    def piramide_top(long)
    def piramide_bottom(long)
