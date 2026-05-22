"""Resolver el problema del factorial de un número utilizando una pila."""
from tda_pila import nodopila, pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

mi_pila = pila()

numero = int(input("Ingrese el numero a factorizar: "))

for i in range(1, numero + 1):
    apilar(mi_pila, i)
acumulador = 1
while not pila_vacia(mi_pila):
    dato = desapilar(mi_pila)
    acumulador *= dato

print(f"El factorial de {numero} es: {acumulador}")