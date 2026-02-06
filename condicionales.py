# Condicionales con Python

# if,else,elif

""""
if ex_bool:
	instrucciones:
else:
    instruccciones

if exp_bool:
    instrucciones
elif expo_bool:
    instrucciones
else:
    instrucciones
"""                	

print('Inicio')

numero = int(input('Ingresa un numero: '))

if numero>0:
	print('Es un numero Positivo ')
elif numero == 0:
    print('Es cero')	
else:
    print('No es un numero Positivo')	

print('Fin')	
