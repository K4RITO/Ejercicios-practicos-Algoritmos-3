"""Determinar si una cadena de caracteres es un palíndromo."""
from .tda_pila import pila, apilar, desapilar, pila_vacia, en_cima, tamanio
from .validaciones import validar_string, validar_numero


mi_pila = pila()

dato = validar_string("Ingrese la cadena: ").lower() 


for caracter in dato:
    apilar(mi_pila, caracter)


lista = list(dato)

for caracter_original in lista: 
    if pila_vacia(mi_pila):
        break
    caracter_pila = desapilar(mi_pila)  
    if caracter_original != caracter_pila:
        print("No es un palíndromo")


print("Es un palíndromo")
