#Aplicación que permita adivinar un número.

import random

intentos = 10
num_secreto = random.randint(1, 100)

print("Adivine el número (de 1 a 100):")
num_ingresado = int(input())

while num_secreto != num_ingresado and intentos > 1:
    if num_secreto > num_ingresado:
        print("Muy bajo")
    else:
        print("Muy alto")
    
    intentos -= 1
    print("Le quedan", intentos, "intentos:")
    num_ingresado = int(input())

if num_secreto == num_ingresado:
    print("¡Exacto! Usted adivinó en", 11 - intentos, "intentos.")
else:
    print("El número era:", num_secreto)
