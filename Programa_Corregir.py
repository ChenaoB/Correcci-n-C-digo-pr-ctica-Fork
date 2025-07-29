def vol_cilindro(radio, altura):
    return 3.14 * radio * radio * altura


def vol_prisma(largo, ancho, altura):
    return largo * ancho * altura


def vol_cubo(lado):
    return lado ** 3


def calcular():
    radio = 5
    altura_cil = 10
    print('El volumen del cilindro es:', vol_cilindro(radio, altura_cil))

    largo = 6
    ancho = 4
    altura_prisma = 2
    print('El volumen del prisma rectangular es:', vol_prisma(largo, ancho, altura_prisma))

    lado_cubo = 3
    print('El volumen del cubo es:', vol_cubo(lado_cubo))


calcular()