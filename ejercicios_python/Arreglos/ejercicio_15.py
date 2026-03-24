#Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. 

num_equipos = 15

equipos = []      #nombres
resultados = []   #goles

for i in range(num_equipos):
    equipo1 = input(f"Introduce el nombre del equipo 1 del partido {i+1}: ")
    equipo2 = input(f"Introduce el nombre del equipo 2 del partido {i+1}: ")
    
    goles1 = int(input(f"Goles de {equipo1}: "))
    goles2 = int(input(f"Goles de {equipo2}: "))
    
    equipos.append([equipo1, equipo2])
    resultados.append([goles1, goles2])

print("\nQUINIELA")
print("========")


for i in range(num_equipos):
    if resultados[i][0] > resultados[i][1]:
        resultado = "1"
    elif resultados[i][0] < resultados[i][1]:
        resultado = "2"
    else:
        resultado = "X"
    
    print(f"{equipos[i][0]} - {equipos[i][1]} -> {resultado}")