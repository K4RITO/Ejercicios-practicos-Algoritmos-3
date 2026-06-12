"""Dada una pila de letras determinar cuántas vocales contiene."""
from .tda_pila import nodopila, pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

mi_pila = pila()
contador = 0

corte = int(input("presione un numero para ingresar una letra / 0 para salir:  "))

while corte != 0:
    letra = input("Ingrese la letra: ")
    apilar(mi_pila, letra)
    corte = int(input("Desea seguir 1= SI, 0= NO: "))

while pila_vacia(mi_pila) == False:
    letra = desapilar(mi_pila)
    if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u":
        contador += 1

print(f"la cantidad de vocales en la pila es de: {contador}")