#Un alumno desea saber cual será su calificación final en la materia de Algoritmos

parcial1= float(input("Dime la nota del parcial 1: "))
parcial2= float(input("Dime la nota del parcial 2: "))
parcial3 = float(input("Dime la nota del parcial 3: "))
examen = float(input("Dime la nota del examen: "))
trabajo = float(input("Dime la nota del trabajo: "))


nota_final = ((parcial1 + parcial2 + parcial3) / 3) * 0.55 + (0.3 * examen) + (0.15 * trabajo)


print(f"Nota final: {nota_final:.2f}")
