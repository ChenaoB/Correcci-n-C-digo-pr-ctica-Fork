
""" def c(r,h):return 3.14*r*r*h
def v(l,a,h):return l*a*h
def cubo(a):return a*a*a
def principal():
    r=5
    h=10
    print('El volumen del cilindro es:',c(r,h))
    l=6
    a=4
    h2=2
    print('volumen del prisma rectangular es:',v(l,a,h2))
    a2=3
    print('El volumen del cubo es:',cubo(a2))
#Calculo volumenes
principal()
 """
""" 
 Explicación 
 import : trae módulos (bibliotecas) externas para usar sus funciones como numpy o pandas.
 - numpy as np: biblioteca avanzada para cálculos numéricos
 def: define (crea) una función con nombre y parámetros.
 return: envía de vuelta un valor cuando la función termina.
 -> float: indica el tipo de dato que devuelve la función (anotación de tipo).
 -> None: indica que la función no devuelve nada (solo hace acciones internas).
 __name__ == "__main__": comprueba si el archivo se ejecuta directamente (no importado).

 """




import numpy as np  # Biblioteca para operaciones matemáticas y científicas

# Calcula el volumen de un cilindro: base circular * altura * pi
def volumen_cilindro(radio: float, altura: float) -> float:
    """Calcula el volumen de un cilindro."""
    return np.pi * radio ** 2 * altura

# Calcula el volumen de un prisma rectangular: largo * ancho * alto
def volumen_prisma_rectangular(longitud: float, anchura: float, altura: float) -> float:
    """Calcula el volumen de un prisma rectangular."""
    return longitud * anchura * altura

# Calcula el volumen de un cubo: arista^3
def volumen_cubo(arista: float) -> float:
    """Calcula el volumen de un cubo."""
    return arista ** 3

# Función principal: define valores de ejemplo y muestra los resultados
def iniciar_programa() -> None:
    """No devuelve nada; imprime resultados en pantalla."""
    # 1) Volumen del cilindro
    radio = 5
    altura_cilindro = 10
    vol_cilindro = volumen_cilindro(radio, altura_cilindro)
    print(f"El volumen del cilindro (r={radio}, h={altura_cilindro}) es: {vol_cilindro:.2f}")

    # 2) Volumen del prisma rectangular
    longitud = 6
    anchura = 4
    altura_prisma = 2
    vol_prisma = volumen_prisma_rectangular(longitud, anchura, altura_prisma)
    print(f"El volumen del prisma rectangular (l={longitud}, a={anchura}, h={altura_prisma}) es: {vol_prisma:.2f}")

    # 3) Volumen del cubo
    arista = 3
    vol_cubo = volumen_cubo(arista)
    print(f"El volumen del cubo (arista={arista}) es: {vol_cubo:.2f}")

# Ejecutar el programa solo si este archivo se corre directamente
esta_ejecucion_es_directa = (__name__ == "__main__")

if esta_ejecucion_es_directa:
    iniciar_programa()
