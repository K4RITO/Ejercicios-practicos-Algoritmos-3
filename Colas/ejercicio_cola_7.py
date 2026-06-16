"""7.eliminar el i-ésimo elemento despues del frente de la cola."""

from .tda_cola import nodocola, cola, arribo, atencion, cola_vacia, en_frente, tamanio, mover_al_final, barrido

from Pilas.tda_pila import nodopila, pila, apilar, desapilar, pila_vacia, en_cima, tamanio

mi_cola= cola()
cola_auxiliar = cola()
indice = 1
contador = 1
corte = int(input("Desea ingresar un dato: 1=Si, 0=Salir: "))

while corte != 0:
    dato = input("Ingrese el elemento: ")
    arribo(mi_cola, dato)
    corte = int(input("Desea ingresar otro elemento: 1=si 0=no: "))

while(not cola_vacia(mi_cola)):    
    dato = atencion(mi_cola)
    print(f"{indice}-{dato}")
    indice += 1
    arribo(cola_auxiliar, dato)

while(not cola_vacia(cola_auxiliar)):
    dato = atencion(cola_auxiliar)
    arribo(mi_cola, dato)

elemento = int(input("Ingrese el índice del elemento que quiere eliminar: "))


while not cola_vacia(mi_cola):
    dato = atencion(mi_cola)

    if contador != elemento:
        arribo(cola_auxiliar, dato)

    contador += 1

while not cola_vacia(cola_auxiliar):
    arribo(mi_cola, atencion(cola_auxiliar))

barrido(mi_cola)