"""20. Desarrollar un algoritmo para el control de un puesto de peaje (que posee 3 cabinas de cobro),
que resuelva las siguientes actividades:
a. agregar 30 vehículos de manera aleatoria a las cabinas de cobro, los tipos de vehículos son
los siguientes:
I. automóviles (tarifa $47);
II. camionetas (tarifa $59);
III. camiones (tarifa $71);
IV. colectivos (tarifa $64).
b. realizar la atención de las cabinas, considerando las tarifas del punto anterior.
c. determinar qué cabina recaudó mayor cantidad de pesos ($).
d. determinar cuántos vehículos de cada tipo se atendieron en cada cola."""

from .tda_cola import cola, arribo, atencion, cola_vacia
from random import randint


cabina1 = cola()
cabina2 = cola()
cabina3 = cola()



# ---------------- Crear vehículo ----------------

def crear_vehiculo():
    tipo = randint(1,4)

    if tipo == 1:
        return ["automovil", 47]
    elif tipo == 2:
        return ["camioneta", 59]
    elif tipo == 3:
        return ["camion", 71]
    else:
        return ["colectivo", 64]

# ---------------- Punto A ----------------

print("Carga de vehículos")

for i in range(30):
    vehiculo = crear_vehiculo()
    cabina = randint(1,3)

    if cabina == 1:
        arribo(cabina1, vehiculo)
    elif cabina == 2:

        arribo(cabina2, vehiculo)
    else:
        arribo(cabina3, vehiculo)



# ---------------- Punto B ----------------

def atender_cabina(cabina):
    recaudacion = 0
    autos = 0
    camionetas = 0
    camiones = 0
    colectivos = 0

    while cola_vacia(cabina) == False:
        vehiculo = atencion(cabina)
        print(
            "Vehículo:",
            vehiculo[0],
            "- Tarifa:",
            vehiculo[1]
        )
        recaudacion += vehiculo[1]
        if vehiculo[0] == "automovil":
            autos += 1

        elif vehiculo[0] == "camioneta":
            camionetas += 1

        elif vehiculo[0] == "camion":
            camiones += 1
            
        elif vehiculo[0] == "colectivo":
            colectivos += 1

    return recaudacion, autos, camionetas, camiones, colectivos

# Atención de las tres cabinas

print("\nAtención cabina 1")
recaudacion1, autos1, camionetas1, camiones1, colectivos1 = atender_cabina(cabina1)
print("\nAtención cabina 2")
recaudacion2, autos2, camionetas2, camiones2, colectivos2 = atender_cabina(cabina2)
print("\nAtención cabina 3")
recaudacion3, autos3, camionetas3, camiones3, colectivos3 = atender_cabina(cabina3)

# ---------------- Punto C ----------------

print("\nRecaudación")
print("Cabina 1:", recaudacion1)
print("Cabina 2:", recaudacion2)
print("Cabina 3:", recaudacion3)

if recaudacion1 > recaudacion2 and recaudacion1 > recaudacion3:
    print("La cabina con mayor recaudación fue la cabina 1")

elif recaudacion2 > recaudacion3:
    print("La cabina con mayor recaudación fue la cabina 2")

else:
    print("La cabina con mayor recaudación fue la cabina 3")

# ---------------- Punto D ----------------

print("\nVehículos atendidos por cabina")
print("\nCabina 1")
print("Automóviles:", autos1)
print("Camionetas:", camionetas1)
print("Camiones:", camiones1)
print("Colectivos:", colectivos1)

print("\nCabina 2")
print("Automóviles:", autos2)
print("Camionetas:", camionetas2)
print("Camiones:", camiones2)
print("Colectivos:", colectivos2)

print("\nCabina 3")
print("Automóviles:", autos3)
print("Camionetas:", camionetas3)
print("Camiones:", camiones3)
print("Colectivos:", colectivos3)