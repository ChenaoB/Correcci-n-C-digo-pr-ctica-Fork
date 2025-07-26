def VolumenCilindro(radioC, alturaC):
    """
    Función que calcula el volumen de un cilindro dada su altura y radio
        Parámetros Entrada:
          radioC: Radio del cilindro (flotante o entero)
          alturaC: Altura del cilindro (flotante o entero)
        
        Salidas: Retorna el volumen del cilindro 
    """
    pi = 3.1416
    return pi * (radioC ** 2) * alturaC


def VolumenPrimas(Largo, Ancho, Altura):
    """
    Función que calcula el volumen de un prisma rectangular dada su largo, ancho y altura
        Parámetros Entrada:
          Largo: Longitud del largo del prisma (flotante o entero)
          Ancho: Longitud del ancho del prisma (flotante o entero)
          Altura: Longitud de la altura del prisma (flotante o entero)
        
        Salidas: Retorna el volumen del prisma
    """
    return Largo * Ancho * Altura


def VolumenCubo(lado):
    """
    Función que calcula el volumen de un cubo dada la longitud de su lado
        Parámetros Entrada:
          lado : Longitud del lado del cubo
        
        Salidas: Retorna el volumen del cubo 
    """
    return lado ** 3


def principal():
    """
    Función que ejecuta el llamado de las funciones principales de los cálculos 
    de los volumenes
    """

    RadiusC = 5
    AlturaC = 10
    print('El volumen del cilindro es:', VolumenCilindro(RadiusC, AlturaC))

    LargoP = 6
    AnchoP = 4
    AlturaP = 2
    print('El volumen del prisma rectangular es:', VolumenPrimas(LargoP, AnchoP, AlturaP))

    LadoC = 3
    print('El volumen del cubo es:', VolumenCubo(LadoC))


principal()

