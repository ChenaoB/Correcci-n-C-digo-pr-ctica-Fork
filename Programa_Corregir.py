import math 

def Volumen_cilindro(radio , altura):
    return math.pi * (radio ** 2) * altura


def Volumen_prisma(largo , ancho , altura):
    return largo * ancho * altura


def Volumen_cubo(lado):
    return math.pow(lado , 3)


def principal():
    radio =  5
    altura  =  10
    print('El volumen del cilindro es:', Volumen_cilindro(radio , altura ))
    
    largo = 6
    ancho = 4
    altura2 = 2
    print('El volumen del prisma rectangular es: ', Volumen_prisma(largo , ancho , altura2))
    
    lado = 3
    print('El volumen del cubo es: ', Volumen_cubo(lado))


principal()