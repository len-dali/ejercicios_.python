#Calcular puntos

correctas = int(input("Dime cantidad de respuestas correctas: "))
incorrectas = int(input("Dime cantidad de respuestas incorrectas: "))

puntos = (correctas * 5) + (incorrectas * -1)

print(f"Puntos totales: {puntos}")