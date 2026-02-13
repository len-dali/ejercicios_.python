#Calcular el coste de Autobus

num_alumnos = int(input("¿Cuántos alumnos participan en la actividad?: "))


if num_alumnos >= 100:
    coste_por_alumno = 65
elif 50 <= num_alumnos <= 99:
    coste_por_alumno = 70
elif 30 <= num_alumnos <= 49:
    coste_por_alumno = 95
elif 0 < num_alumnos < 30:
    coste_por_alumno = 4000 / num_alumnos
else:
    coste_por_alumno = 0


if num_alumnos > 0:
    coste_total = num_alumnos * coste_por_alumno
    print(f"El coste por alumno es {coste_por_alumno} euros.")
    print(f"El coste total del autobús es {coste_total} euros.")
else:
    print("El número de alumnos debe ser un valor positivo.")