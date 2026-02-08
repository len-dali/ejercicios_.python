#Calcular Distancia Entre Puntos

import math
print("Dime las coordenadas del punto 1:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))

print("Dime las coordenadas del punto 2:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))


distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"Distancia entre puntos: {distancia:.2f}")