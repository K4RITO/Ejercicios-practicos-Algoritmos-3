"""4. Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos."""

from .tda_cola import nodocola, cola, arribo, atencion, cola_vacia, en_frente, tamanio, mover_al_final, barrido
from Pilas.tda_pila import nodopila, pila, apilar, desapilar, pila_vacia, en_cima, tamanio
from .validaciones import validar_numero, validar_string

mi_cola = cola()
cola_auxiliar = cola()

corte = validar_numero("Desea ingresar un numero: 1 = si, 0 = Salir: ")
while corte != 0 and corte != 1:
        print("Numero invalido")
        corte = validar_numero("Desea ingresar un numero: 1 = si, 0 = Salir: ")

while corte != 0:
    numero = validar_numero("Ingrese un numero: ")
    arribo(mi_cola, numero)
    corte = validar_numero("Desea ingresar otro: 1= si, 0= no: ")
    while corte != 0 and corte != 1:
        print("Numero invalido")
        corte = validar_numero("Desea ingresar otro: 1= si, 0= no: ")

print("\nCola original:")
barrido(mi_cola)


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

print("\nCola sin numeros NO primos:")
barrido(cola_auxiliar)