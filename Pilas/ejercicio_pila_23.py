"""Dada una pila con los valores promedio de temperatura ambiente de cada día del mes de abril,
obtener la siguiente información sin perder los datos:
a. determinar el rango de temperatura del mes, temperatura mínima y máxima;
b. calcular el promedio de temperatura (o media) del total de valores;
c. determinar la cantidad de valores por encima y por debajo de la media."""
from .tda_pila import nodopila, pila, apilar, desapilar, pila_vacia

temperaturas = pila()
pila_auxiliar = pila()
contador = 1
for i in range(30):

    temp = float(input(f"Ingrese temperatura del dia {contador} de abril: "))
    contador +=1
    apilar(temperaturas, temp)

suma = 0
cantidad = 0
encima_media = 0
debajo_media = 0
bandera = True

while pila_vacia(temperaturas) == False:
    dato = desapilar(temperaturas)
    apilar(pila_auxiliar, dato)
    suma += dato
    cantidad += 1

    if bandera:
        maxima = dato
        minima = dato
        bandera = False
    else:
        if dato > maxima:
            maxima = dato
        if dato < minima:
            minima = dato

media = suma / cantidad

while pila_vacia(pila_auxiliar) == False:
    dato = desapilar(pila_auxiliar)
    apilar(temperaturas, dato)

    if dato > media:
        encima_media += 1

    elif dato < media:
        debajo_media += 1

print("Temperatura maxima:", maxima)
print("Temperatura minima:", minima)
print("Rango termico:", maxima - minima)
print("Media:", media)
print("Cantidad encima de la media:", encima_media)
print("Cantidad debajo de la media:", debajo_media)