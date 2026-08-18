"""
Dada una lista de números enteros eliminar de estas los números primos
"""
import math
from .validaciones import validar_numero
from .tda_lista import insertar, lista_vacia, eliminar, barrido, tamanio, buscar, criterio, buscar_criterio, insertar_criterio, eliminar_criterio, Lista, nodoLista

# ingreso de datos
lista = Lista()

def es_primo(n):
    """Calcula si un numero es primo y retorna un booleano que indica si es o no es."""
    if (n == 1): return False
    
    base = math.sqrt(n)
    contador = math.floor(base)
    
    while (contador >= 2):
        if (n % contador == 0):
            return False
        contador -= 1
    return True




while (True):
    opcion = input("Desea ingresar un numero a la lista?, Si para ingresar, No para salir: ").lower()

    if (opcion == "no"): 

        break
    elif (opcion == "si"):
        numero = validar_numero("Ingrese el numero que quiere guardar: ")
        insertar(lista, numero)        

    else:    

        print("La opcion ingresada no esta dentro de las opciones listadas.")


# separacion de listas
lista_no_primos = Lista()

aux = lista.inicio
while (aux is not None):
    if (not es_primo(aux.info)):
        insertar(lista_no_primos, aux.info)
    aux = aux.sig

if (lista_vacia(lista)):
    print("No se ingresaron datos, por lo tanto no hay listas que mostrar.")
else:
    print("Lista Original: ")
    barrido(lista)

    print("Lista sin numeros primos: ")
    barrido(lista_no_primos)