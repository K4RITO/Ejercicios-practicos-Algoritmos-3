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
from tda_pila import pila, apilar, desapilar, pila_vacia


trajes = pila()
aux = pila()


# CARGA
corte = 1

while corte != 0:

    modelo = input("Ingrese modelo: ")
    pelicula = input("Ingrese pelicula: ")
    estado = input("Ingrese estado: ")

    repetido = False

    # verificar repetidos
    while not pila_vacia(trajes):

        dato = desapilar(trajes)

        if dato[0] == modelo and dato[1] == pelicula:
            repetido = True

        apilar(aux, dato)

    # restaurar
    while not pila_vacia(aux):
        apilar(trajes, desapilar(aux))


    if repetido == False:

        traje = [modelo, pelicula, estado]

        apilar(trajes, traje)

    else:
        print("Ese modelo ya existe en esa pelicula")


    corte = int(input("Desea ingresar otro? 1 = SI / 0 = NO: "))


# agregar Mark LXXXV
repetido = False

while not pila_vacia(trajes):

    dato = desapilar(trajes)

    if dato[0] == "Mark LXXXV" and dato[1] == "Avengers: Endgame":
        repetido = True

    apilar(aux, dato)


while not pila_vacia(aux):
    apilar(trajes, desapilar(aux))


if repetido == False:

    apilar(trajes, ["Mark LXXXV", "Avengers: Endgame", "Impecable"])


# RECORRIDO
hulkbuster = False

while not pila_vacia(trajes):

    dato = desapilar(trajes)

    modelo = dato[0]
    pelicula = dato[1]
    estado = dato[2]


    # a
    if modelo == "Mark XLIV":

        hulkbuster = True

        print("Hulkbuster usada en:", pelicula)


    # b
    if estado.lower() == "dañado":

        print("Traje dañado:", modelo)


    # c
    if estado.lower() == "destruido":

        print("Eliminando traje destruido:", modelo)

    else:
        apilar(aux, dato)


    # f
    if pelicula == "Spider-Man: Homecoming" or pelicula == "Capitan America: Civil War":

        print("Traje usado en", pelicula, ":", modelo)


# restaurar sin destruidos
while not pila_vacia(aux):

    apilar(trajes, desapilar(aux))


if hulkbuster == False:
    print("No se utilizo Hulkbuster")