"""Determinar el número de ocurrencias de un determinado elemento en una pila."""

from .tda_pila import pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

from .validaciones import validar_numero, validar_caracter_especial, validar_string, validar_contrasenia

mi_pila = pila()
contador = 0

corte = validar_numero("Desea ingresar un dato? 1=SI, 0=NO: ")

while corte != 1 and corte != 0:
    print("Ingrese un numero valido")
    corte = validar_numero("Desea ingresar un dato? 1=SI, 0=NO: ")

while corte != 0:
    dato = validar_numero("Ingrese el dato: ")
    apilar(mi_pila, dato)
    corte = validar_numero("Desea seguir? 1=SI, 0=NO: ")
    
    while corte != 1 and corte != 0:
        print("Ingrese un numero valido")
        corte = validar_numero("Desea seguir? 1=SI, 0=NO: ")

elemento = validar_numero("Ingrese el elemento que quiere buscar en la pila: ")

while pila_vacia(mi_pila) == False:
    dato = desapilar(mi_pila)
    if dato == elemento:
        contador += 1

print(f"El número de ocurrencias del elemento {elemento} fue de {contador}")