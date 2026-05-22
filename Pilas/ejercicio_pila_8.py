"""Dada una pila de cartas de las cuales se conoce su número y palo,que representa un mazo de
cartas de baraja española,resolver las siguientes actividades:
a. generar las cartas del mazo de forma aleatoria;
b. separar la pila mazo en cuatro pilas una por cada palo;
c. ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente."""
from tda_pila import nodopila, pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

import random


mazo = pila()
pila_oro = pila()
pila_basto = pila()
pila_espada = pila()
pila_copa = pila()
pila_auxiliar = pila()
cartas_usadas = []

while tamanio(mazo) < 48:

    numero = random.randint(1, 12)
    palo = random.choice(["oro", "basto", "espada", "copa",])
    carta = [palo, numero]

    if carta not in cartas_usadas:
        cartas_usadas.append(carta)
        apilar(mazo, carta)
        print(carta)


while pila_vacia(mazo) == False:
    carta = desapilar(mazo)

    if carta[0] == "oro":
        apilar(pila_oro, carta)
    elif carta[0] == "basto":
        apilar(pila_basto, carta)
    elif carta[0] == "espada":
        apilar(pila_espada, carta)
    else:
        apilar(pila_copa, carta)

ordenar = input("que pila quiere ordenar: oro, basto, espada, copa: ")
if ordenar == "oro":
    while pila_vacia(pila_oro) == False:
        carta = desapilar(pila_oro)

        while pila_vacia(pila_auxiliar)== False and (en_cima(pila_auxiliar)[1] > carta[1]):
            apilar(pila_oro, desapilar(pila_auxiliar))
        apilar(pila_auxiliar, carta)
elif ordenar == "basto":
    while pila_vacia(pila_basto) == False:
        carta = desapilar(pila_basto)

        while pila_vacia(pila_auxiliar)== False and (en_cima(pila_auxiliar)[1] > carta[1]):
            apilar(pila_basto, desapilar(pila_auxiliar))
        apilar(pila_auxiliar, carta)
elif ordenar == "espada":
    while pila_vacia(pila_espada) == False:
        carta = desapilar(pila_espada)

        while pila_vacia(pila_auxiliar)== False and (en_cima(pila_auxiliar)[1] > carta[1]):
            apilar(pila_espada, desapilar(pila_auxiliar))
        apilar(pila_auxiliar, carta)
else:
    while pila_vacia(pila_copa) == False:
        carta = desapilar(pila_copa)

        while pila_vacia(pila_auxiliar)== False and (en_cima(pila_auxiliar)[1] > carta[1]):
            apilar(pila_copa, desapilar(pila_auxiliar))
        apilar(pila_auxiliar, carta)

if ordenar == "oro":
    while pila_vacia(pila_auxiliar) == False:
        apilar(pila_oro, desapilar(pila_auxiliar))

    print("Pila de oro ordenada:")

    barrido(pila_oro)
elif ordenar == "basto":
    while pila_vacia(pila_auxiliar) == False:
        apilar(pila_basto, desapilar(pila_auxiliar))

    print("Pila de basto ordenada:")

    barrido(pila_basto)
elif ordenar == "espada":
    while pila_vacia(pila_auxiliar) == False:
        apilar(pila_espada, desapilar(pila_auxiliar))

    print("Pila de espada ordenada:")

    barrido(pila_espada)
else:
    while pila_vacia(pila_auxiliar) == False:
        apilar(pila_copa, desapilar(pila_auxiliar))

    print("Pila de copa ordenada:")

    barrido(pila_copa)