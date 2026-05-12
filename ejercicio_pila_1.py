"""Determinar el número de ocurrencias de un determinado elemento en una pila."""

from tda_pila import pila, apilar, desapilar, pila_vacia, en_cima, tamanio

corte = int(input("ingrese 1 para entrar 0 para salir:  "))
mi_pila = pila()
contador = 0
while corte != 0:
    fin = int(input("Ingrese el dato: "))
    apilar(mi_pila, fin)
    corte = int(input("Desea seguir 1= SI, 0= NO: "))

elemento = int(input("ingrese el elemento: "))

while pila_vacia(mi_pila) == False:
    dato = desapilar(mi_pila)
    if dato == elemento:
        contador += 1
print(f"el numero de ocurrencias de el elemento:{elemento} fue de {contador}")