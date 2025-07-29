def c(r,h):return 3.14*r*r*h
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

# CODIGO CORREGIDO 

def c(r, h):
    return 3.14 * r * r * h

def v(l, a, h):
    return l * a * h

def cubo(a):
    return a * a * a

def principal():
    # Volumen del cilindro
    r = 5
    h = 10
    print('El volumen del cilindro es:', c(r, h))
    
    # Volumen del prisma rectangular
    l = 6
    a = 4
    h2 = 2
    print('El volumen del prisma rectangular es:', v(l, a, h2))
    
    # Volumen del cubo
    a2 = 3
    print('El volumen del cubo es:', cubo(a2))

# Cálculo de volúmenes
principal()
