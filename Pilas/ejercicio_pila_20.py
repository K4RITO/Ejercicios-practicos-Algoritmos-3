"""Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
cantidad de pasos y dirección suponga que el robot solo puede moverse en ocho direcciones:
norte, sur, este, oeste, noreste, noroeste, sureste y suroeste. Luego desarrolle otro algoritmo
que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
partida, retornando por el mismo camino que fue."""
from .tda_pila import nodopila, pila, apilar, desapilar, pila_vacia
from .validaciones import validar_string, validar_numero

movimientos = pila()
corte = 1
valido = True
while corte != 0:

    direccion = validar_string("Ingrese direccion: ").lower()
    while valido == True:
        if direccion not in("norte", "sur", "este", "oeste", "noreste", "noroeste", "sureste","suroeste"):
            print("ERROR: direccion invalida")
            direccion = validar_string("Ingrese direccion: ").lower()
            valido == False
        else:
            pasos = validar_numero("Ingrese cantidad de pasos: ")
            valido = True
            break

    movimiento = [direccion, pasos]

    apilar(movimientos, movimiento)

    corte = validar_numero("Desea ingresar otro? 1 = SI / 0 = NO: ")
    while corte != 0 and corte != 1:
        print("Numero invalido")
        corte = validar_numero("Desea ingresar otro? 1 = SI / 0 = NO: ")


print("\nCamino de regreso:\n")

while pila_vacia(movimientos) == False:

    movimiento = desapilar(movimientos)

    direccion = movimiento[0]
    pasos = movimiento[1]

    if direccion == "norte":
        regreso = "sur"

    elif direccion == "sur":
        regreso = "norte"

    elif direccion == "este":
        regreso = "oeste"

    elif direccion == "oeste":
        regreso = "este"

    elif direccion == "noreste":
        regreso = "suroeste"

    elif direccion == "noroeste":
        regreso = "sureste"

    elif direccion == "sureste":
        regreso = "noroeste"

    elif direccion == "suroeste":
        regreso = "noreste"

    print("Mover", pasos, "pasos hacia", regreso)