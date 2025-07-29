# pp8: PEP 8 es la guía de estilo oficial para el código Python. Proporciona un conjunto de convenciones y recomendaciones para escribir código Python limpio, legible y consistente. El objetivo de PEP 8 es mejorar la legibilidad del código Python y hacerlo más uniforme, especialmente en entornos colaborativos. 

def cilindro(r, h):
    return 3.14*r*r*h

def volumen_prisma_rectangular(l, a, h):
    return l * a * h

def cubo(a):
    return a ** 3

def principal():
    r = 5
    h = 10
    print('El volumen del cilindro es:', cilindro(r, h))

    l = 6
    a = 4
    h2 = 2
    print('El volumen del prisma rectangular es:', volumen_prisma_rectangular(l, a, h2))

    a2 = 3
    print('El volumen del cubo es:', cubo(a2))

# Calculo de volumenes
principal()