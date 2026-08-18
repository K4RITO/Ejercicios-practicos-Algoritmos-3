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
           6: [
    "python",
    "-m",
    "Colas.ejercicio_cola_6"
    ],
    7: [
    "python",
    "-m",
    "Colas.ejercicio_cola_7"
    ],
    8: [
    "python",
    "-m",
    "Colas.ejercicio_cola_8"
    ],
    9: [
    "python",
    "-m",
    "Colas.ejercicio_cola_9"
    ],
    10: [
    "python",
    "-m",
    "Colas.ejercicio_cola_10"
    ],
    12: [
    "python",
    "-m",
    "Colas.ejercicio_cola_12"
    ],
    13: [
    "python",
    "-m",
    "Colas.ejercicio_cola_13"
    ],
    14: [
    "python",
    "-m",
    "Colas.ejercicio_cola_14"
    ],
    15: [
    "python",
    "-m",
    "Colas.ejercicio_cola_15"
    ],
    16: [
    "python",
    "-m",
    "Colas.ejercicio_cola_16"
    ],
    18: [
    "python",
    "-m",
    "Colas.ejercicio_cola_18"
    ],
    19: [
    "python",
    "-m",
    "Colas.ejercicio_cola_19"
    ],
    20: [
    "python",
    "-m",
    "Colas.ejercicio_cola_20"
    ],
    21: [
    "python",
    "-m",
    "Colas.ejercicio_cola_21"
    ],
    },

    "Listas": {
    1: [
        "python",
        "-m",
        "Listas.ejercicio_lista_1"
    ],
    2: [
        "python",
        "-m",
        "Listas.ejercicio_lista_2"
    ],
    3: [
        "python",
        "-m",
        "Listas.ejercicio_lista_3"
    ],
    4: [
        "python",
        "-m",
        "Listas.ejercicio_lista_4"
    ],
    5: [
        "python",
        "-m",
        "Listas.ejercicio_lista_5"
    ],
    7: [
        "python",
        "-m",
        "Listas.ejercicio_lista_7"
    ],
    8: [
        "python",
        "-m",
        "Listas.ejercicio_lista_8"
    ],
    9: [
            "python",
            "-m",
            "Listas.ejercicio_lista_9"
        ],
    14: [
                "python",
                "-m",
                "Listas.ejercicio_lista_14"
            ],
    16: [
                    "python",
                    "-m",
                    "Listas.ejercicio_lista_16"
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
6: Determinar numero de ocurrencias
7: Eliminar elemento
8: Ordenar elementos
9: Calcular rango y contar elementos
10: Notificaciones de aplicacion
12: Combinar colas
13: Generar caracteres aleatoriamente
14: Semaforo
15: Fórmula de Haversine
16: Cola de prioridad
18: Turnos
19: Cola circular
20: Puesto de peaje
21: Adminitrar Aeropuerto
"""
lista_ejercicios_listas = """
1: contador de nodos    
2: eliminar vocales
3: dividir paridad
4: insertar nodos
5: eliminar primos
7: concatener listas
8: palindromo lista enlazada
9: cargar alumnos al curso
14: dados
16: proyecto de software
"""

print("Bienvenido al sistema de ejercicios")
while (True):
    print("")
    opcion = input("Ingrese el nombre del tipo ejercicios desea ver (Pilas),(Colas),(Listas): ").lower()
    if (opcion == "pilas"):
        print(lista_ejercicios_pilas)
        opcion = int(input("Escriba el numero del ejercicio que desea ejecutar: "))
        subprocess.run(ejercicios["Pilas"][opcion])
    elif (opcion == "colas"):
        print(lista_ejercicios_colas)
        opcion = int(input("Escriba el numero del ejercicio que desea ejecutar: "))
        subprocess.run(ejercicios["Colas"][opcion])
    elif (opcion == "listas"):
        print(lista_ejercicios_listas)
        opcion = int(input("Escriba el numero del ejercicio que desea ejecutar: "))
        subprocess.run(ejercicios["Listas"][opcion])
        