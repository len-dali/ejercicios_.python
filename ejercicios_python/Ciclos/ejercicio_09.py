#Calcular potencia


base = float(input("Dame la base de la potencia: "))


while True:
    exponente = int(input("Dame el exponente de la potencia: "))
    
    if exponente < 0:
        print("ERROR: El exponente debe ser positivo")
    else:
        break

potencia = 1

for i in range(1, exponente + 1):
    potencia = potencia * base

print("Potencia:", potencia)