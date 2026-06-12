"""Eliminar el i-ésimo elemento debajo de la cima de una pila de palabras."""
from .tda_pila import pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

mi_pila = pila()
pila_auxiliar = pila()
lista = []
contador = 0
contador_eliminar = 0
corte = int(input("presione un numero para ingresar una palabra / 0 para salir:  "))

while corte != 0:
    palabra = input("Ingrese la palabra: ")
    apilar(mi_pila, palabra)
    lista.append(palabra)
    corte = int(input("Desea seguir 1= SI, 0= NO: "))

corte = int(input("Desea eliminar una palabra? 1=SI / 0=NO: "))

for palabra in reversed(lista):
    print(f"{contador}-{palabra}")
    contador += 1

palabra_eliminar = int(input("Ingrese el indice de la palabra que quiere eliminar: "))

while corte != 0 and pila_vacia(mi_pila) == False:
    palabra = desapilar(mi_pila)

    if contador_eliminar == palabra_eliminar:
        corte = 0
    else:
        contador_eliminar += 1
        apilar(pila_auxiliar, palabra)

while pila_vacia(pila_auxiliar) == False:
    palabra = desapilar(pila_auxiliar)
    apilar(mi_pila, palabra)

barrido(mi_pila)



