"""1. Eliminar de una cola de caracteres todas las vocales que aparecen."""

from .tda_cola import nodocola, cola, arribo, atencion, cola_vacia, en_frente,tamanio, mover_al_final, barrido
from .validaciones import validar_numero, validar_string


mi_cola = cola()
cola_auxiliar = cola()
corte = validar_numero("Desea ingresar datos: 1 = si, 0 = no: ")
while corte != 0 and corte != 1:
        print("Numero invalido")
        corte = validar_numero("Desea ingresar datos: 1 = si, 0 = no: ")

while  corte != 0:
    
    caracter = validar_string("Ingrese un caracter: ")
    while len(caracter) > 1:
         print("Error: Ingrese un solo caracter")
         caracter = validar_string("Ingrese un caracter: ")
    arribo(mi_cola, caracter)
    corte = validar_numero("Seguir ingresando datos: 1 = si, 0 para salir: ")
    while corte != 0 and corte != 1:
        print("Numero invalido")
        corte = validar_numero("Seguir ingresando datos: 1 = si, 0 para salir: ")

print("\nCola original:")
barrido(mi_cola)

while cola_vacia(mi_cola) == False: 
    dato = atencion(mi_cola)
    if dato in "aeiou":
        dato = "es vocal"
    else:
        arribo(cola_auxiliar, dato)

print("\nCola sin bocales:")
barrido(cola_auxiliar)