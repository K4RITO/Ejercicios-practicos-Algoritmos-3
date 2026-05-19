#Escribir un programa que calcule la suma (serie armónica 1+ 1/2 + 1/3 + ... + 1/n)

#donde "n" sea especificada por el usuario

numero = int(input("Ingrese un numero: "))

def serie_armonica(numero):
    serie = 0
    for i in range(1, numero + 1):
        serie = serie + 1/i
    return serie

resultado = serie_armonica(numero)
print("Resultado:", resultado)      