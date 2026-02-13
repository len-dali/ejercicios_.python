#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

dias_del_mes = 0

if mes in [1, 3, 5, 7, 8, 10, 12]:
    dias_del_mes = 31
elif mes in [4, 6, 9, 11]:
    dias_del_mes = 30
elif mes == 2:
    
    if (año % 4 == 0 and not (año % 100 == 0)) or (año % 400 == 0):
        dias_del_mes = 29
    else:
        dias_del_mes = 28
else:
    print("Mes no válido")


if dias_del_mes > 0:
    if dia < 1 or dia > dias_del_mes:
        print("Fecha incorrecta")
    else:
        print("Fecha correcta")