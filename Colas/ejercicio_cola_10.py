"""10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
resolver las siguientes actividades:
a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
la palabra "Python", sin perder datos en la cola;
c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
11:43 y las 15:57, y determinar cuántas son."""

from .tda_cola import cola, arribo, atencion, cola_vacia
from Pilas.tda_pila import pila, apilar, desapilar, pila_vacia
from .validaciones import validar_numero, validar_string

mi_cola = cola()

corte = validar_numero("Desea ingresar una notificacion: 1=Si, 0=Salir: ")
while corte != 0 and corte != 1:
    print("Numero invalido")
    corte = validar_numero("Desea ingresar una notificacion: 1=Si, 0=Salir: ")

while corte != 0:

    hora = input("Ingrese la hora formato(24hs): (HH:MM): ")
    aplicacion = input("Ingrese la aplicacion: ")
    mensaje = input("Ingrese el mensaje: ")

    notificacion = {
        "hora": hora,
        "aplicacion": aplicacion,
        "mensaje": mensaje
    }

    arribo(mi_cola, notificacion)

    corte = validar_numero("Desea ingresar otra notificacion: 1=Si, 0=Salir: ")
    while corte != 0 and corte != 1:
        print("Numero invalido")
        corte = validar_numero("Desea ingresar otra notificacion: 1=Si, 0=Salir: ")


# -------------------- Punto A --------------------

cola_auxiliar = cola()

while cola_vacia(mi_cola) == False:

    dato = atencion(mi_cola)

    if dato["aplicacion"] != "Facebook":
        arribo(cola_auxiliar, dato)

while cola_vacia(cola_auxiliar) == False:
    arribo(mi_cola, atencion(cola_auxiliar))


# -------------------- Punto B --------------------

cola_auxiliar = cola()

while cola_vacia(mi_cola) == False:

    dato = atencion(mi_cola)

    if dato["aplicacion"] == "Twitter" and "Python" in dato["mensaje"]:
        print(dato)

    arribo(cola_auxiliar, dato)

while cola_vacia(cola_auxiliar) == False:
    arribo(mi_cola, atencion(cola_auxiliar))


# -------------------- Punto C --------------------

cola_auxiliar = cola()
mi_pila = pila()

cantidad = 0

while cola_vacia(mi_cola) == False:

    dato = atencion(mi_cola)

    if dato["hora"] >= "11:43" and dato["hora"] <= "15:57":
        apilar(mi_pila, dato)
        cantidad += 1

    arribo(cola_auxiliar, dato)

while cola_vacia(cola_auxiliar) == False:
    arribo(mi_cola, atencion(cola_auxiliar))

print("Cantidad de notificaciones entre las 11:43 y las 15:57:", cantidad)

print("\nNotificaciones almacenadas en la pila:")

while pila_vacia(mi_pila) == False:
    print(desapilar(mi_pila))