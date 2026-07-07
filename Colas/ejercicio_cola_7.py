"""7.eliminar el i-ésimo elemento despues del frente de la cola."""

from .tda_cola import nodocola, cola, arribo, atencion, cola_vacia, en_frente, tamanio, mover_al_final, barrido
from Pilas.tda_pila import nodopila, pila, apilar, desapilar, pila_vacia, en_cima, tamanio
from .validaciones import validar_numero,validar_string

mi_cola= cola()
cola_auxiliar = cola()
indice = 1
contador = 1
corte = validar_numero("Desea ingresar un dato: 1=Si, 0=Salir: ")
while corte != 0 and corte != 1:
        print("Numero invalido")
        corte = validar_numero("Desea ingresar un dato: 1 = si, 0 = Salir: ")


while corte != 0:
    dato = input("Ingrese el elemento: ")
    arribo(mi_cola, dato)
    corte = validar_numero("Desea ingresar otro dato: 1=Si, 0=Salir: ")
while corte != 0 and corte != 1:
        print("Numero invalido")
        corte = validar_numero("Desea ingresar otro dato: 1 = si, 0 = Salir: ")


while cola_vacia(mi_cola) == False:    
    dato = atencion(mi_cola)
    print(f"{indice}-{dato}")
    indice += 1
    arribo(cola_auxiliar, dato)

while cola_vacia(cola_auxiliar) == False:
    dato = atencion(cola_auxiliar)
    arribo(mi_cola, dato)

elemento = validar_numero("Ingrese el índice del elemento que quiere eliminar: ")


while cola_vacia(mi_cola) == False:
    dato = atencion(mi_cola)

    if contador != elemento:
        arribo(cola_auxiliar, dato)

    contador += 1

while cola_vacia(cola_auxiliar) == False:
    arribo(mi_cola, atencion(cola_auxiliar))

barrido(mi_cola)