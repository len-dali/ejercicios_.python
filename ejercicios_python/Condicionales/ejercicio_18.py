#Dia de la Semana

dia_num = int(input("Dime un día de la semana (1-7): "))

semana = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

resultado = semana.get(dia_num, "Día incorrecto")
print(resultado)