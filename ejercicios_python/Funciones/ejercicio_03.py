#Calcular temperatura media

def CalcularTemperaturaMedia(tmin, tmax):
    return (tmin + tmax) / 2
cantidad = int(input("¿Cúantas temperaturas vas a calcular?: "))

for indice in range (1, cantidad +1):
    tmin = float(input("Introduce la temperatura mínima: "))
    tmax = float(input("Introduce la temperatura máxima: "))

print("Temperatura media:", CalcularTemperaturaMedia (tmin, tmax))