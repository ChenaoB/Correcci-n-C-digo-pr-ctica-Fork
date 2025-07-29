import numpy as np

def c(r,h): return 3.14*r*r*h
def v(l,a,h): return l*a*h
def cubo(a): return a*a*a
def principal():
    r = 5
    h = 10
    print("El volumen del cilindro:", c(r, h))
    l = 6
    a = 4
    h2 = 2
    print("El volumen del prisma rectangular:", v(l, a, h2))
    a2 = 3
    print("El volumen del cubo:", cubo(a2))
    #Calculo volumenes
principal()