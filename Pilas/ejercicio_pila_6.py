"""Leer una palabra y visualizarla en forma inversa."""
from .tda_pila import pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

mi_pila = pila()
contador = 0
lista = [] 
lista_caracteres = []
corte = int(input("ingrese un numero para ingresar la palabra / 0 para salir:  "))

while corte != 0:
    palabra = str(input("Ingrese la palabra: "))
    for caracter in palabra:
        lista_caracteres.append(caracter)
    corte = 0


while contador < len(lista_caracteres):
    dato = lista_caracteres[contador]
    contador += 1
    apilar(mi_pila,dato)

while pila_vacia(mi_pila) == False:
    dato = desapilar(mi_pila)
    lista.append(dato)
    
palabra_inversa = "".join(lista)
print(palabra)
print(palabra_inversa)
