#/Crear un vector de 5 elementos de cadenas de caracteres, inicializa el vector con datos leídos por el teclado.


vector1 = []
vector2 = []

tam_vector = 5

for i in range(tam_vector):
    cadena = input(f"Dame la cadena {i+1}: ")
    vector1.append(cadena)

for i in range(tam_vector - 1, -1, -1):
    vector2.append(vector1[i])

for i in range(tam_vector):
    print(f"La cadena {i+1}: {vector2[i]}")