#/Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias y las clasifique en uno de estos estados:

#Entrada de datos
x1 = float(input("Coordenada x1: "))
y1 = float(input("Coordenada y1: "))
r1 = float(input("Radio r1: "))

x2 = float(input("Coordenada x2: "))
y2 = float(input("Coordenada y2: "))
r2 = float(input("Radio r2: "))

#Cálculo de la distancia 
distancia = ((x2 - x1)**2 + (y2 - y1)**2)

#Clasificación 
suma_radios = r1 + r2
resta_radios = abs(r1 - r2)

if distancia > suma_radios:
    print("Circunferencias exteriores")
elif distancia == suma_radios:
    print("Circunferencias tangentes exteriores")
elif resta_radios < distancia < suma_radios:
    print("Circunferencias secantes")
elif distancia == resta_radios:
    print("Circunferencias tangentes interiores")
elif 0 < distancia < resta_radios:
    print("Circunferencias interiores")
elif distancia == 0:
    print("Circunferencias concéntricas")