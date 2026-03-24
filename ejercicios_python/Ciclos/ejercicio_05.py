#Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL'

while True:
    
    while True:
        car = input("Introduce un carácter: ")
        if len(car) == 1:
            break
        else:
            print("Por favor, introduce solo un carácter.")

    
    if car == " ":
        break

    if car.upper() in ["A", "E", "I", "O", "U"]:
        print("VOCAL")
    else:
        print("NO VOCAL")

salir = input("¿Quiere salir? ")

