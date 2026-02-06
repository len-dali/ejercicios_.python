#Programa que lea 3 datos de entrada A, B y C. 

#Entrada de datos
ladoA = float(input("Introduce longitud lado A: "))
ladoB = float(input("Introduce longitud lado B: "))
ladoC = float(input("Introduce longitud lado C: "))

#Verificación de Triángulo Rectángulo 

if (ladoA**2 + ladoB**2 == ladoC**2) or \
   (ladoB**2 + ladoC**2 == ladoA**2) or \
   (ladoC**2 + ladoA**2 == ladoB**2):
    print("Triángulo Rectángulo")

#Clasificación por sus lados
if (ladoA == ladoB and ladoA != ladoC) or \
   (ladoB == ladoC and ladoB != ladoA) or \
   (ladoC == ladoA and ladoC != ladoB):
    print("Triángulo Isósceles")
else:
    if ladoA == ladoB and ladoA == ladoC:
        print("Triángulo Equilátero")
    else:
        print("Triángulo Escaleno")