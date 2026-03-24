#Función EsBisiesto

def leer_fecha():
    d = int(input("Día: "))
    m = int(input("Mes: "))
    a = int(input("Año: "))
    return d, m, a


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