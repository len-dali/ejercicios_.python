#Calcular vectores, maximos y minimos

import random
def calcular_max_min(lista):
    vmax = lista[0]
    vmin = lista[0]

    for i in range(len(lista)):
        if lista[i] > vmax:
            vmax = lista[i]
        if lista[i] < vmin:
            vmin = lista[i]

    return vmax, vmin


lista = []

for i in range(10):
    lista.append(random.randint(1, 100))


vmax, vmin = calcular_max_min(lista)

print("Lista generada:", lista)
print("El valor máximo es", vmax)
print("El valor mínimo es", vmin)