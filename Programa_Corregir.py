import math

def volumen_cilindro(radio, altura):
    """Calcula el volumen de un cilindro."""
    return math.pi * radio**2 * altura

def volumen_prisma_rectangular(longitud, ancho, altura):
    """Calcula el volumen de un prisma rectangular."""
    return longitud * ancho * altura

def volumen_cubo(lado):
    """Calcula el volumen de un cubo."""
    return lado ** 3

def principal():
    # Volumen del cilindro
    radio = 5
    altura_cilindro = 10
    print("El volumen del cilindro es:", volumen_cilindro(radio, altura_cilindro))

    # Volumen del prisma rectangular
    longitud = 6
    ancho = 4
    altura_prisma = 2
    print("El volumen del prisma rectangular es:", volumen_prisma_rectangular(longitud, ancho, altura_prisma))

    # Volumen del cubo
    lado_cubo = 3
    print("El volumen del cubo es:", volumen_cubo(lado_cubo))

# Cálculo de volúmenes
if __name__ == "__main__":
    principal()
