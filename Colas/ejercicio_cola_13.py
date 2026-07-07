from .tda_cola import cola, arribo, atencion, cola_vacia, barrido
import random
import string

mi_cola = cola()
cola_digitos = cola()
cola_caracteres = cola()

caracteres = string.ascii_letters + string.digits + "?#@$%&"

for i in range(50000):

    dato = random.choice(caracteres)
    arribo(mi_cola, dato)

# ---------------- Punto A ----------------

while cola_vacia(mi_cola) == False:

    dato = atencion(mi_cola)

    if dato.isdigit():
        arribo(cola_digitos, dato)
    else:
        arribo(cola_caracteres, dato)

# ---------------- Punto B ----------------

cantidad_letras = 0
existe_interrogacion = False
existe_numeral = False

while cola_vacia(cola_caracteres) == False:

    dato = atencion(cola_caracteres)

    if dato.isalpha():
        cantidad_letras += 1

    if dato == "?":
        existe_interrogacion = True

    if dato == "#":
        existe_numeral = True

print("Cantidad de letras:", cantidad_letras)

if existe_interrogacion == True:
    print("Existe el caracter ?")
else:
    print("No existe el caracter ?")

if existe_numeral == True:
    print("Existe el caracter #")
else:
    print("No existe el caracter #")