"""5. Utilizando operaciones de cola y pila, invertir el contenido de una pila."""

from .tda_cola import nodocola, cola, arribo, atencion, cola_vacia, en_frente, tamanio, mover_al_final, barrido

from Pilas.tda_pila import nodopila, pila, apilar, desapilar, pila_vacia, en_cima, tamanio

mi_cola = cola()
mi_pila = pila()

corte = int(input("Desea ingresar un dato: 1 = si, 0 = Salir: "))

while corte != 0:
    dato = input("Ingrese el dato: ")
    apilar(mi_pila, dato)
    corte = int(input("Desea ingresar otro dato 1= si, 0=no: "))

while pila_vacia(mi_pila) == False:
    dato = desapilar(mi_pila)
    arribo(mi_cola, dato)

barrido(mi_cola)