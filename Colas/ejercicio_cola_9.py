"""9. Dada una cola de valores enteros calcular su rango y contar cuántos elementos negativos hay."""

from .tda_cola import cola, arribo, atencion, cola_vacia, tamanio, barrido
from .validaciones import validar_numero

mi_cola = cola()
cola_auxiliar = cola()

corte = validar_numero("Desea ingresar un numero: 1=Si, 0=Salir: ")
while corte != 0 and corte != 1:
    print("Numero invalido")
    corte = validar_numero("Desea ingresar un numero: 1=Si, 0=Salir: ")

while corte != 0:
    numero = validar_numero("Ingrese un numero entero: ")
    arribo(mi_cola, numero)

    corte = validar_numero("Desea ingresar otro numero: 1=Si, 0=Salir: ")
    while corte != 0 and corte != 1:
        print("Numero invalido")
        corte = validar_numero("Desea ingresar otro numero: 1=Si, 0=Salir: ")

if cola_vacia(mi_cola) == False:

    dato = atencion(mi_cola)
    mayor = dato
    menor = dato
    negativos = 0

    if dato < 0:
        negativos += 1

    arribo(cola_auxiliar, dato)

    while cola_vacia(mi_cola) == False:

        dato = atencion(mi_cola)

        if dato > mayor:
            mayor = dato

        if dato < menor:
            menor = dato

        if dato < 0:
            negativos += 1

        arribo(cola_auxiliar, dato)

    rango = mayor - menor

    print("El rango es:", rango)
    print("Cantidad de numeros negativos:", negativos)

    while cola_vacia(cola_auxiliar) == False:
        arribo(mi_cola, atencion(cola_auxiliar))

    print("Contenido de la cola:")
    barrido(mi_cola)

else:
    print("La cola esta vacia.")