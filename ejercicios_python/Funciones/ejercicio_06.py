#/Procedimiento CalcularAreaPerimetro: recibe el radio de una circunferencia ydevuelve el área y el perímetro.

import math

def calcular_area_perimetro(radio):
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    return area, perimetro

radio = float(input("Introduce el radio: "))

area, perimetro = calcular_area_perimetro(radio)

print("Área:", area)
print("Perímetro:", perimetro)