"""Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden ordenados de forma creciente. Solo puede utilizar una pila auxiliar como estructura extra no se pueden utilizar métodos de ordenamiento."""
from .tda_pila import nodopila, pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido
from .validaciones import validar_string,validar_numero

mi_pila = pila()
pila_auxiliar = pila()
corte = validar_numero("¿Desea ingresar un elemento? 1 = SI / 0 para salir: ")


while corte != 0 and corte != 1:
    print("Numero invalido")
    corte = validar_numero("¿Desea ingresar un elemento? 1 = SI / 0 para salir: ")


while corte != 0:
    numero = validar_numero("Ingrese un numero: ")
    
    while pila_vacia(mi_pila) == False and (en_cima(mi_pila) > numero):
        dato = desapilar(mi_pila)
        apilar(pila_auxiliar, dato)
    apilar(mi_pila, numero)

    while pila_vacia(pila_auxiliar) == False:
        dato = desapilar(pila_auxiliar)
        apilar(mi_pila, dato)
    corte = validar_numero("Desea seguir? 1=SI / 0=NO: ")
    while corte != 0 and corte != 1:
        print("Numero invalido")
        corte = validar_numero("Desea seguir? 1 = SI, 0 = NO: ")


print("Pila ordenada:")
barrido(mi_pila)