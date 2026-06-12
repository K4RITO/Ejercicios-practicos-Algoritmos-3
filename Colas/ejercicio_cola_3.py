"""3. Dada una secuencia de caracteres utilizando operaciones de cola y pila determinar
si es un palíndromo."""

from .tda_cola import nodocola, cola, arribo, atencion, cola_vacia, en_frente, tamanio, mover_al_final, barrido

from Pilas.tda_pila import nodopila, pila, apilar, desapilar, pila_vacia, en_cima, tamanio

mi_pila = pila()
mi_cola = cola()
cola_auxiliar = cola()
contador = 0

corte = True

while corte == True:
    dato = input("Ingrese la secuencia de caracteres: ")
    caracteres = list(dato)
    for i in caracteres:    
        arribo(mi_cola, caracteres[contador])
        contador += 1
    corte = False

while cola_vacia(mi_cola) == False:
    dato = atencion(mi_cola)
    apilar(mi_pila, dato)
    arribo(cola_auxiliar, dato)

while cola_vacia(cola_auxiliar) == False:
    dato_pila = desapilar(mi_pila)
    dato_cola = atencion(cola_auxiliar)

    if dato_pila == dato_cola:
        palindromo = True
    else:
        palindromo = False
        break

if palindromo == True:
    print("Es palindromo")
else:
    print("no es palindromo")
