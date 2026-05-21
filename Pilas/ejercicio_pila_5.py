"""Determinar si una cadena de caracteres es un palíndromo."""
from tda_pila import pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

mi_pila = pila()
lista = []
corte = int(input("presione una tecla para ingresar datos / 0 para salir:  "))

while corte != 0:
    fin = int(input("Ingrese el dato: "))
    apilar(mi_pila, fin)
    corte = int(input("Desea seguir 1= SI, 0= NO: "))

while pila_vacia(mi_pila) == False:
    dato = desapilar(mi_pila)
    lista.append(dato)

for dato in lista:
    if lista[0] == lista [-1]:
        del lista[0]
        del lista[-1]
    else:
        break

if len(lista) <= 1:
    print("Es un palindromo")
else:
    print("No es un palindromo")