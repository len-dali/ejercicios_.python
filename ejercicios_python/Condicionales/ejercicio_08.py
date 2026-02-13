#Algoritmo que pida dos números 'nota' y 'edad' y un carácter 'sexo'

nota = int(input('Introduce la nota:'))
edad = int(input('Introduce la edad:'))
sexo = input('Introduce el sexo (F/M):').upper()

if nota >= 5 and edad >= 18:
	if sexo == "F":
		print('ACEPTADA')
	elif sexo =="M":
		print('Posible')
	else:
		print('No Aceptada')
else:
	print('No Aceptada')

