"""Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Universe (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se
usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver
las siguientes actividades:
a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas, además mostrar el nombre de dichas películas;
b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
c. eliminar los modelos de los trajes destruidos mostrando su nombre;
d. un modelo de traje puede usarse en más de una película y en una película se pueden usar
más de un modelo de traje, estos deben cargarse por separado;
e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos
repetidos en una misma película;
f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y
“Capitan America: Civil War”."""
from .tda_pila import pila, apilar, desapilar, pila_vacia


trajes = pila()
pila_auxiliar = pila()

corte = 1

while corte != 0:

    modelo = input("Ingrese modelo: ")
    pelicula = input("Ingrese pelicula: ")
    estado = input("Ingrese estado: ")

    repetido = False

    while pila_vacia(trajes) == False:

        dato = desapilar(trajes)

        if dato[0] == modelo and dato[1] == pelicula:
            repetido = True

        apilar(pila_auxiliar, dato)

    while pila_vacia(pila_auxiliar) == False:
        apilar(trajes, desapilar(pila_auxiliar))


    if repetido == False:

        traje = [modelo, pelicula, estado]

        apilar(trajes, traje)

    else:
        print("Ese modelo ya existe en esa pelicula")


    corte = int(input("Desea ingresar otro? 1 = SI / 0 = NO: "))

repetido = False

while pila_vacia(trajes) == False:

    dato = desapilar(trajes)

    if dato[0] == "Mark LXXXV" and dato[1] == "Avengers: Endgame":
        repetido = True

    apilar(pila_auxiliar, dato)

while pila_vacia(pila_auxiliar) == False:
    apilar(trajes, desapilar(pila_auxiliar))


if repetido == False:

    apilar(trajes, ["Mark LXXXV", "Avengers: Endgame", "Impecable"])

hulkbuster = False

while pila_vacia(trajes) == False:

    dato = desapilar(trajes)

    modelo = dato[0]
    pelicula = dato[1]
    estado = dato[2]

    if modelo == "Mark XLIV":

        hulkbuster = True

        print("Hulkbuster usada en:", pelicula)

    if estado.lower() == "dañado":

        print("Traje dañado:", modelo)

    if estado.lower() == "destruido":

        print("Eliminando traje destruido:", modelo)
    else:
        apilar(pila_auxiliar, dato)

    if pelicula == "Spider-Man: Homecoming" or pelicula == "Capitan America: Civil War":

        print("Traje usado en", pelicula, ":", modelo)

while pila_vacia(pila_auxiliar) == False:

    apilar(trajes, desapilar(pila_auxiliar))

if hulkbuster == False:
    print("No se utilizo Hulkbuster")