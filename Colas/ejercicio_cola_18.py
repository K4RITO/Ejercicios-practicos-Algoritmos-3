"""18. Dada una cola con los códigos de turnos de atención (con el formato #@@@, donde # es una
letra de la A hasta la F y “@@@” son tres dígitos desde el 000 al 999), desarrollar un algoritmo
que resuelva las siguientes situaciones:
a. cargar 1000 turnos de manera aleatoria a la cola.
b. separar la cola con datos en dos colas, cola_1 con los turnos que empiezan con la letra A, C
y F, y la cola_2 con el resto de los turnos (B, D y E).
c. determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál de las letras
tiene mayor cantidad.
d. mostrar los turnos de la cola con menor cantidad de elementos, cuyo número de turno sea
mayor que 506."""

from .tda_cola import cola, arribo, atencion, cola_vacia, tamanio, barrido
import random
import string

mi_cola = cola()
cola_1 = cola()
cola_2 = cola()

# ---------------- Punto A ----------------

turnos_generados = set()

while len(turnos_generados) < 1000:

    letra = random.choice("ABCDEF")
    numero = random.randint(0, 999)

    turno = letra + str(numero).zfill(3)

    if turno not in turnos_generados:
        turnos_generados.add(turno)
        arribo(mi_cola, turno)

# ---------------- Punto B ----------------

while cola_vacia(mi_cola) == False:

    dato = atencion(mi_cola)

    if dato[0] == "A" or dato[0] == "C" or dato[0] == "F":
        arribo(cola_1, dato)
    else:
        arribo(cola_2, dato)

# ---------------- Punto C ----------------

cantidad_1 = tamanio(cola_1)
cantidad_2 = tamanio(cola_2)

print("Cantidad cola 1:", cantidad_1)
print("Cantidad cola 2:", cantidad_2)

if cantidad_1 > cantidad_2:

    print("La cola 1 tiene mayor cantidad de turnos")

    cola_auxiliar = cola()

    contador_A = 0
    contador_C = 0
    contador_F = 0

    while cola_vacia(cola_1) == False:

        dato = atencion(cola_1)

        if dato[0] == "A":
            contador_A += 1

        elif dato[0] == "C":
            contador_C += 1

        elif dato[0] == "F":
            contador_F += 1

        arribo(cola_auxiliar, dato)

    while cola_vacia(cola_auxiliar) == False:
        arribo(cola_1, atencion(cola_auxiliar))

    if contador_A >= contador_C and contador_A >= contador_F:
        print("La letra con mayor cantidad es A")

    elif contador_C >= contador_A and contador_C >= contador_F:
        print("La letra con mayor cantidad es C")

    else:
        print("La letra con mayor cantidad es F")

else:

    print("La cola 2 tiene mayor cantidad de turnos")

    cola_auxiliar = cola()

    contador_B = 0
    contador_D = 0
    contador_E = 0

    while cola_vacia(cola_2) == False:

        dato = atencion(cola_2)

        if dato[0] == "B":
            contador_B += 1

        elif dato[0] == "D":
            contador_D += 1

        elif dato[0] == "E":
            contador_E += 1

        arribo(cola_auxiliar, dato)

    while cola_vacia(cola_auxiliar) == False:
        arribo(cola_2, atencion(cola_auxiliar))

    if contador_B >= contador_D and contador_B >= contador_E:
        print("La letra con mayor cantidad es B")

    elif contador_D >= contador_B and contador_D >= contador_E:
        print("La letra con mayor cantidad es D")

    else:
        print("La letra con mayor cantidad es E")

# ---------------- Punto D ----------------

print("\nTurnos mayores a 506 de la cola con menor cantidad:")

if cantidad_1 < cantidad_2:

    cola_auxiliar = cola()

    while cola_vacia(cola_1) == False:

        dato = atencion(cola_1)

        if int(dato[1:]) > 506:
            print(dato)

        arribo(cola_auxiliar, dato)

    while cola_vacia(cola_auxiliar) == False:
        arribo(cola_1, atencion(cola_auxiliar))

else:

    cola_auxiliar = cola()

    while cola_vacia(cola_2) == False:

        dato = atencion(cola_2)

        if int(dato[1:]) > 506:
            print(dato)

        arribo(cola_auxiliar, dato)

    while cola_vacia(cola_auxiliar) == False:
        arribo(cola_2, atencion(cola_auxiliar))