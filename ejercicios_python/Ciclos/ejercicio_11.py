#Escribe un programa que diga si un número introducido por teclado es o no primo.

import math

numero = int(input("Introduce un numero para comprobar si es primo: "))
es_primo = True 

if numero <= 1 :
	es_primo = False

else:
	limite = math.isqrt(numero)
for num in range(2,limite + 1):
		if numero % num == 0:
		    es_primo = False
    
if es_primo:
	print("Es primo")
else:
	print("No es primo")
