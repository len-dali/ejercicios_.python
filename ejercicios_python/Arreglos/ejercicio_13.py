#De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros que conducen cada día de la semana.

nombres = []
kms = [] 

tam_conductores_max = 10
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

while True:
    num_conductores = int(input("¿Cuántos conductores tiene la empresa?: "))
    if num_conductores <= tam_conductores_max:
        break
    else:
        print(f"Como máximo puedo guardar la información de {tam_conductores_max} conductores")

for i in range(num_conductores):
    nombre = input(f"Nombre del conductor {i+1}: ")
    nombres.append(nombre)
    
    fila_kms = []
    
    
    for j in range(7):
        km = int(input(f"¿Cuántos km ha realizado el {dias[j]}?: "))
        fila_kms.append(km)
    
    
    fila_kms.append(0)
    kms.append(fila_kms)

for i in range(num_conductores):
    total = 0
    for j in range(7):
        total += kms[i][j]
    kms[i][7] = total

for i in range(num_conductores):
    print(f"{nombres[i]} ha realizado {kms[i][7]} kms.")