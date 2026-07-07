"""15. Suponga que se escapa hacia el planeta tierra en un Caza TIE robado huyendo de un Destruc-
tor Estelar y necesita localizar la base rebelde más cercana y se tiene una cola con informa-
ción de las bases rebeldes en la tierra de las cuales conoce su nombre, número de flota aérea,

coordenadas de latitud y longitud. Desarrolle un algoritmo que permita resolver las siguientes
tareas una vez que aterrice:
a. determinar cuál es la base rebelde más cercana desde su posición actual.
b. para el cálculo de la distancia deberá utilizar la fórmula de Haversine:

donde r es el radio medio de la tierra en metros (6371000), φ1 y φ2 las latitudes de los
dos puntos por ejemplo coordenadas actual, λ1 y λ2 las longitudes de los dos puntos
coordenadas de la base ambos expresadas en radianes; para convertir de grados a
radianes utilice la función math.radians(ángulo coordenada).

c. mostrar el nombre y la distancia a la que se encuentran las tres bases más cercanas y deter-
minar cual tiene mayor flota aérea.

d. determinar la distancia hasta la base rebelde con mayor flota aérea."""

from .tda_cola import cola, arribo, atencion, cola_vacia
from .validaciones import validar_numero, validar_string,validar_float
import math

mi_cola = cola()
cola_auxiliar = cola()



latitud_actual = validar_float("Ingrese la latitud actual: ")
longitud_actual = validar_float("Ingrese la longitud actual: ")



corte = validar_numero("Desea ingresar una base: 1=Si, 0=Salir: ")
while corte != 0 and corte != 1:
    print("Numero invalido")
    corte = validar_numero("Desea ingresar una base: 1=Si, 0=Salir: ")

while corte != 0:

    nombre = validar_string("Ingrese el nombre de la base: ")
    flota = validar_numero("Ingrese la cantidad de naves de la flota: ")
    latitud = validar_float("Ingrese la latitud: ")
    longitud = validar_float("Ingrese la longitud: ")

    base = {
        "nombre": nombre,
        "flota": flota,
        "latitud": latitud,
        "longitud": longitud
    }

    arribo(mi_cola, base)

    corte = validar_numero("Desea ingresar otra base: 1=Si, 0=Salir: ")
    while corte != 0 and corte != 1:
        print("Numero invalido")
        corte = validar_numero("Desea ingresar otra base: 1=Si, 0=Salir: ")



radio = 6371000

distancia_minima = None
base_cercana = None

primera = None
segunda = None
tercera = None

distancia_primera = None
distancia_segunda = None
distancia_tercera = None

mayor_flota = None
base_mayor_flota = None
distancia_mayor_flota = None

while cola_vacia(mi_cola) == False:

    dato = atencion(mi_cola)

    phi1 = math.radians(latitud_actual)
    phi2 = math.radians(dato["latitud"])

    lambda1 = math.radians(longitud_actual)
    lambda2 = math.radians(dato["longitud"])

    a = math.sin((phi2 - phi1) / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin((lambda2 - lambda1) / 2) ** 2

    distancia = 2 * radio * math.asin(math.sqrt(a))

    # Punto A

    if distancia_minima == None or distancia < distancia_minima:
        distancia_minima = distancia
        base_cercana = dato

    # Punto C

    if distancia_primera == None or distancia < distancia_primera:

        tercera = segunda
        distancia_tercera = distancia_segunda

        segunda = primera
        distancia_segunda = distancia_primera

        primera = dato
        distancia_primera = distancia

    elif distancia_segunda == None or distancia < distancia_segunda:

        tercera = segunda
        distancia_tercera = distancia_segunda

        segunda = dato
        distancia_segunda = distancia

    elif distancia_tercera == None or distancia < distancia_tercera:

        tercera = dato
        distancia_tercera = distancia

    # Punto D

    if mayor_flota == None or dato["flota"] > mayor_flota:

        mayor_flota = dato["flota"]
        base_mayor_flota = dato
        distancia_mayor_flota = distancia

    arribo(cola_auxiliar, dato)

while cola_vacia(cola_auxiliar) == False:
    arribo(mi_cola, atencion(cola_auxiliar))

# Punto A

print("\nBase mas cercana")
print("Nombre:", base_cercana["nombre"])
print("Distancia:", round(distancia_minima, 2), "metros")

# Punto C

print("\nTres bases mas cercanas")

if primera != None:
    print(primera["nombre"], "-", round(distancia_primera, 2), "metros")

if segunda != None:
    print(segunda["nombre"], "-", round(distancia_segunda, 2), "metros")

if tercera != None:
    print(tercera["nombre"], "-", round(distancia_tercera, 2), "metros")

mayor = primera

if segunda != None and segunda["flota"] > mayor["flota"]:
    mayor = segunda

if tercera != None and tercera["flota"] > mayor["flota"]:
    mayor = tercera

print("\nLa mayor flota entre las tres bases cercanas pertenece a:")
print(mayor["nombre"])
print("Flota:", mayor["flota"])

# Punto D

print("\nBase con mayor flota aerea")
print("Nombre:", base_mayor_flota["nombre"])
print("Flota:", base_mayor_flota["flota"])
print("Distancia:", round(distancia_mayor_flota, 2), "metros")