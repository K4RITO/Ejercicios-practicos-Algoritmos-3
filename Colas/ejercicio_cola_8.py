"""8. Realizar un algoritmo que mantenga ordenado los elementos agregados a una cola, utilizando
solo una cola como estructura auxiliar."""

from .tda_cola import nodocola, cola, arribo, atencion, cola_vacia, en_frente, tamanio, mover_al_final, barrido

from Pilas.tda_pila import nodopila, pila, apilar, desapilar, pila_vacia, en_cima, tamanio

mi_cola = cola()
cola_auxiliar = cola()

corte = int(input("Desea ingresar un dato: 1=Si, 0=Salir: "))

while corte != 0:
    dato = input("Ingrese el elemento: ")
    arribo(mi_cola, dato)
    corte = int(input("Desea ingresar otro elemento: 1=si 0=no: "))

while not cola_vacia(mi_cola):

    dato = atencion(mi_cola)
    insertado = False
    cantidad = tamanio(cola_auxiliar)

    for i in range(cantidad):

        x = atencion(cola_auxiliar)

        if not insertado and dato < x:
            arribo(cola_auxiliar, dato)
            insertado = True

        arribo(cola_auxiliar, x)

    if not insertado:
        arribo(cola_auxiliar, dato)

barrido(cola_auxiliar)