"""14. Realizar un algoritmo que permita realizar las siguientes funciones:
a. cargar semáforos de una rotonda y sus respectivos tiempos de encendido en verde cargue
al menos tres semáforos.
b. simular el funcionamiento de los semáforos cargados (cola circular).
c. debe mostrar por pantalla el cambio de colores y el número del semáforo."""

from .tda_cola import cola, arribo, atencion, cola_vacia
from .validaciones import validar_numero
import time

mi_cola = cola()

cantidad = 0
numero = 0
while cantidad < 3:

    print("Semaforo", cantidad + 1)

    numero += 1
    tiempo = validar_numero("Ingrese el tiempo en verde (segundos): ")

    semaforo = {
        "numero": numero,
        "tiempo": tiempo
    }

    arribo(mi_cola, semaforo)

    cantidad += 1

ciclos = validar_numero("Ingrese la cantidad de ciclos a simular: ")

while ciclos > 0:

    dato = atencion(mi_cola)

    print("-----------------------------")
    print("Semaforo:", dato["numero"])
    print("Color: VERDE")
    time.sleep(dato["tiempo"])

    print("Semaforo:", dato["numero"])
    print("Color: AMARILLO")
    time.sleep(2)

    print("Semaforo:", dato["numero"])
    print("Color: ROJO")
    time.sleep(1)

    arribo(mi_cola, dato)

    ciclos -= 1