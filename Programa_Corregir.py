def Volumen_cilindro(r, h):
    return 3.14 * (r ** 2) * h


def Volumen_prisma(l, a, h2):
    return l * a * h2


def Volumen_cubo(lado):
    return lado * lado * lado


def principal():
    r = 5
    h = 10
    print('El volumen del cilindro es:', Volumen_cilindro(r, h))
    l = 6
    a = 4
    h2 = 2
    print('volumen del prisma rectangular es: ', Volumen_prisma(l, a, h2))
    lado = 3
    print('El volumen del cubo es: ', Volumen_cubo(a))


principal()