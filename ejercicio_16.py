#Calcular coste de telefono

tiempo = int(input("¿Cuánto tiempo duró la llamada (min)?: "))
es_domingo = input("¿Es domingo? (S/N): ").upper()


if tiempo < 5:
    coste = tiempo * 100
elif tiempo < 8:
    coste = (tiempo - 5) * 80 + 500
elif tiempo < 10:
    coste = (tiempo - 8) * 70 + 240 + 500
else:
    coste = (tiempo - 10) * 50 + 140 + 240 + 500

if es_domingo == "S":
    coste += coste * 0.03
else:
    turno = input("¿Qué turno? Mañana (M) o Tarde (T): ").upper()
    if turno == "M":
        coste += coste * 0.15
    else:
        coste += coste * 0.10


print(f"El coste de la llamada es: {coste / 100:.2f} euros.")