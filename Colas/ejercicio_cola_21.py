"""21. Desarrollar un algoritmo que permita administrar los despegues y aterrizajes de un aeropuerto que tiene una pista, contemplando las siguientes actividades:

a. de cada vuelo se conoce el nombre de la empresa, hora salida, hora llegada, aeropuerto de
origen, aeropuerto de destino y su tipo (pasajeros, negocios o carga).

b. utilizar una cola para administrar los despegues, se deben cargan ordenados por horario de
salida. Otra para los aterrizajes, se deben agregan a medida que arriban al aeropuerto.

c. en la pista solo puede haber un avión realizando una maniobra de aterrizaje o despegue.

d. se debe permitir agregar vuelos tanto de aterrizaje como de despegue en ambas colas des-
pués de realizar una atención.

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
from .validaciones import validar_numero, validar_string


cola_despegues = cola()
cola_aterrizajes = cola()
cola_auxiliar = cola()

# ---------------- Carga de vuelos de despegue ----------------

cantidad = validar_numero("Ingrese cantidad de vuelos de despegue: ")

for i in range(cantidad):

    print("\nVuelo", i+1)

    empresa = validar_string("Empresa: ")
    salida = input("Hora salida(HH:MM) formato 24hs :")
    llegada = input("Hora llegada(HH:MM) formato 24hs :")
    origen = validar_string("Aeropuerto origen: ")
    destino = validar_string("Aeropuerto destino: ")
    tipo = validar_string("Tipo (pasajeros/negocios/carga): ")

    vuelo = {
        "empresa": empresa,
        "salida": salida,
        "llegada": llegada,
        "origen": origen,
        "destino": destino,
        "tipo": tipo
    }

    #Punto B 

    insertado = False

    while cola_vacia(cola_despegues) == False:
        dato = atencion(cola_despegues)
        if vuelo["salida"] < dato["salida"] and insertado == False:
            arribo(cola_auxiliar,vuelo)
            insertado = True

        arribo(cola_auxiliar,dato)

    if insertado == False:
        arribo(cola_auxiliar,vuelo)

    while cola_vacia(cola_auxiliar) == False:
        arribo(cola_despegues,atencion(cola_auxiliar))

# ---------------- Carga de aterrizajes ----------------

cantidad = validar_numero("Ingrese cantidad de vuelos de aterrizaje: ")

for i in range(cantidad):

    print("\nVuelo", i+1)

    empresa = validar_string("Empresa: ")
    salida = input("Hora salida (HH:MM) formato 24hs: ")
    llegada = input("Hora llegada (HH:MM) formato 24hs: ")
    origen = validar_string("Aeropuerto origen: ")
    destino = validar_string("Aeropuerto destino: ")
    tipo = validar_string("Tipo (pasajeros/negocios/carga): ")

    vuelo = {

        "empresa": empresa,
        "salida": salida,
        "llegada": llegada,
        "origen": origen,
        "destino": destino,
        "tipo": tipo
    }

    arribo(cola_aterrizajes,vuelo)

#Punto E

hora_actual = input("\nIngrese hora actual (HH:MM) formato 24hs: ")
atender = None

if cola_vacia(cola_aterrizajes) == False:

    if cola_vacia(cola_despegues) == False:
        primero = en_frente(cola_despegues)
        if primero["salida"] == hora_actual:
            atender = "despegue"

    if atender == None:
        atender = "aterrizaje"

elif cola_vacia(cola_despegues) == False:
    atender = "despegue"



# ---------------- Atención pista ----------------


if atender == "aterrizaje":
    vuelo = atencion(cola_aterrizajes)
    print("\nAterrizando avión")
    print("Empresa:", vuelo["empresa"])

    # Punto F

    if vuelo["tipo"] == "pasajeros":
        tiempo = 10
    elif vuelo["tipo"] == "negocios":
        tiempo = 5
    else:
        tiempo = 12
    print("Tiempo de pista:", tiempo, "segundos")

elif atender == "despegue":
    vuelo = atencion(cola_despegues)
    print("\nDespegando avión")
    print("Empresa:", vuelo["empresa"])

    # Punto F

    if vuelo["tipo"] == "pasajeros":
        tiempo = 5
    elif vuelo["tipo"] == "negocios":
        tiempo = 3
    else:
        tiempo = 9
    print("Tiempo de pista:", tiempo, "segundos")

else:
    print("No hay vuelos para atender")

#Punto G

opcion = validar_numero("Cancelar vuelo de despegue? 1-Si 0-No: ")

while opcion != 0 and opcion != 1:
    print("Numero invalido")
    opcion = validar_numero("Cancelar vuelo de despegue? 1-Si 0-No: ")


if opcion == 1:

    empresa_cancelar = validar_string("Ingrese empresa del vuelo: ")
    encontrado = False

    while cola_vacia(cola_despegues) == False:
        vuelo = atencion(cola_despegues)
        if vuelo["empresa"] == empresa_cancelar and encontrado == False:
            encontrado = True
            print("Vuelo cancelado")
        else:
            arribo(cola_auxiliar,vuelo)

    while cola_vacia(cola_auxiliar) == False:
        arribo(cola_despegues,atencion(cola_auxiliar))

# Reprogramar vuelo al momento del despegue

opcion = validar_numero("\Reprogramar vuelo? 1-Si 0-No: ")
while opcion != 0 and opcion != 1:
    print("Numero invalido")
    opcion = validar_numero("Reprogramar vuelo? 1-Si 0-No: ")

if opcion == 1:
    vuelo = atencion(cola_despegues)
    ultima_hora = vuelo["salida"]
    while cola_vacia(cola_despegues) == False:
        dato = atencion(cola_despegues)
        if dato["salida"] > ultima_hora:
            ultima_hora = dato["salida"]

        arribo(cola_auxiliar,dato)

    while cola_vacia(cola_auxiliar) == False:
        arribo(cola_despegues,atencion(cola_auxiliar))

    vuelo["salida"] = ultima_hora + 1
    arribo(cola_despegues,vuelo)
    print("Vuelo reprogramado para:",vuelo["salida"])

print("\nDespegues pendientes")

while cola_vacia(cola_despegues) == False:
    vuelo = atencion(cola_despegues)
    print(vuelo["empresa"],"- salida:",vuelo["salida"])

print("\nAterrizajes pendientes")

while cola_vacia(cola_aterrizajes) == False:
    vuelo = atencion(cola_aterrizajes)
    print(vuelo["empresa"],"- llegada:",vuelo["llegada"])