#Algoritmo que pida un número y diga si es positivo, negativo o 0.

num_1 = int(input('Dime el numero: '))

if num_1 == 0:
	print('Es igual a 0')
elif  num_1 > 0:
    print('Es positivo')
else: 
  if num_1 < 0: (print('Es negativo'))  

print('Fin')