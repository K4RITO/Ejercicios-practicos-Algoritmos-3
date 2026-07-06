"""Reemplazar todas las ocurrencias de un determinado elemento en una pila."""

from .tda_pila import pila, apilar, desapilar, pila_vacia, barrido
from .validaciones import validar_numero

mi_pila = pila()
pila_auxiliar = pila()

corte = validar_numero("Ingrese 1 para ingresar datos / 0 para salir: ")

while corte != 0 and corte != 1:
    print("Numero invalido. ")
    corte = validar_numero("Ingrese 1 para ingresar datos / 0 para salir: ")


while corte != 0:
    dato = input("Ingrese el dato: ")
    apilar(mi_pila, dato)

    corte = validar_numero("Desea seguir? 1 = SI, 0 = NO: ")

    while corte != 0 and corte != 1:
        print("Numero invalido. ")
        corte = validar_numero("Desea seguir? 1 = SI, 0 = NO: ")

elemento_reemplazar = input("Ingrese el elemento que quiere reemplazar en la pila: ")
elemento_nuevo = input("Ingrese el dato que quiere agregar en su lugar: ")


while pila_vacia(mi_pila) == False:
    dato = desapilar(mi_pila)

    if dato == elemento_reemplazar:
        dato = elemento_nuevo

    apilar(pila_auxiliar, dato)

while  pila_vacia(pila_auxiliar) == False:
    dato = desapilar(pila_auxiliar)
    apilar(mi_pila, dato)

print("Pila luego del reemplazo:")
barrido(mi_pila)