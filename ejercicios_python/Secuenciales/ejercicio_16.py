#Calcular adelantamiento

v1 = float(input('Dime la velocidad del coche 1 (k/h): '))
v2 = float(input('Dime la velocidad del coche 2 (mas lenta) (k/h): '))
distancia = float(input('Dime la distancia entre los dos coches (km): '))

tiempo_horas = distancia / (v1 - v2)
tiempo_minutos = tiempo_horas * 60


print(f"Lo alcanza en {tiempo_minutos:.2f} minutos.")