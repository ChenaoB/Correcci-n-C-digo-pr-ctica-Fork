# Función para calcular el volumen de un cilindro
def volumen_cilindro(radio, altura):
    return 3.14 * radio * radio * altura

# Función para calcular el volumen de un prisma rectangular
def volumen_prisma_rectangular(largo, ancho, altura):
    return largo * ancho * altura

# Función para calcular el volumen de un cubo
def volumen_cubo(lado):
    return lado ** 3

# Función principal que ejecuta los cálculos
def calcular_volumenes():
    radio = 5
    altura_cilindro = 10
    print('El volumen del cilindro es:', volumen_cilindro(radio, altura_cilindro))

    largo = 6
    ancho = 4
    altura_prisma = 2
    print('El volumen del prisma rectangular es:', volumen_prisma_rectangular(largo, ancho, altura_prisma))

    lado_cubo = 3
    print('El volumen del cubo es:', volumen_cubo(lado_cubo))

# Ejecutar cálculos
calcular_volumenes()