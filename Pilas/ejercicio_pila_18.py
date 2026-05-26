"""Dada una pila de objetos de una oficina de los que se dispone de su nombre y peso(por ejemplo monitor 1kg, teclado 0.25kg, silla 7kg, etc.), ordenar dicha pila de acuerdo a su peso del objeto mas liviano al mas pesado. Solo pueden utilizar pilas auxiliares como estructuras extras,no se pueden utilizar métodos de ordenamiento."""
from tda_pila import nodopila, pila, apilar, desapilar, pila_vacia, en_cima, barrido

mi_pila = pila()
pila_auxiliar = pila()
corte = 1

while corte != 0:
    item = input("Ingrese el nombre del objeto: ")
    peso = float(input("Ingrese el peso del objeto en kg: "))
    objeto = [item, peso]
    apilar(mi_pila, objeto)
    corte = int(input("Desea ingresar otro? 1 = SI / 0 = NO: "))

while  pila_vacia(mi_pila) == False:
    dato = desapilar(mi_pila)
    while  pila_vacia(pila_auxiliar) == False and en_cima(pila_auxiliar)[1] > dato[1]:
        apilar(mi_pila, desapilar(pila_auxiliar))
    apilar(pila_auxiliar, dato)

print("\nPila ordenada:")
barrido(pila_auxiliar)

