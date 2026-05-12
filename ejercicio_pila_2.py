"""Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden números pares."""

from tda_pila import pila, apilar, desapilar, pila_vacia, en_cima, tamanio

mi_pila = pila()
pila_auxiliar = pila()

corte = int(input("ingrese 1 para entrar 0 para salir:  "))

while corte != 0:
    fin = int(input("Ingrese el dato: "))
    apilar(mi_pila, fin)
    corte = int(input("Desea seguir 1= SI, 0= NO: "))

while pila_vacia(mi_pila) == False:
    dato = desapilar(mi_pila)
    if dato % 2 == 0:
        apilar(pila_auxiliar, dato)
    else:
        impar = dato
        
while pila_vacia(pila_auxiliar) == False:
    dato = desapilar(pila_auxiliar)
    apilar(mi_pila, dato)
    dato = desapilar(mi_pila)
    print(dato)
