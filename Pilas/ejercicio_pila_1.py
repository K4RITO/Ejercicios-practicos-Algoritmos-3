"""Determinar el número de ocurrencias de un determinado elemento en una pila."""

from tda_pila import pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido


mi_pila = pila()
contador = 0
corte = int(input("ingrese un numero para ingresar datos / 0 para salir:  "))
while corte != 0:
    fin = int(input("Ingrese el dato: "))
    apilar(mi_pila, fin)
    corte = int(input("Desea seguir 1= SI, 0= NO: "))

elemento = int(input("ingrese el elemento que quiere buscar en la pila: "))

while pila_vacia(mi_pila) == False:
    dato = desapilar(mi_pila)
    if dato == elemento:
        contador += 1
print(f"el numero de ocurrencias de el elemento:{elemento} fue de {contador}")