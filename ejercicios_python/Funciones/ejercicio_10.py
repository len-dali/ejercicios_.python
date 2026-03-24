#Función Convertir_A_Segundos

def convertir_a_segundos(hor, min, seg):
    return hor * 3600 + min * 60 + seg


def convertir_a_hms(segundos):
    hor = segundos // 3600
    min = (segundos % 3600) // 60
    seg = segundos % 60
    return hor, min, seg


while True:
    print("1.- Convertir a segundos")
    print("2.- Convertir a horas, minutos y segundos")
    print("3.- Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        hor = int(input("Horas: "))
        min = int(input("Minutos: "))
        seg = int(input("Segundos: "))
        print("Corresponde a", convertir_a_segundos(hor, min, seg), "segundos.")

    elif opcion == 2:
        segund = int(input("Segundos: "))
        hor, min, seg = convertir_a_hms(segund)
        print("Corresponde a", hor, ":", min, ":", seg)

    elif opcion == 3:
        break
    else:
        print("Opción incorrecta")