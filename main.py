import subprocess

ejercicios = {
    "Pilas": {
        1: [
            "python",
            "-m"
            "Pilas.ejercicio_pila_1"
        ],

        2: [
            "python",
            "-m"
            "Pilas.ejercicio_pila_2"
        ],

        3: [
            "python",
            "-m"
            "Pilas.ejercicio_pila_3"
        ],

        4: [
            "python",
            "-m"
            "Pilas.ejercicio_pila_4"
        ],

        5: [
            "python",
            "-m"
            "Pilas.ejercicio_pila_5"
        ],

        6: [
            "python",
            "-m"
            "Pilas.ejercicio_pila_6"
        ],

        7: [
            "python",
            "-m"
            "Pilas.ejercicio_pila_7"
        ],

        8: [
            "python",
            "-m"
            "Pilas.ejercicio_pila_8"
        ],

        9: [
            "python",
            "-m"
            "Pilas.ejercicio_pila_9"
        ],

        11: [
            "python",
            "-m"
            "Pilas.ejercicio_pila_11"
        ],

        13: [
            "python",
            "-m"
            "Pilas.ejercicio_pila_13"
        ],

        14: [
            "python",
            "-m"
            "Pilas.ejercicio_pila_14"
        ],

        17: [
            "python",
            "-m"
            "Pilas.ejercicio_pila_17"

        ],
        18: [
            "python",
            "-m"
            "Pilas.ejercicio_pila_18"
        ],
        20: [
            "python",
            "-m"
            "Pilas.ejercicio_pila_20"

        ],
        23: [
            "python",
            "-m"
            "Pilas.ejercicio_pila_23"
        ],
    },
    
    "Colas": {
        1: [
        "python",
        "-m",
        "Colas.ejercicio_cola_1"
    ],
        2: [
    "python",
    "-m",
    "Colas.ejercicio_cola_2"
    ],
       3: [
    "python",
    "-m",
    "Colas.ejercicio_cola_3"
    ],
       4: [
    "python",
    "-m",
    "Colas.ejercicio_cola_4"
    ],
           5: [
    "python",
    "-m",
    "Colas.ejercicio_cola_5"
    ],
    
    
},
    
}


lista_ejercicios_pilas = """
1: Ocurrencias de un elemento
2: Eliminar elementos impares
3: Reemplazar ocurrencias de un elemento
4: Invertir una pila
5: Palíndromo
6: Palabra inversa
7: Eliminar elemento i-ésimo
8: Pila de cartas
9: Factorial con pila
11: determinar vocales
13: trajes de iron-man
14: ordenamiento creciente
17: separar parrafo
18: ordenamiento de objetos de oficina
20: movimiento de robot
23: temperatura promedio de abril
"""
lista_ejercicios_colas = """
1: Eliminar vocales
2: Invertir el contenido de una cola
3: Palíndromo
4: Eliminar numero NO primos
5: Invertir el contenido de una pila
"""

print("Bienvenido al sistema de ejercicios")
while (True):
    print("")
    opcion = input("Ingrese el nombre del tipo ejercicios desea ver (Pilas),(Colas): ").lower()
    if (opcion == "pilas"):
        print(lista_ejercicios_pilas)
        opcion = int(input("Escriba el numero del ejercicio que desea ejecutar: "))
        subprocess.run(ejercicios["Pilas"][opcion])
    elif (opcion == "colas"):
        print(lista_ejercicios_colas)
        opcion = int(input("Escriba el numero del ejercicio que desea ejecutar: "))
        subprocess.run(ejercicios["Colas"][opcion])
        