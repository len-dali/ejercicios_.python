# Leer fracciones
def leer_fraccion():
    num = int(input("Numerador: "))
    den = int(input("Denominador: "))
    return num, den


def escribir_fraccion(num, den):
    print("Resultado:", num, "/", den)


def sumar_fracciones(n1, d1, n2, d2):
    numr = n1*d2 + n2*d1
    denr = d1*d2
    return numr, denr


def restar_fracciones(n1, d1, n2, d2):
    numr = n1*d2 - n2*d1
    denr = d1*d2
    return numr, denr


def multiplicar_fracciones(n1, d1, n2, d2):
    numr = n1*n2
    denr = d1*d2
    return numr, denr


def dividir_fracciones(n1, d1, n2, d2):
    numr = n1*d2
    denr = d1*n2
    return numr, denr


while True:

    print("1.- Sumar dos fracciones")
    print("2.- Restar dos fracciones")
    print("3.- Multiplicar dos fracciones")
    print("4.- Dividir dos fracciones")
    print("5.- Salir")

    opcion = int(input("Opción: "))

    if opcion == 5:
        break

    if opcion >= 1 and opcion <= 4:
        print("Fracción 1:")
        num1, den1 = leer_fraccion()

        print("Fracción 2:")
        num2, den2 = leer_fraccion()

    if opcion == 1:
        print("Sumar fracciones")
        numr, denr = sumar_fracciones(num1, den1, num2, den2)
        escribir_fraccion(numr, denr)

    elif opcion == 2:
        print("Restar fracciones")
        numr, denr = restar_fracciones(num1, den1, num2, den2)
        escribir_fraccion(numr, denr)

    elif opcion == 3:
        print("Multiplicar fracciones")
        numr, denr = multiplicar_fracciones(num1, den1, num2, den2)
        escribir_fraccion(numr, denr)

    elif opcion == 4:
        print("Dividir fracciones")
        numr, denr = dividir_fracciones(num1, den1, num2, den2)
        escribir_fraccion(numr, denr)

    else:
        print("Opción incorrecta")