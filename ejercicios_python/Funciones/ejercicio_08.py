#Función CalcularFactorial

def calcular_factorial(numero):
    factorial = 1
    
    for i in range(1, numero + 1):
        factorial = factorial * i
        
    return factorial

numero1 = int(input("Número: "))

print("El factorial es:", calcular_factorial(numero1))