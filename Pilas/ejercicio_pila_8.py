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
carta = []
contador = 0

def generar_mazo():
    while contador < 48:
        numero = random.randrange(1, 12)
        palo = random.choice(["oro","basto","espada","copa"])
        carta = {palo: numero}
        if palo == "oro":
            apilar(pila_oro, carta)
            contador_oro += 1
        elif palo == "basto":
            apilar(pila_basto, carta)
        elif palo == "espada":
            apilar(pila_espada, carta)
        elif palo == "copa":
            apilar(pila_copa, carta)
        
