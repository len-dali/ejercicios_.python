#Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

print("TABLAS DE MULTIPLICAR DEL 1 AL 5")

for tabla in range(1, 6):
    
    
    for num in range(1, 11):
        print(tabla, "*", num, "=", tabla * num)
    
    input("Presiona Enter para continuar con la siguiente tabla.")

