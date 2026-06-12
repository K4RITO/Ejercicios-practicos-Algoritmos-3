"""Reemplazar todas las ocurrencias de un determinado elemento en una pila."""
from .tda_pila import pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido


mi_pila = pila()
pila_auxiliar = pila()
corte = int(input("ingrese un numero para ingresar datos / 0 para salir:  "))
while corte != 0:
    fin = int(input("Ingrese el dato: "))
    apilar(mi_pila, fin)
    corte = int(input("Desea seguir 1= SI, 0= NO: "))

elemento_reemplazar = int(input("Ingrese el elemento que quiere reemplazar en la pila: "))
elemento = int(input("Ingrese el dato que quiere agregar en su lugar: "))

while pila_vacia(mi_pila) == False:
    dato = desapilar(mi_pila)
    if dato == elemento_reemplazar:
        dato = elemento
    apilar(pila_auxiliar, dato)
    dato = desapilar(pila_auxiliar)
    print(dato)

