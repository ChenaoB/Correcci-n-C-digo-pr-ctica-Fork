def volumen_cilindro (radio_cilindro, altura_cilindro):
    # Calcula el Volumen del Cilindro dado el Radio y la Altura
    return 3.14 * radio_cilindro * radio_cilindro * altura_cilindro


def volumen_prisma_rectangular (largo_prisma, ancho_prisma, altura_prisma):
    # Calcula el Volumen del Prisma Rectangular dado el Largo, Ancho y Altura
    return largo_prisma * ancho_prisma * altura_prisma


def volumen_cubo(lado_cubo):
    # Calcula el Volumen de un Cubo dado su Lado
    return lado_cubo * lado_cubo * lado_cubo


def principal():
    # Funcion principal para diferentes Volumenes
    
    radio_cilindro = float(input ('Ingrese el radio del Cilindro: '))
    altura_cilindro = float(input ('Ingrese la altura del Cilindro: '))
    print('El volumen del cilindro es: ', volumen_cilindro(radio_cilindro, altura_cilindro))
    lado_prisma = float(input ('Ingrese el lado del Prisma: '))
    ancho_prisma = float(input ('Ingrese el ancho del Prisma: '))
    altura_prisma = float(input ('Ingrese la altura del Prisma: '))
    print('El volumen del prisma rectangular es: ', volumen_prisma_rectangular(lado_prisma , ancho_prisma, altura_prisma))
    lado_cubo = float(input ('Ingrese el lado del Cubo: '))
    print('El volumen del cubo es: ', volumen_cubo(lado_cubo))
#Calculo volumenes
principal()