"""12. Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar, ni métodos de ordenamiento."""
from .tda_cola import cola, arribo, atencion, cola_vacia, en_frente, barrido
from .validaciones import validar_numero

cola_1 = cola()
cola_2 = cola()
cola_3 = cola()

print("Cargar datos de la cola 1 (ordenados)")

corte = validar_numero("Desea ingresar un numero: 1=Si, 0=Salir: ")
while corte != 0 and corte != 1:
    print("Numero invalido")
    corte = validar_numero("Desea ingresar un numero: 1=Si, 0=Salir: ")

while corte != 0:

    dato = validar_numero("Ingrese un numero: ")
    arribo(cola_1, dato)

    corte = validar_numero("Desea ingresar otro numero: 1=Si, 0=Salir: ")
    while corte != 0 and corte != 1:
        print("Numero invalido")
        corte = validar_numero("Desea ingresar otro numero: 1=Si, 0=Salir: ")

print("Cargar datos de la cola 2 (ordenados)")

corte = validar_numero("Desea ingresar un numero: 1=Si, 0=Salir: ")
while corte != 0 and corte != 1:
    print("Numero invalido")
    corte = validar_numero("Desea ingresar un numero: 1=Si, 0=Salir: ")

while corte != 0:

    dato = validar_numero("Ingrese un numero: ")
    arribo(cola_2, dato)

    corte = validar_numero("Desea ingresar otro numero: 1=Si, 0=Salir: ")
    while corte != 0 and corte != 1:
        print("Numero invalido")
        corte = validar_numero("Desea ingresar otro numero: 1=Si, 0=Salir: ")

while cola_vacia(cola_1) == False and cola_vacia(cola_2) == False:

    if en_frente(cola_1) < en_frente(cola_2):
        arribo(cola_3, atencion(cola_1))
    else:
        arribo(cola_3, atencion(cola_2))

while cola_vacia(cola_1) == False:
    arribo(cola_3, atencion(cola_1))

while cola_vacia(cola_2) == False:
    arribo(cola_3, atencion(cola_2))

print("Cola combinada:")

barrido(cola_3)