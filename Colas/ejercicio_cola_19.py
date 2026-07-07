"""19. Modificar las funciones de arribo y atención del TDA cola para adaptarlo a una cola circular,
que no necesite la función mover al final; y desarrollar un función que permita realizar un barrido de dicha estructura respetando el principio de funcionamiento de la cola."""

from .tda_cola import cola, nodocola, arribo, atencion, cola_vacia, tamanio, barrido,en_frente
from .validaciones import validar_numero

def atencion_cir(cola):
    """ABSTRACCION: Atiende el elemento en el frente de la cola circular y lo devuelve."""
    if cola_vacia(cola):
        return
    dato = cola.frente.info
    if cola.frente == cola.final:    
        cola.frente = None
        cola.final = None
    else:
        cola.frente = cola.frente.sig
        cola.final.sig = cola.frente 
    cola.tamanio -= 1
    return dato

def arribo_cir(cola, dato):
    """ABSTRACCION: Arriba el dato al final de la cola circular."""
    nodo = nodocola()
    nodo.info = dato
    if cola.frente is None:
        cola.frente = nodo
        nodo.sig = cola.frente       
    else:
        cola.final.sig = nodo
        nodo.sig = cola.frente       
    cola.final = nodo
    cola.tamanio += 1

def mover_al_final_cir(cola):
    """ABSTRACCION: Hace que los punteros cola.final y cola.frente apunten al nodo siguiente y devuelve el dato que estaba en el frente"""
    dato = cola.frente.info
    cola.final = cola.frente         
    cola.frente = cola.frente.sig    
    return dato

def barrido_cir(cola):
    """ABSTRACCION: Recorre una cola circular sin modificar su estructura."""
    if cola_vacia(cola):
        return
    
    aux = cola.frente
    while True:
        print(aux.info)

        aux = aux.sig

        if aux == cola.frente:
            break

mi_cola = cola()

while(True):
    opcion = validar_numero("Opciones: 1 - Agregar dato, 2 - Eliminar dato, 3 - Mostrar datos, 0 - Salir: ")
    if (opcion == 1):
        dato = input("Escriba el dato a ingresar: ")
        arribo_cir(mi_cola, dato)
    if (opcion == 2):
        dato = atencion_cir(mi_cola)
        print(dato)
    if (opcion == 3):
        barrido_cir(mi_cola)
    if (opcion == 0): break