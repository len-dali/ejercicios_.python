#Algoritmo que pida números hasta que se introduzca un cero.

suma = 0
cont = 0

while True:
    try:
        num = int(input("Número (0 para salir): "))
    except ValueError:
        print("Ingrese solo números.")
        continue

    suma += num

    if num != 0:
        cont += 1

    if num == 0:
        break

if cont != 0:
    media = suma / cont
else:
    media = 0

print("Suma:", suma)
print("Media:", media)
