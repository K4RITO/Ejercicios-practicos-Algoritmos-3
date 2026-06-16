"""6.Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar ninguna estructura auxiliar"""

from .tda_cola import nodocola, cola, arribo, atencion, cola_vacia, en_frente, tamanio, mover_al_final, barrido

from Pilas.tda_pila import nodopila, pila, apilar, desapilar, pila_vacia, en_cima, tamanio

mi_cola= cola()
contador = 0
corte = int(input("Desea ingresar un dato: 1=Si, 0=Salir"))

while corte != 0:
    dato = input("Ingrese el elemento: ")
    arribo(mi_cola, dato)
    corte = int(input("Desea ingresar otro elemento: 1=si 0=no"))

elemento = input("ingrese el elemento que quiere buscar: ")
while cola_vacia(mi_cola) == False:
    
    while cola_vacia(mi_cola) == False:
        if elemento != en_frente(mi_cola):
            atencion(mi_cola)
        elif elemento == en_frente(mi_cola):
            contador += 1
            atencion(mi_cola)

print(f"La cantidad de ocurrencias de {elemento} en la cola de es {contador}")