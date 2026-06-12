"""4. Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos."""

from .tda_cola import nodocola, cola, arribo, atencion, cola_vacia, en_frente, tamanio, mover_al_final, barrido

from Pilas.tda_pila import nodopila, pila, apilar, desapilar, pila_vacia, en_cima, tamanio

mi_cola = cola()
cola_auxiliar = cola()

corte = int(input("Desea ingresar un numero: 1 = si, 0 = Salir: "))

while corte != 0:
    numero = int(input("Ingrese un numero: "))
    arribo(mi_cola, numero)
    corte = int(input("Desea ingresar otro: 1= si, 0= no: "))

while cola_vacia(mi_cola) == False:
    numero = atencion(mi_cola)
    es_primo = True
    
    if numero < 2:
        es_primo = False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break
    if es_primo:
        arribo(cola_auxiliar, numero)

barrido(cola_auxiliar)