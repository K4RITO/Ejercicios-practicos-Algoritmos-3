"""Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra."""

from .tda_pila import pila, apilar, desapilar, pila_vacia, barrido
from .validaciones import validar_numero

mi_pila = pila()
pila_auxiliar = pila()

corte = validar_numero("Ingrese 1 para ingresar datos / 0 para salir: ")

while corte != 0 and corte != 1:
    print("Numero invalido")
    corte = validar_numero("Ingrese 1 para ingresar datos / 0 para salir: ")


while corte != 0:
    dato = input("Ingrese el dato: ")
    apilar(mi_pila, dato)

    corte = validar_numero("Desea seguir? 1 = SI, 0 = NO: ")

    while corte != 0 and corte != 1:
        print("Numero invalido")
        corte = validar_numero("Desea seguir? 1 = SI, 0 = NO: ")


while  pila_vacia(mi_pila) == False:
    dato = desapilar(mi_pila)
    apilar(pila_auxiliar, dato)

print("Pila invertida:")
barrido(pila_auxiliar)