#Calcular multiplos

num_1 = int(input("Número 1: "))
num_2 = int(input("Número 2: "))
es_multiplo = num_1 % num_2

if num_1 % num_2 == 0:
    print(num_1, "es múltiplo de", num_2)
else:
    print(num_1, "no es múltiplo de", num_2)    
