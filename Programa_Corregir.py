

#----------------------------------------------------------------------------------------------
#CORRECION DEL CODIGO:
import numpy as np

# Funcion para calcular el Volumen de un Cilindo


def volumenCilindro(radio, alturaCi):
    pi = np.pi  # define pi como π
    return (
        pi * np.power(radio, 2) * alturaCi
    )  # np.power es funcion de potencia en numpy np.power(base, potencia)


# Funcion para calcilar el Volumen de un prisma rectangular.
def volumenPrisma(largo, ancho, alturaPr):
    return largo * ancho * alturaPr


# Funcion para calcular el volumen de un cubo
def volumenCubo(areaCu):
    return np.power(
        areaCu: 3
    )  # np.power es funcion de potencia en numpy np.power(base, potencia)


# funcion principal que llamas las funciones de los volumenes, y define el valor para las variables
def principal():

    # Definimos el valor del radio y altura del Cilindro, e imprimimos la funcion para calcular el volumen del cilindro
    radioCilindro = 5
    alturaCilindro = 10
    print("El volumen del cilindro es:", volumenCilindro(radioCilindro, alturaCilindro))

    # Definimos el valor del largo, ancho y altura del prisma e imprimos la funcion para calcular el volumen del prisma
    largoPrisma = 6
    anchoPrisma = 4
    alturaPrisma = 2
    print(
        "volumen del prisma rectangular es:",
        volumenPrisma(largoPrisma, anchoPrisma, alturaPrisma),
    )

    # Definimos el valor del area del cubo e imprimos la funcion para calcular el area del cubo.
    areaCubo = 3
    print("El volumen del cubo es:", volumenCubo(areaCubo))


# Calculo volumenes
principal()  # llama la funcion principal que almacena todos los volumenes.

