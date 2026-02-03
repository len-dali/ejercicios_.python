 #Escribe un programa que lea un número e indique si es par o impar.

print('Calcular Par e Impar')

numero = int(input('Dime el número: '))

if numero % 2 == 0:
	print(numero, ('es par'))
else:
    print(numero, ('es impar')) 

print('Fin')
