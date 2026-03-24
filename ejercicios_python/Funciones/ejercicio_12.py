# Función para validar la fecha

def validar_fecha(day, month, year):

    dias_mes = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]


    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        dias_mes[1] = 29

    if month < 1 or month > 12:
        return False

    if day < 1 or day > dias_mes[month - 1]:
        return False

    return True

def leer_fecha():
    while True:
        day = int(input("Día: "))
        month = int(input("Mes: "))
        year = int(input("Año: "))

        if validar_fecha(day, month, year):
            return day, month, year
        else:
            print("Fecha no válida")


def calcular_dia_juliano(d, m, a):

    dias_mes = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        dias_mes[1] = 29

    dia_juliano = d

    for i in range(m - 1):
        dia_juliano += dias_mes[i]

    return dia_juliano

d, m, a = leer_fecha()

print("Día Juliano:", calcular_dia_juliano(d, m, a))