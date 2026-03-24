#Queremos guardar los nombres y la edades de los alumnos de un curso. 
#Realiza un programa que introduzca el nombre y la edad de cada alumno. 

nombres = []
edades = []

tam_vector = 30
indice = 0

while True:
    nombre = input("Dime el nombre de un alumno (o * para terminar): ")
    
    if nombre == "*":
        break
    
    edad = int(input("Dime su edad: "))
    
    nombres.append(nombre)
    edades.append(edad)
    
    indice += 1
    
    if indice == tam_vector:
        break

edad_max = edades[0]

for edad in edades:
    if edad > edad_max:
        edad_max = edad

print("\nAlumnos mayores de edad")
print("=======================")

for i in range(len(nombres)):
    if edades[i] >= 18:
        print(nombres[i])

print("\nAlumnos mayores")
print("===============")

for i in range(len(nombres)):
    if edades[i] == edad_max:
        print(nombres[i])