"""Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden números pares."""

from .tda_pila import pila, apilar, desapilar, pila_vacia, barrido
from .validaciones import validar_numero

mi_pila = pila()
pila_auxiliar = pila()

corte = validar_numero("Ingrese un número para ingresar datos / 0 para salir: ")
while corte != 0 and corte != 1:
    print("Ingrese un numero valido")
    corte = validar_numero("Ingrese un número para ingresar datos / 0 para salir: ")

while corte != 0:
    dato = validar_numero("Ingrese el dato: ")
    apilar(mi_pila, dato)
    corte = validar_numero("Desea seguir? 1 = SI, 0 = NO: ")

    while corte != 0 and corte != 1:
        print("Ingrese un numero valido")
        corte = validar_numero("Desea seguir? 1 = SI, 0 = NO: ")
   
while pila_vacia(mi_pila) == False:
    dato = desapilar(mi_pila)
    if dato % 2 == 0:
        apilar(pila_auxiliar, dato)

while pila_vacia(pila_auxiliar) == False:
    dato = desapilar(pila_auxiliar)
    apilar(mi_pila, dato)

print("Pila con solo números pares:")
barrido(mi_pila)