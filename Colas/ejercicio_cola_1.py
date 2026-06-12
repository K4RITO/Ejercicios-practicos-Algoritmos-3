"""1. Eliminar de una cola de caracteres todas las vocales que aparecen."""

from .tda_cola import nodocola, cola, arribo, atencion, cola_vacia, en_frente,tamanio, mover_al_final, barrido

corte = int(input("ingresar datos: 1 = Si, 0 para salir "))
mi_cola = cola()
cola_auxiliar = cola()

while  corte != 0:
    
    caracter = input("Ingrese un caracter: ")
    arribo(mi_cola, caracter)
    corte = int(input("Seguir ingresando datos: 1 = si, 0 para salir: "))

while cola_vacia(mi_cola) == False: 
    dato = atencion(mi_cola)
    if dato in "aeiou":
        dato = "es vocal"
    else:
        arribo(cola_auxiliar, dato)

barrido(cola_auxiliar)