"""21. Desarrollar un algoritmo que permita administrar los despegues y aterrizajes de un aeropuer
to que tiene una pista, contemplando las siguientes actividades:

a. de cada vuelo se conoce el nombre de la empresa, hora salida, hora llegada, aeropuerto de
origen, aeropuerto de destino y su tipo (pasajeros, negocios o carga).

b. utilizar una cola para administrar los despegues, se deben cargan ordenados por horario de
salida. Otra para los aterrizajes, se deben agregan a medida que arriban al aeropuerto.

c. en la pista solo puede haber un avión realizando una maniobra de aterrizaje o despegue.

d. se debe permitir agregar vuelos tanto de aterrizaje como de despegue en ambas colas después de realizar una atención.

e. se debe atender siempre que se pueda a los elementos de la cola de aterrizaje dado que son
aviones que están sobrevolando en la zona de espera, salvo que sea el horario de salida del
primer avión de la cola de despegue, en ese caso se deberá atender dicho despegue.

f. cada tipo de avión tiene su tiempo de uso de la pista para la maniobra de despegue y aterrizaje adaptados a segundo para los fines prácticos del ejercicio:

I. pasajeros (aterrizaje = 10 segundos, despegue = 5 segundos);
II. negocios (aterrizaje = 5 segundos, despegue = 3 segundos);
III. carga (aterrizaje = 12 segundos, despegue = 9 segundos).

g. se debe poder cancelar vuelos de despegue y poder reprogramar un vuelo para más tarde
cuando se lo atiende para despegar (en esta caso el horario de salida será mayor que el
último de la cola)."""

from .tda_cola import cola, arribo, atencion, cola_vacia, en_frente
from .validaciones import validar_string, validar_numero


cola_despegues = cola()
cola_aterrizajes = cola()



# ---------------- Crear vuelo ----------------

def cargar_vuelo():

    vuelo = []

    empresa = validar_string("Empresa: ")
    salida = validar_numero("Hora salida: ")
    llegada = validar_numero("Hora llegada: ")
    origen = validar_string("Aeropuerto origen: ")
    destino = validar_string("Aeropuerto destino: ")
    tipo = validar_string("Tipo (pasajeros/negocios/carga): ")


    vuelo.append(empresa)
    vuelo.append(salida)
    vuelo.append(llegada)
    vuelo.append(origen)
    vuelo.append(destino)
    vuelo.append(tipo)


    return vuelo



# ---------------- Insertar despegue ordenado ----------------

def insertar_despegue(cola_despegues, vuelo):

    if cola_vacia(cola_despegues):

        arribo(cola_despegues, vuelo)


    else:

        cola_aux = cola()
        insertado = False


        while cola_vacia(cola_despegues) == False:

            dato = atencion(cola_despegues)


            if vuelo[1] < dato[1] and insertado == False:

                arribo(cola_aux, vuelo)

                insertado = True


            arribo(cola_aux, dato)



        if insertado == False:

            arribo(cola_aux, vuelo)



        while cola_vacia(cola_aux) == False:

            arribo(
                cola_despegues,
                atencion(cola_aux)
            )



# ---------------- Tiempo pista ----------------

def tiempo_pista(vuelo, maniobra):


    tipo = vuelo[5]


    if tipo == "pasajeros":

        if maniobra == "aterrizaje":
            return 10
        else:
            return 5



    elif tipo == "negocios":

        if maniobra == "aterrizaje":
            return 5
        else:
            return 3



    elif tipo == "carga":

        if maniobra == "aterrizaje":
            return 12
        else:
            return 9




# ---------------- Elegir atención ----------------

def prioridad_pista(hora_actual):


    if cola_vacia(cola_aterrizajes) == False:


        if cola_vacia(cola_despegues) == False:


            vuelo = en_frente(cola_despegues)


            if vuelo[1] == hora_actual:

                return "despegue"


        return "aterrizaje"



    elif cola_vacia(cola_despegues) == False:

        return "despegue"



    return None



# ---------------- Punto A ----------------

print("Carga de vuelos de despegue")


cantidad = validar_numero("Cantidad de vuelos: ")


for i in range(cantidad):

    print("\nVuelo", i+1)

    vuelo = cargar_vuelo()

    insertar_despegue(
        cola_despegues,
        vuelo
    )



# ---------------- Punto B ----------------

print("\nCarga de vuelos de aterrizaje")


cantidad = validar_numero("Cantidad de vuelos: ")


for i in range(cantidad):

    print("\nVuelo", i+1)


    vuelo = cargar_vuelo()


    arribo(
        cola_aterrizajes,
        vuelo
    )



# ---------------- Punto C, D, E ----------------

print("\nAtención de pista")


hora = validar_numero("Hora actual: ")


accion = prioridad_pista(hora)



if accion == "aterrizaje":


    vuelo = atencion(cola_aterrizajes)


    print("\nAterrizando avión:")
    print("Empresa:", vuelo[0])

    print(
        "Tiempo pista:",
        tiempo_pista(vuelo,"aterrizaje"),
        "segundos"
    )



elif accion == "despegue":


    vuelo = atencion(cola_despegues)


    print("\nDespegando avión:")
    print("Empresa:", vuelo[0])


    print(
        "Tiempo pista:",
        tiempo_pista(vuelo,"despegue"),
        "segundos"
    )



else:

    print("No hay vuelos esperando")



# ---------------- Agregar nuevos vuelos ----------------

print("\nAgregar vuelo nuevo")


opcion = validar_numero(
    "1-Despegue  2-Aterrizaje  0-Salir: "
)


if opcion == 1:


    vuelo = cargar_vuelo()


    insertar_despegue(
        cola_despegues,
        vuelo
    )



elif opcion == 2:


    vuelo = cargar_vuelo()


    arribo(
        cola_aterrizajes,
        vuelo
    )



# ---------------- Barrido de colas ----------------

print("\nDespegues pendientes")


while cola_vacia(cola_despegues) == False:


    vuelo = atencion(cola_despegues)


    print(
        vuelo[0],
        "- salida:",
        vuelo[1]
    )



print("\nAterrizajes pendientes")


while cola_vacia(cola_aterrizajes) == False:


    vuelo = atencion(cola_aterrizajes)


    print(
        vuelo[0],
        "- llegada:",
        vuelo[2]
    )