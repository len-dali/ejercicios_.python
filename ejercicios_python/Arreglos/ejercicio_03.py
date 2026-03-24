#Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10).

notas = []
tam_notas = 5

for i in range(tam_notas):
    while True:
        nota = float(input(f"Introduce la nota {i+1}: "))
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        else:
            print("Error: la nota debe estar entre 0 y 10")

nota_max = notas[0]
nota_min = notas[0]
suma = 0

for nota in notas:
    suma += nota
    
    if nota > nota_max:
        nota_max = nota
        
    if nota < nota_min:
        nota_min = nota


nota_media = suma / tam_notas

print("\nNotas:", end=" ")
for nota in notas:
    print(nota, end=" ")

print("\nNota media:", nota_media)
print("Nota máxima:", nota_max)
print("Nota mínima:", nota_min)