#Dado


cara = int(input("Introduce el número de la cara (1-6): "))

opuestos = {
    1: "SEIS",
    2: "CINCO",
    3: "CUATRO",
    4: "TRES",
    5: "DOS",
    6: "UNO"
}

if cara in opuestos:
    print(opuestos[cara])
else:
    print("Error: número incorrecto.")