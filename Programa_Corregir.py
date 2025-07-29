import numpy as np
import matplotlib as mt

#función para calcular el volumen de un cilindro
def Vol_cilindro (radio, altura):
    return 3.14 *radio*radio*altura


#función para calcular el volumen de un prisma
def Vol_prisma (largo, ancho, altura):
    return largo*ancho*altura


#funcion para calcular el area de un cucbo
def cubo (altura):
    return altura*altura*altura

# funcion que llama las demás funciones
def principal ():
    radio1 = 5  #definimos el radio del cilindro
    altura2 = 10 #definimos la altura del cilindro
    print('El volumen del cilindro es:',(radio1**2 * altura2))
    
    
    largo1 = 6 #definimos el largo del prisma
    ancho1 = 4 #definimos el ancho del prisma
    altura1 = 2 #definimos la altura del prisma
    print('volumen del prisma rectangular es:',Vol_prisma (largo1, ancho1, altura1))
    
    volumen_cubo = 3 #definimos el volumen del cubo
    print('El volumen del cubo es:',cubo (volumen_cubo**3))


#Calculo volumenes

principal()