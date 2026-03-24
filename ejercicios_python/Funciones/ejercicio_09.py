#Procedimiento Intercambiar: Recibe dos números como parámetros de entrada y salida e intercambia sus valores si el segundo es mayor que el primero.

def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))

print("MCD:", calcular_mcd(numero1, numero2))