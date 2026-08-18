"""
Diseñar un algoritmo que permita contar la cantidad de nodos de una lista
"""

from .tda_lista import insertar, lista_vacia, eliminar, barrido, tamanio, buscar, criterio, buscar_criterio, insertar_criterio, eliminar_criterio, Lista, nodoLista



lista = Lista()

while (True):
    opcion = input("Desea ingresar un dato a la lista?, Si para ingresar, No para salir: ").lower()

    if (opcion == "no"): 
        break
    elif (opcion == "si"):
        dato = input("Ingrese el dato que quiere guardar: ")
        insertar(lista, dato)
    else: 
        print("La opcion ingresada no esta dentro de las opciones listadas.")

cantidad_nodos = tamanio(lista)

if (cantidad_nodos == 0):
    print("No hay nodos en la lista, no se ingreso ningun dato a esta.")
else:
    print(f"La cantidad de nodos en la lista es de {cantidad_nodos} {"Nodos" if cantidad_nodos != 1 else "Nodo"}.")