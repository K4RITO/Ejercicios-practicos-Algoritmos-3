"""6.Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar ninguna estructura auxiliar"""

from .tda_cola import nodocola, cola, arribo, atencion, cola_vacia, en_frente, tamanio, mover_al_final, barrido
from Pilas.tda_pila import nodopila, pila, apilar, desapilar, pila_vacia, en_cima, tamanio
from .validaciones import validar_numero, validar_string

mi_cola= cola()
contador = 0
corte = validar_numero("Desea ingresar un dato: 1=Si, 0=Salir: ")
while corte != 0 and corte != 1:
        print("Numero invalido")
        corte = validar_numero("Desea ingresar un dato: 1 = si, 0 = Salir: ")

while corte != 0:
    dato = input("Ingrese el elemento: ")
    arribo(mi_cola, dato)
    corte = validar_numero("Desea ingresar otro dato: 1 = si, 0 = Salir: ")
    while corte != 0 and corte != 1:
        print("Numero invalido")
        corte = validar_numero("Desea ingresar otro dato: 1 = si, 0 = Salir: ")

elemento = input("ingrese el elemento que quiere buscar: ")
while cola_vacia(mi_cola) == False:
    
    while cola_vacia(mi_cola) == False:
        if elemento != en_frente(mi_cola):
            atencion(mi_cola)
        elif elemento == en_frente(mi_cola):
            contador += 1
            atencion(mi_cola)

print(f"La cantidad de ocurrencias de {elemento} en la cola de es {contador}")