"""Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra."""
from tda_pila import pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

mi_pila = pila()
pila_auxiliar = pila()
corte = int(input("ingrese un numero para ingresar datos / 0 para salir:  "))
while corte != 0:
    fin = int(input("Ingrese el dato: "))
    apilar(mi_pila, fin)
    corte = int(input("Desea seguir 1= SI, 0= NO: "))


while pila_vacia(mi_pila) == False:
    dato = desapilar(mi_pila)
    apilar(pila_auxiliar, dato)

while pila_vacia(pila_auxiliar) == False:
    dato = desapilar(pila_auxiliar)
    print(dato)