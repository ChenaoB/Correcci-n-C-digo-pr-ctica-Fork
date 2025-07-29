Pi = 3.1486 # representa la constante de Pi
def volumenCilindro(radio, altura):
    return Pi * radio ** 2 * altura 


def VolumenRectangulo(longitud, ancho, altura):
    return longitud * ancho * altura


def volumenCubo(lado):
    return lado ** 3


def main():
    # calculo del volumen del cilindro 
    radio_Cilindro = 23
    altura_Cilindro = 34
    print('El volumen del cilindro es:', volumenCilindro(radio_Cilindro, altura_Cilindro))
    
# Cálculo del volumen del prisma rectangular
    longitud_prisma = 6
    ancho_prisma = 4
    altura_prisma = 2
    print('El volumen del prisma rectangular es:', VolumenRectangulo(longitud_prisma, ancho_prisma, altura_prisma))
    
    # Cálculo del volumen del cubo
    lado_cubo = 3
    print('El volumen del cubo es:', volumenCubo(lado_cubo))


# Ejecutar función principal
if __name__ == "__main__":
    main()

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
principal() """