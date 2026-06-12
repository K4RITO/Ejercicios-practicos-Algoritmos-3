"""2. Utilizando operaciones de cola y pila, invertir el contenido de una cola."""

from .tda_cola import nodocola, cola, arribo, atencion, cola_vacia, en_frente, tamanio, mover_al_final, barrido

from Pilas.tda_pila import nodopila, pila, apilar, desapilar, pila_vacia, en_cima, tamanio

mi_pila = pila()
mi_cola = cola()
corte = int(input("Desea ingresar datos: 1 = si, 0 = no: "))

while corte != 0:
    dato = input("Ingrese el dato: ")
    arribo(mi_cola, dato)
    corte = int(input("Desea ingresar otro dato: 1 = si, 0 = no: "))


while cola_vacia(mi_cola) == False:
    dato = atencion(mi_cola)
    apilar(mi_pila, dato)

while pila_vacia(mi_pila)  == False:
    dato = desapilar(mi_pila)
    arribo(mi_cola, dato)

barrido(mi_cola)