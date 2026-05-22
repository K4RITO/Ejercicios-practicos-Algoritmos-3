"""Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden ordenados de forma creciente. Solo puede utilizar una pila auxiliar como estructura extra no se pueden utilizar métodos de ordenamiento."""
from tda_pila import nodopila, pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

mi_pila = pila()
pila_auxiliar = pila()
corte = int(input("presione un numero para ingresar un dato / 0 para salir:  "))

while corte != 0:
    numero = int(input("Ingrese un numero: "))
    
    while (not pila_vacia(mi_pila)) and (en_cima(mi_pila) > numero):
        dato = desapilar(mi_pila)
        apilar(pila_auxiliar, dato)
    apilar(mi_pila, numero)

    while not pila_vacia(pila_auxiliar):
        dato = desapilar(pila_auxiliar)
        apilar(mi_pila, dato)
    corte = int(input("Desea seguir? 1=SI / 0=NO: "))

print("Pila ordenada:")
barrido(mi_pila)