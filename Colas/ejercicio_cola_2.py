"""2. Utilizando operaciones de cola y pila, invertir el contenido de una cola."""

from .tda_cola import nodocola, cola, arribo, atencion, cola_vacia, en_frente, tamanio, mover_al_final, barrido
from Pilas.tda_pila import nodopila, pila, apilar, desapilar, pila_vacia, en_cima, tamanio
from .validaciones import validar_numero, validar_string

mi_pila = pila()
mi_cola = cola()
corte = validar_numero("Desea ingresar datos: 1 = si, 0 = no: ")
while corte != 0 and corte != 1:
        print("Numero invalido")
        corte = validar_numero("Desea ingresar datos: 1 = si, 0 = no: ")


while corte != 0:
    dato = input("Ingrese el dato: ")
    arribo(mi_cola, dato)
    corte = validar_numero("Seguir ingresando datos: 1 = si, 0 para salir: ")
    while corte != 0 and corte != 1:
        print("Numero invalido")
        corte = validar_numero("Seguir ingresando datos: 1 = si, 0 para salir: ")


while cola_vacia(mi_cola) == False:
    dato = atencion(mi_cola)
    apilar(mi_pila, dato)

while pila_vacia(mi_pila)  == False:
    dato = desapilar(mi_pila)
    arribo(mi_cola, dato)

barrido(mi_cola)