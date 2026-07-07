"""16. Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
siguiente situación:
a. cargue tres documentos de empleados (cada documento se representa solamente con
un nombre).
b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
c. cargue dos documentos del staff de TI.
d. cargue un documento del gerente.
e. imprima los dos primeros documentos de la cola.
f. cargue dos documentos de empleados y uno de gerente.
g. imprima todos los documentos de la cola de impresión."""

from .tda_cola import cola, arribo, atencion, cola_vacia
from .validaciones import validar_string

cola_empleados = cola()
cola_ti = cola()
cola_gerente = cola()

# ---------------- Punto A ----------------

print("Carga de documentos de empleados")

for i in range(3):

    nombre = validar_string("Ingrese el nombre del documento: ")
    arribo(cola_empleados, nombre)

# ---------------- Punto B ----------------

print("\nPrimer documento impreso:")

if cola_vacia(cola_gerente) == False:
    print(atencion(cola_gerente))
elif cola_vacia(cola_ti) == False:
    print(atencion(cola_ti))
else:
    print(atencion(cola_empleados))

# ---------------- Punto C ----------------

print("\nCarga de documentos del personal de TI")

for i in range(2):

    nombre = validar_string("Ingrese el nombre del documento: ")
    arribo(cola_ti, nombre)

# ---------------- Punto D ----------------

print("\nCarga de documento del gerente")

nombre = validar_string("Ingrese el nombre del documento: ")
arribo(cola_gerente, nombre)

# ---------------- Punto E ----------------

print("\nSe imprimen dos documentos:")

for i in range(2):

    if cola_vacia(cola_gerente) == False:
        print(atencion(cola_gerente))
    elif cola_vacia(cola_ti) == False:
        print(atencion(cola_ti))
    elif cola_vacia(cola_empleados) == False:
        print(atencion(cola_empleados))

# ---------------- Punto F ----------------

print("\nCarga de dos documentos de empleados")

for i in range(2):

    nombre = validar_string("Ingrese el nombre del documento: ")
    arribo(cola_empleados, nombre)

print("\nCarga de un documento del gerente")

nombre = validar_string("Ingrese el nombre del documento: ")
arribo(cola_gerente, nombre)

# ---------------- Punto G ----------------

print("\nImpresion de todos los documentos:")

while cola_vacia(cola_gerente) == False or cola_vacia(cola_ti) == False or cola_vacia(cola_empleados) == False:

    if cola_vacia(cola_gerente) == False:
        print(atencion(cola_gerente))

    elif cola_vacia(cola_ti) == False:
        print(atencion(cola_ti))

    else:
        print(atencion(cola_empleados))