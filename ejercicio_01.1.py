#Aplicacion de factoriales

num = int(input("Dime un número: "))
resultado = 1

for contador in range(2, num + 1):
    resultado *= contador

print("El resultado es", resultado)
