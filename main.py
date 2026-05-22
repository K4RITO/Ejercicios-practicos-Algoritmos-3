import subprocess

ejercicios = {
    "Pilas": {
        1: [
            "python",
            r"Pilas/ejercicio_pila_1.py"
        ],

        2: [
            "python",
            r"Pilas\ejercicio_pila_2.py"
        ],

        3: [
            "python",
            r"Pilas\ejercicio_pila_3.py"
        ],

        4: [
            "python",
            r"Pilas\ejercicio_pila_4.py"
        ],

        5: [
            "python",
            r"Pilas\ejercicio_pila_5"
        ],

        6: [
            "python",
            r"Pilas\ejercicio_pila_6"
        ],

        7: [
            "python",
            r"Pilas\ejercicio_pila_7.py"
        ],

        8: [
            "python",
            r"Pilas\cartas.py"
        ],

        9: [
            "python",
            r"Pilas\factorial.py"
        ],

        11: [
            "python",
            r"Pilas\insertar_atenea.py"
        ],

        13: [
            "python",
            r"Pilas\contar_vocales.py"
        ],

        14: [
            "python",
            r"Pilas\encontrar_personajes.py"
        ],

        17: [
            "python",
            r"Pilas\ironman.py"
        ]
    }
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
11: 
13: 
14: 
17: 
"""
print("Bienvenido al sistema de ejercicios")
while (True):
    print("")
    opcion = input("Que tipo ejercicios desea ver (Pilas): ").lower()
    if (opcion == "pilas"):
        print(lista_ejercicios_pilas)
        opcion = int(input("Escriba el numero del ejercicio que desea ejecutar: "))
        subprocess.run(ejercicios["Pilas"][opcion])
        