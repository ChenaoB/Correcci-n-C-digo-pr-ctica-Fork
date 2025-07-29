import math

def c(r, h):
    return math.pi * r * r * h

def v(l, a, h):
    return l * a * h

def cubo(a):
    return a ** 3

def principal():
    print("🧮 Cálculo de Volúmenes 🧮")

    try:
        r = float(input("Ingresa el radio del cilindro: "))
        h = float(input("Ingresa la altura del cilindro: "))
        print('🔸 El volumen del cilindro es:', round(c(r, h), 2))

        l = float(input("\nIngresa el largo del prisma rectangular: "))
        a = float(input("Ingresa el ancho del prisma rectangular: "))
        h2 = float(input("Ingresa la altura del prisma rectangular: "))
        print('🔹 El volumen del prisma rectangular es:', round(v(l, a, h2), 2))

        a2 = float(input("\nIngresa el lado del cubo: "))
        print('🔺 El volumen del cubo es:', round(cubo(a2), 2))

    except ValueError:
        print("⚠️ Entrada inválida. Por favor, ingresa números válidos.")

# Ejecutar programa
principal()