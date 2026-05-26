"""Dada una pila con los valores promedio de temperatura ambiente de cada día del mes de abril,
obtener la siguiente información sin perder los datos:
a. determinar el rango de temperatura del mes, temperatura mínima y máxima;
b. calcular el promedio de temperatura (o media) del total de valores;
c. determinar la cantidad de valores por encima y por debajo de la media."""
from tda_pila import nodopila, pila, apilar, desapilar, pila_vacia

temperaturas = pila()
aux = pila()

# CARGA
for i in range(30):

    temp = float(input("Ingrese temperatura del dia: "))
    apilar(temperaturas, temp)


# VARIABLES
suma = 0
cantidad = 0
encima_media = 0
debajo_media = 0

bandera = True


# RECORRIDO PARA MAX, MIN Y MEDIA
while not pila_vacia(temperaturas):

    dato = desapilar(temperaturas)

    apilar(aux, dato)

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


# RECORRIDO PARA ENCIMA/DEBAJO DE LA MEDIA
while not pila_vacia(aux):

    dato = desapilar(aux)

    apilar(temperaturas, dato)

    if dato > media:
        encima_media += 1

    elif dato < media:
        debajo_media += 1


# RESULTADOS
print("Temperatura maxima:", maxima)
print("Temperatura minima:", minima)

print("Rango termico:", maxima - minima)

print("Media:", media)

print("Cantidad encima de la media:", encima_media)

print("Cantidad debajo de la media:", debajo_media)