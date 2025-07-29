#Ejercicio corregido
import math

def volumen_cilindro(radio, altura):
    """Calcula el volumen de un cilindro."""
    return math.pi * radio * radio * altura

def volumen_prisma_rectangular(largo, ancho, altura):
    """Calcula el volumen de un prisma rectangular."""
    return largo * ancho * altura

def volumen_cubo(lado):
    """Calcula el volumen de un cubo."""
    return lado * lado * lado

def principal():
    # Cálculo del volumen del cilindro
    radio_cilindro = 5
    altura_cilindro = 10
    print('El volumen del cilindro es:', volumen_cilindro(radio_cilindro, altura_cilindro))

    # Cálculo del volumen del prisma rectangular
    largo_prisma = 6
    ancho_prisma = 4
    altura_prisma = 2
    print('El volumen del prisma rectangular es:', volumen_prisma_rectangular(largo_prisma, ancho_prisma, altura_prisma))

    # Cálculo del volumen del cubo
    lado_cubo = 3
    print('El volumen del cubo es:', volumen_cubo(lado_cubo))

# Ejecución de la función principal para calcular volúmenes
if __name__ == "__main__":
    principal()