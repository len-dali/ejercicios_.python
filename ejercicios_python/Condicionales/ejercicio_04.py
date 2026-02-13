#Crea un programa que pida al usuario dos números y muestre su división

print('Calcular Disión') 

num_1 = int(input('Dime el número 1: '))
num_2 = int(input('Dime el número 2: '))
divisor = num_1/num_2

if divisor == 0:
   print ('No puedes dividir por 0');

else:
   print('La división es ',divisor)
